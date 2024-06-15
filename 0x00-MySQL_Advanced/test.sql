-- Active: 1718468356831@@127.0.0.1@3306@hbtn
-- Let's create a table
SELECT * FROM users;

UPDATE users SET email = 'bob@dylan.com' WHERE email = 'bob+new@dylan.com';