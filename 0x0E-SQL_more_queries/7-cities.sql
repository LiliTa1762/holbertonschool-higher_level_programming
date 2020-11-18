-- the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY(id),
state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(state_id),
name VARCHAR(256) NOT NULL);
