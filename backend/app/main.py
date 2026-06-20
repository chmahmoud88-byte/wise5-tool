
from fastapi import FastAPI, UploadFile, File
from app.wise5 import WISE5Scorer
from app.bagi import BAGIScorer
from app.extract import extract_text

app = FastAPI()

@app.get('/health')
def health(): return {'status':'ok'}

@app.post('/score')
def score(data:dict):
    return WISE5Scorer().score(data)

@app.post('/bagi')
def bagi(data:dict):
    return BAGIScorer().score(data)

@app.post('/extract-and-score')
async def extract_and_score(file:UploadFile=File(...)):
    text=(await file.read()).decode(errors='ignore')
    parsed=extract_text(text)
    result=WISE5Scorer().score(parsed)
    return {'parsed':parsed,'score':result}

from fastapi.responses import FileResponse
import os

@app.get("/")
def home():
    return FileResponse(os.path.join(os.getcwd(), "../frontend/index.html"))

