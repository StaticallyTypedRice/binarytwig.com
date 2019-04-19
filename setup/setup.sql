-- Use these queries to set up the database for MySQL or MariaDB

CREATE DATABASE binarytwig CHARACTER SET UTF8;
CREATE USER binarytwig@localhost IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON binarytwig.* TO binarytwig@localhost;
FLUSH PRIVILEGES
