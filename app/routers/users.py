from fastapi import APIRouter
from app.models.user import User
from app.database.db import vinculacion

router = APIRouter()

@router.get("/users")
def get_users():
    db = vinculacion()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    db.close()
    return users

@router.post("/users")
def create_user(user: User):
    db = vinculacion()
    cursor = db.cursor()

    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (user.name, user.email))
    db.commit()
    
    cursor.close()
    db.close()

    return {"message": "User created"}

@router.get("/users/{user_id}")
def get_user(user_id: int):
    db = vinculacion()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()

    cursor.close()
    db.close()
    if user:
        return user
    return {"error": "User not found"}

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = vinculacion()
    cursor = db.cursor()

    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    db.commit()

    cursor.close()
    db.close()
    return {"message": "User deleted"}

@router.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    db = vinculacion()
    cursor = db.cursor()

    query = "UPDATE users SET name=%s, email=%s WHERE id=%s"
    cursor.execute(query, (user.name, user.email, user_id))
    db.commit()
    
    cursor.close()
    db.close()
    return {"message": "User updated"}