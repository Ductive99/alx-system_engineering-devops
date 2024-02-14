-- Creates a user
-- Responsible for checking the configuration of the servers

CREATE USER IF NOT EXISTS 'holberton_user'@'localhost'
IDENTIFIED BY 'projectcorrection280hbtn';

GRANT REPLICATION CLIENT, SELECT ON *.* TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;
