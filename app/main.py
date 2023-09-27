from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv
from uploads import UploadType
from pypdf import PdfReader
import uvicorn
import os


load_dotenv()
os.makedirs('./static', exist_ok=True)
os.makedirs('./uploads', exist_ok=True)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def upload(request: Request, file: UploadFile):
    content: str = ""
    try:
        contents = file.file.read()
        path = f"uploads/{file.filename}"
        with open(path, 'wb') as f:
            f.write(contents)

            if file.content_type == UploadType.PDF.value:
                reader = PdfReader(path)
                content = reader.pages[0].extract_text()
            else:
                content = contents.decode()

    except Exception as e:
        return templates.TemplateResponse("error.html", {"request": request, "error": e})
    finally:
        file.file.close()

    return templates.TemplateResponse("file.html", {"request": request, "file_name": file.filename, "content": content})


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
