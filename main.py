from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User
from models import Feedback
app = FastAPI()
feedbacks: list[Feedback] = []
@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.post("/calculate")
def calculate(num1: float, num2: float):
    return {"result": num1 + num2}

user = User(
    name="Змеев Илья",
    age=1
)
@app.get("/users")
def get_user():
    return user

def isAdult(age: int) -> bool:
    return age >= 18

@app.post("/user")
def create_user(use: User):
    is_adult = isAdult(use.age)
    return {
        "name": use.name,
        "age": use.age,
        "is_adult": is_adult
    }


@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    }