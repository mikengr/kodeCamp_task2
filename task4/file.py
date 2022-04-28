from fastapi import FastAPI, File, UploadFile, HTTPException


app = FastAPI()


@app.post("/files/")
async def file_upload(file: UploadFile = File(default=None)):
    if file is None:
        raise HTTPException(status_code=404, detail="no file uploaded")
    return {
        "name": file.filename,
        "img_type": file.content_type,
        "properties": file.file,
        }