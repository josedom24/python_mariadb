# python_mariadb

Ejemplo de aplicación python3 para el acceso a una base de dato MariaDB.

Tenemos construida una base de datos `testdb` con una tabla `Alumnos`, con la siguiente definición:

```
MariaDB [testdb]> desc Alumnos;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| id        | int(11)      | NO   | PRI | NULL    |       |
| nombre    | varchar(255) | NO   |     | NULL    |       |
| apellidos | varchar(255) | YES  |     | NULL    |       |
| edad      | int(11)      | YES  |     | 0       |       |
+-----------+--------------+------+-----+---------+-------+
```

Además tenemos un usuario llamado `usuario` con contraseña `asdasd` que tiene todos los privilegios sobre la tabla `Alumnos`.
Puedes crear la base de datos y el usuario con el fichero `esquema.sql` que encuentras en el repositorio:

```
mysql -u root -p < esquema.sql
```

Puedes encontrar un artículo que explica el uso de Python para gestionar una base de datos MariaDB en [Gestión de base de datos mysql/mariadb con python3](https://www.josedomingo.org/pledin/2021/12/python3-mysql/).

Como nos enseña el artículo es necesario instalar la librería `mysqlclient`, para ello:

```
apt install python3-mysqldb
```