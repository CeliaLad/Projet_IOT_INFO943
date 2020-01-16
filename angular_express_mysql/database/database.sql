CREATE DATABASE ng_games_db;

USE ng_games_db;

CREATE TABLE game (
    id INT(1) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(180),
    description VARCHAR(255),
    image VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DESCRIBE game;
