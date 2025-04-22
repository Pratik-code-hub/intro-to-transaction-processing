CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

SHOW TABLES;
SELECT * FROM users;

DESCRIBE users;
ALTER TABLE users
ADD COLUMN password VARCHAR(255) NOT NULL;

DESCRIBE users;

ALTER TABLE users
ADD COLUMN role ENUM('admin', 'user', 'guest') NOT NULL;
DESCRIBE users;
SHOW TABLES;
SELECT * FROM users;

