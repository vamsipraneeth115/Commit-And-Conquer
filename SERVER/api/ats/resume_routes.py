from fastapi import APIRouter, UploadFile, File, HTTPException, Form, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
from typing import List, Optional, Dict, Any
import os
import shutil
import tempfile
import uuid
from datetime import datetime
import json

from .ats_resume_reader import parse_resume, batch_process_resumes, ResumeParsingError

# Create router
router = APIRouter(
    prefix="/ats",
    tags=["ats"],
    responses={404: {"description": "Not found"}},
)

# Temporary directory for storing uploaded resumes
UPLOAD_DIR = os.path.join(tempfile.gettempdir(), "ats_resumes")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/parse-resume")
async def parse_single_resume(
    resume_file: UploadFile = File(...),
    background_tasks: BackgroundTasks = None
):
    
    file_extension = os.path.splitext(resume_file.filename)[1]
    temp_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, temp_filename)
    
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(resume_file.file, buffer)
        result = parse_resume(file_path)
        result["original_filename"] = resume_file.filename
        result["parsed_at"] = datetime.now().isoformat()
        if background_tasks:
            background_tasks.add_task(os.remove, file_path)
        
        return result
    
    except ResumeParsingError as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=422, detail=str(e))
    
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

@router.post("/batch-parse-resumes")
async def parse_multiple_resumes(
    resume_files: List[UploadFile] = File(...),
    background_tasks: BackgroundTasks = None
):
    batch_id = str(uuid.uuid4())
    batch_dir = os.path.join(UPLOAD_DIR, batch_id)
    os.makedirs(batch_dir, exist_ok=True)
    
    saved_files = []
    
    try:
        for resume_file in resume_files:
            file_extension = os.path.splitext(resume_file.filename)[1]
            temp_filename = f"{uuid.uuid4()}{file_extension}"
            file_path = os.path.join(batch_dir, temp_filename)
            
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(resume_file.file, buffer)
            
            saved_files.append({
                "path": file_path,
                "original_filename": resume_file.filename
            })

        results = batch_process_resumes(batch_dir)
        for i, result in enumerate(results):
            if i < len(saved_files):
                result["original_filename"] = saved_files[i]["original_filename"]
            result["parsed_at"] = datetime.now().isoformat()
  
        if background_tasks:
            background_tasks.add_task(shutil.rmtree, batch_dir)
        
        return results
    
    except Exception as e:
        if os.path.exists(batch_dir):
            shutil.rmtree(batch_dir)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

@router.get("/resume-stats")
async def get_resume_stats(
    resume_data: Dict[str, Any]
):
    
    try:
        skill_count = len(resume_data.get("skills", []))
        experience_count = len(resume_data.get("experience", []))
        exp_length = 0
        for exp in resume_data.get("experience", []):
            if "description" in exp:
                exp_length += len(exp["description"])
        
        return {
            "skill_count": skill_count,
            "experience_count": experience_count,
            "experience_length": exp_length,
            "has_email": resume_data.get("email") is not None,
            "has_name": resume_data.get("name") is not None
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while calculating stats: {str(e)}") 