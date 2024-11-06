USE `ry-vue`;
DROP TABLE IF EXISTS city_travel;

CREATE TABLE city_travel(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    title VARCHAR(255),
    content VARCHAR(255),
    city VARCHAR(255) UNIQUE,
    province VARCHAR(255),
    src VARCHAR(255),
    img VARCHAR(255)
);

DROP TABLE IF EXISTS city_food;

CREATE TABLE city_food(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE,
    summary VARCHAR(1024),
    province VARCHAR(255),
    src VARCHAR(255),
    img VARCHAR(255)
);