from fastapi import APIRouter, UploadFile, File
import shutil

router = APIRouter()

UPLOAD_DIR = "uploads"


@router.post("/upload")

async def upload_file(
    file: UploadFile = File(...)
):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "filename": file.filename,
        "path": file_path
    }