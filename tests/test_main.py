from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def setup_module(module):
    Base.metadata.create_all(bind=engine)


def test_create_question():
    response = client.post("/questions/", json={"text": "What is Python?"})
    assert response.status_code == 201
    assert response.json()["text"] == "What is Python?"
    assert "id" in response.json()


def test_cascade_delete():
    q_res = client.post("/questions/", json={"text": "To be deleted"})
    q_id = q_res.json()["id"]

    client.post(f"/questions/{q_id}/answers/", json={"user_id": "u1", "text": "Answer"})

    del_res = client.delete(f"/questions/{q_id}")
    assert del_res.status_code == 204

    get_q = client.get(f"/questions/{q_id}")
    assert get_q.status_code == 404