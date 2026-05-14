--Creates database.
CREATE DATABASE miniproject;

--Creates tables.
---Products table.
CREATE TABLE products (
id 
INT 
PRIMARY KEY,
name
VARCHAR(50),
price
float
);

---Couriers table.
CREATE TABLE couriers (
id 
INT 
PRIMARY KEY,
name
VARCHAR(50),
phone
INT
);