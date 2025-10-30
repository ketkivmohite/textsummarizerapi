from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load Hugging Face summarization pipeline
summarizer = pipeline("summarization")

class TextIn(BaseModel):
    text: str

@app.post("/summarize")
def summarize_text(data: TextIn):
    summary = summarizer(data.text, max_length=50, min_length=25, do_sample=False)
    return {"summary": summary[0]["summary_text"]}
