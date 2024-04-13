use sy1_student_;
Create table emp(
id int primary key auto_increment,
ename varchar(100) not null,
email varchar(100),
phone bigint not null,
salary int not null,
city varchar(100) not null
);

insert into emp(ename, email, phone, salary, city) values ("rahul", "rahul@gmail.com", 897568978, 35000, "miraj"),
("akash", "akash@gmail.com", 8955978985, 25000, "sangli"),
("sonu", "sonu@gmail.com", 8478965897, 45000, "kavlapur"),
("nidhi", "nidhi@gmail.com", 9751458789, 50000, "bisur"),
("tejas", "tejas@gmail.com", 5456445978, 55000, "bisur");

select * from emp;

Drop table emp;

select id,ename, count(ename) from emp where salary >30000 group by city ;



MariaDB [db]> insert into emp(id, ename, email, phone,salary,  city) values (null,"leyona", "leyona@gmail.com",880935000, 50000, "miraj");
ERROR 1048 (23000): Column 'id' cannot be null
MariaDB [db]> 



