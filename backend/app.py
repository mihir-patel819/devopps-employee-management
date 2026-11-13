
import os
from flask import Flask, jsonify, request
import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword"),
        database=os.getenv("DB_NAME", "employee_db")
    )

@app.route("/api/health")
def health():
    return jsonify({"status": "healthy", "application": "Employee Management API"})

@app.route("/api/employees", methods=["GET"])
def get_employees():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(employees)

@app.route("/api/employees", methods=["POST"])
def add_employee():
    data = request.get_json()

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO employees (name, email, department) VALUES (%s, %s, %s)",
        (data["name"], data["email"], data["department"])
    )
    db.commit()
    cursor.close()
    db.close()

    return jsonify({"message": "Employee added successfully"}), 201

@app.route("/api/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "Employee deleted successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# Practicing Git: my first code change
# this is a test change to see if I can commit and push changes to the repository.
# some more changes to test the git commit and push functionality.


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    cursor = mysql.connection.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE email = %s",
        (email,)
    )

    employee = cursor.fetchone()
    cursor.close()

    if employee:
        return jsonify({
            "message": "Employee found. Login authentication is not configured yet."
        }), 200

    return jsonify({
        "message": "Employee not found"
    }), 401
