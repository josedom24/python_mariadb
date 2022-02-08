CREATE DATABASE testdb;
CREATE USER 'usuario'@'%' IDENTIFIED BY 'asdasd';
GRANT ALL PRIVILEGES ON testdb.* to 'usuario'@'%';
FLUSH PRIVILEGES;
USE testdb;

CREATE TABLE Alumnos (
id int,
nombre varchar(255) not null,
apellidos varchar(255),
edad int default 0,
primary key (id)
);
