-- create database db;

create table IF NOT EXISTS student(
    id integer primary key AUTOINCREMENT,
    NAME VARCHAR(100) NOT NULL, 
    address VARCHAR(100)
);


select * FROM  student;