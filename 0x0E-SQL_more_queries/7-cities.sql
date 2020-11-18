-- The database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL,
	state_id INT NOT NULL,
	UNIQUE (id),
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
