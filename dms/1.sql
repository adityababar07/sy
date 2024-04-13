create Database sy1_student_;

use sy1_student_;

create Table student (
roll_no int  primary key auto_increment,
name varchar(100) not null,
address varchar(100),
marks int not null
);

insert into student (name, town, marks) values  ("aditya", "bedag", 83),
("Leyona", "travancoor", 93),
("alan", "london", 85),
("Roy", "malapuram", 73),
("aboobacker", "adimally", 86),
("Sidique", "painavu", 94),
("kunjilakshmi", "vangikavalla", 92),
("Mathew", "adimally", 88),
("laura", "adimally", 96),
("aleena", "pallikavala", 83);

select * from student;

select * FROM STUDENT WHERE town="adimally";

select * from student where marks>=90;

select name from student where marks<=90 and marks>= 85;

select * from student where roll_no between 3 and 8;

select * from student where roll_no in (3, 8);

select name, marks from student order by marks desc limit 4;



-- if error shown
SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

select name, count(town)  from student where roll_no > 6 group by town, name having town="adimally";

select count(name),count(town)  from student group by town having town="adimally";

Alter Table student rename column address to town;

delete from student where roll_no=10;

update  student  set roll_no=10 where roll_no=11;

alter table student add column class varchar(3);

alter table drop class;

drop table student;

show tables;

delete from  student  class; 

update  student  set class="sy" where roll_no=10;

select count(class ), class from student group by class;

select *  from student where name like "a%";

select * from student where name like "_a%a";

select  min(marks) from student ;
select  min(marks) from student ;
select avg(marks) from student;
select sum(marks) from student;

select name, marks from student order by marks asc;

select name, marks from student order by marks asc limit 3;

select class, min(marks), max(marks), avg(marks), sum(marks) from student group by class order by class asc ;



+-------+
| class |
+-------+
| sy    |
| fy    |
| ty    |
+-------+
3 rows in set (0.000 sec)








