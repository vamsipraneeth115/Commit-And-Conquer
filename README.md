# Commit And Conquer

## Overview
The repository contains a full-stack application with a **Next.js** frontend and a **FastAPI** backend, with connection to a postgresql (use of neondb is recommended).

## Folder Structure
```
repo-root/
├── CLIENT/   # Next.js frontend application
├── SERVER/   # FastAPI backend
```

---

## Prerequisites
- Ensure you have **Node.js** installed for setting up nextjs.
-  **Python 3** installed for setting up FASTAPI .


## Setup Instructions

### CLIENT (Frontend - Next.js)

1. Navigate to the `CLIENT` folder:
   ```sh
   cd CLIENT
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm run dev
   ```
4. The frontend should now be running at `http://localhost:3000`

---

### SERVER (Backend - FastAPI)

1. Navigate to the `SERVER` folder:
   ```sh
   cd SERVER
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment:
   - **Windows:**
     ```sh
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```sh
     source venv/bin/activate
     ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Generate Prisma client:
   ```sh
   prisma generate
   ```
6. Start the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```
7. The backend should now be running at `http://localhost:8000`

---


## Contributing Guidelines


1. **Fork the repository** and clone it locally:
   
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
4. Make your changes in the `main` branch of your fork.
5. Commit your changes with a structured message:
   - Format:
     ```
     Update <file-name>
     
     Fixes #<issue-number>  
     Team <team-id>
     ```
   - Example:
     ```
     Update main.dart
     
     Fixes #1  
     Team 12
     ```
6. Push your changes to your forked repository:
   ```sh
   git push origin main
   ```
7. Go to the **original repository** and create a **pull request (PR)** from your fork’s `main` branch.

8. A maintainer will review and merge your PR.

 **DO NOT MERGE YOUR CODE TO THE MAIN BRANCH OF THE MAIN REPOSITORY**

---



## Notes
- The frontend and backend should run concurrently for full functionality.
- Modify environment variables as needed.

---

<!-- LEADERBOARD_START -->



<!-- LEADERBOARD_END -->





