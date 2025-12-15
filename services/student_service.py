from sqlalchemy import text
from db.database import get_connection


def create_student(student):
    query = text(
        "INSERT INTO students (name, age, city) VALUES (:name, :age, :city)"
    )
    conn = get_connection()
    conn.execute(query, student)
    conn.commit()
    conn.close()


def get_all_students():
    conn = get_connection()
    result = conn.execute(text("SELECT * FROM students"))

    students = []
    for row in result:
        students.append({
            "id": row.id,
            "name": row.name,
            "age": row.age,
            "city": row.city
        })

    conn.close()
    return students


def get_student_by_id(student_id):
    conn = get_connection()
    result = conn.execute(
        text("SELECT * FROM students WHERE id = :id"),
        {"id": student_id}
    )
    row = result.fetchone()
    conn.close()

    if row:
        return {
            "id": row.id,
            "name": row.name,
            "age": row.age,
            "city": row.city
        }
    return None


def update_student(student_id, student):
    conn = get_connection()
    conn.execute(
        text(
            "UPDATE students SET name=:name, age=:age, city=:city WHERE id=:id"
        ),
        {**student, "id": student_id}
    )
    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = get_connection()
    conn.execute(
        text("DELETE FROM students WHERE id=:id"),
        {"id": student_id}
    )
    conn.commit()
    conn.close()
