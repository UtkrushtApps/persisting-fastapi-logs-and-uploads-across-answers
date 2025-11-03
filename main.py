from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os
import shutil
import logging
from datetime import datetime

app = FastAPI()

LOGS_PATH = "logs"
UPLOADS_PATH = "uploads"
os.makedirs(LOGS_PATH, exist_ok=True)
os.makedirs(UPLOADS_PATH, exist_ok=True)

# Configure logging
def get_logger():
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(os.path.join(LOGS_PATH, "app.log"))
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    fh.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(fh)
    return logger

@app.post("/upload/")
def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOADS_PATH, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    logger = get_logger()
    logger.info(f"Uploaded file: {file.filename}")
    return {"info": f"file '{file.filename}' saved"}

@app.get("/log/")
def write_log(message: str):
    logger = get_logger()
    logger.info(f"Manual log: {message}")
    return {"info": f"logged message: '{message}'"}

@app.get("/logs/")
def list_logs():
    logs = []
    for f in os.listdir(LOGS_PATH):
        if f.endswith(".log"):
            logs.append(f)
    return {"log_files": logs}

@app.get("/uploads/")
def list_uploads():
    uploads = os.listdir(UPLOADS_PATH)
    return {"uploads": uploads}
