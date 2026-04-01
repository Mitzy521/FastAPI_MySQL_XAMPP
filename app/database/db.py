import mysql.connector

def vinculacion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fastapi_python"
    )

db = vinculacion()
cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE
    );
""")

print("Tabla completada o existente.")

db.commit()
cursor.close()
db.close()

print("\nConexión cerrada.")
