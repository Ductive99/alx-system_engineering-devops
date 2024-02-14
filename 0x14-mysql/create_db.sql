-- Create a MySQL DataBase
-- And, creates a table in the DB.

CREATE DATABASE IF NOT EXISTS tyrell_corp;

CREATE TABLE IF NOT EXISTS tyrell_corp.nexus6
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
);

INSERT INTO `tyrell_corp.nexus6` (`name`) VALUES ("El Houssain");

