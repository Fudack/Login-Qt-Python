CREATE DATABASE fulladmin;

USE fulladmin;

CREATE TABLE usuarios(
rut INT(10)
correo VARCHAR(100)
nombre VARCHAR(20),
apPat VARCHAR(20),
apMat VARCHAR(20),
contrasena VARCHAR(20))

SELECT * FROM usuarios;

ALTER TABLE usuarios MODIFY contrasena VARCHAR(64);

ALTER TABLE usuarios ADD root BOOLEAN;

ALTER TABLE usuarios MODIFY rut INT(10) NOT NULL PRIMARY KEY;

ALTER TABLE usuarios MODIFY correo VARCHAR(100) NOT NULL;

ALTER TABLE usuarios MODIFY contrasena VARCHAR(64) NOT NULL;

