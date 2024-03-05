-- create DATABASE if NOT EXISTS db;

create table IF NOT EXISTS student(
    id integer primary key AUTOINCREMENT,
    NAME VARCHAR(100) NOT NULL, 
    address VARCHAR(100)
);


select * FROM  student;


INSERT INTO student  VALUES ("aditya babar", 'sangli')



