-- CreateTable
CREATE TABLE "Internship" (
    "id" SERIAL NOT NULL,
    "title" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "company" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "stipend" INTEGER NOT NULL,
    "duration" INTEGER NOT NULL,

    CONSTRAINT "Internship_pkey" PRIMARY KEY ("id")
);
