-- Creates a replica user

CREATE USER IF NOT EXISTS 'replica_user'@'%'
IDENTIFIED BY 'project280holberton';

GRANT REPLICATION CLIENT, SELECT ON *.* TO 'replica_user'@'%';

FLUSH PRIVILEGES;
