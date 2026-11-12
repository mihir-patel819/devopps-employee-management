CREATE DATABASE IF NOT EXISTS employee_db;

USE employee_db;

CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    department VARCHAR(100) NOT NULL
);

INSERT IGNORE INTO employees (name, email, department)
VALUES
('Rahul Sharma', 'rahul@example.com', 'IT'),
('Priya Patel', 'priya@example.com', 'HR'),
('Amit Shah', 'amit@example.com', 'DevOps');