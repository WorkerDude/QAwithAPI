from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict


class AnswerBase(BaseModel):
    user_id: str
    text: str


class AnswerCreate(AnswerBase):
    pass


class Answer(AnswerBase):
    id: int
    question_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class QuestionBase(BaseModel):
    text: str


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int
    created_at: datetime
    answers: List[Answer] = []

    model_config = ConfigDict(from_attributes=True)