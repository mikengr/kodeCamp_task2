from fastapi import FastAPI, File, UploadFile, HTTPException


app = FastAPI()


@app.post("/files/")
async def file_upload(file: UploadFile = File(...)):
    if file.filename == "":
        raise HTTPException(status_code=406, detail="upload a valid file")
    return {
        "name": file.filename,
        "img_type": file.content_type,
        "properties": file.file,
        }