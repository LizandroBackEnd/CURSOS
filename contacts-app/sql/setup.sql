-- Active: 1700514994314@@127.0.0.1@3306@contacts_app
CREATE DATABASE contacts_app;

USE contacts_app;

CREATE TABLE contacts(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    phone_number VARCHAR(255)
 );

INSERT INTO contacts(name, phone_number) VALUES("Pedro", "7224730020"); 