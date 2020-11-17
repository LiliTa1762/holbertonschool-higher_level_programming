-- Creates the database hbtn_0d_usa and the table states in that database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENTED, name VARCHAR(256) NOT NULL);
