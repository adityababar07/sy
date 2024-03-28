use sy1_student_;

create table clients(
c_id int primary key,
c_name varchar(100) not null
);

insert into clients values (4, 'sanjana'),
(5, 'rohan'),
(6, 'arun');

select * from  clients;

create table project(
p_id int primary key,
e_id int ,
c_id int,
p_date Date ,
foreign key (e_id) references emp(id),
foreign key (c_id) references clients(c_id)
);

insert into project values (2345, 1, 4, 20120126),
(9876, 2, 5, 20190228),
(3455, 3, 6, 20171012);

select * from  project;




MariaDB [db]> insert into project values (235, 1, 3, 20120120);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`db`.`project`, CONSTRAINT `project_ibfk_2` FOREIGN KEY (`c_id`) REFERENCES `clients` (`c_id`))
MariaDB [db]>

