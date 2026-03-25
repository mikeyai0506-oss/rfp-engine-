from fastapi import FastAPI, UploadFile, File
import shutil
from parser import extract_text, extract_questions
from ai_engine import generate_answer

app = FastAPI()

@app.post("/upload-rfp/")
async def upload_rfp(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)
    questions = extract_questions(text)

    responses = []

    for q in questions:
        answer = generate_answer(q)
        responses.append({
            "question": q,
            "answer": answer
        })

    return {
        "total_questions": len(questions),
        "responses": responses
    }