from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

app = FastAPI(title="QA Service API")

@app.get("/questions/", response_model=List[schemas.Question])
def read_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_questions(db, skip=skip, limit=limit)

@app.post("/questions/", response_model=schemas.Question, status_code=status.HTTP_201_CREATED)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.create_question(db=db, question=question)

@app.get("/questions/{question_id}", response_model=schemas.Question)
def read_question(question_id: int, db: Session = Depends(get_db)):
    db_question = crud.get_question(db, question_id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question

@app.delete("/questions/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    success = crud.delete_question(db, question_id=question_id)
    if not success:
        raise HTTPException(status_code=404, detail="Question not found")
    return None

@app.post("/questions/{question_id}/answers/", response_model=schemas.Answer, status_code=status.HTTP_201_CREATED)
def create_answer_for_question(question_id: int, answer: schemas.AnswerCreate, db: Session = Depends(get_db)):
    db_question = crud.get_question(db, question_id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return crud.create_answer(db=db, answer=answer, question_id=question_id)

@app.get("/answers/{answer_id}", response_model=schemas.Answer)
def read_answer(answer_id: int, db: Session = Depends(get_db)):
    db_answer = crud.get_answer(db, answer_id=answer_id)
    if db_answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    return db_answer

@app.delete("/answers/{answer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    success = crud.delete_answer(db, answer_id=answer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Answer not found")
    return None