from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=1, le=120)
    city: str = Field(..., min_length=1)


# 👇 THIS CLASS IS REQUIRED FOR ACTIVITY 4
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    city: str
