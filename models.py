from pydantic import BaseModel, Field, field_validator
from typing import ClassVar

class User(BaseModel):
    name: str
    age: int


class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)

    words: ClassVar[list[str]] = ["кринж", "рофл", "вайб"]

    @field_validator('message')
    @classmethod
    def validate_message(cls, v):

        vlower = v.lower()
        for i in cls.words:
            if i in vlower:
                raise ValueError('Использование недопустимых слов')
        return v