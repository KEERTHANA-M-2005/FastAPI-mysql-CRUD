# FastAPI MySQL CRUD

A backend project built using **FastAPI** that demonstrates **RESTful CRUD operations** with **MySQL** using **SQLAlchemy (Raw SQL)**.  
The project also includes **input validation**, **response models**, and **custom error handling**.

---

## 📌 Features

- FastAPI-based REST APIs  
- CRUD operations with MySQL  
- SQLAlchemy **Raw SQL** (no ORM models)  
- Pydantic request & response models  
- Input validation  
- Custom **404 error handling**  
- Swagger UI for API testing  

---

## 🗂 Project Structure

project/
├── main.py
├── routes/
├── services/
├── models/
├── db/
├── utils/

yaml
Copy code

---

## 🔗 API Endpoints

### Students API

| Method | Endpoint | Description |
|------|---------|-------------|
| POST | `/students` | Create a new student |
| GET | `/students` | Get all students |
| GET | `/students/{id}` | Get student by ID |
| PUT | `/students/{id}` | Update student details |
| DELETE | `/students/{id}` | Delete a student |

---

## 🛠 Tech Stack

- Python  
- FastAPI  
- MySQL  
- SQLAlchemy (Raw SQL)  
- PyMySQL  
- Uvicorn  

---

## ▶️ How to Run

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy pymysql

# Run server
uvicorn main:app --reload
🌐 Open in Browser
arduino
Copy code
http://127.0.0.1:8000/docs
🧪 Sample Request (POST /students)
json
Copy code
{
  "name": "Keerthana",
  "age": 22,
  "city": "Bangalore"
}
---
##📘 Learning Outcomes
Built RESTful APIs using FastAPI

Implemented CRUD operations with MySQL

Used SQLAlchemy Raw SQL for database interaction

Applied input validation and error handling

Designed clean and structured API responses

---
###👤 Author
Keerthana M

⭐ Notes
Virtual environment files are excluded using .gitignore

APIs can be tested using Swagger UI

yaml
Copy code

---
