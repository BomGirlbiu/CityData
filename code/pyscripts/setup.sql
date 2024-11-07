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

DROP TABLE IF EXISTS newyork_counts;
CREATE TABLE newyork_counts(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    city VARCHAR(255),
    start_date DATE,
    end_date DATE,
    insert_date DATE,
    count INT
)

DROP TABLE IF EXISTS bilibili_comments;
CREATE TABLE bilibili_comments(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    city VARCHAR(255),
    bv VARCHAR(255),
    username VARCHAR(255),
    content VARCHAR(2048),
    level VARCHAR(16),
    nice_count INT,
    reply_time DATETIME,
    insert_time DATETIME
)

DROP TABLE IF EXISTS city_images;
CREATE TABLE city_images(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    city VARCHAR(255),
    province VARCHAR(255),
    imagesURL VARCHAR(255) UNIQUE
)

DROP TABLE IF EXISTS emotion_bili;
CREATE TABLE emotion_bili(
    cityName VARCHAR(255),
    positiveNum INT,
    negativeNum INT,
    neutralNum INT,
    platform VARCHAR(255)
)

DROP TABLE IF EXISTS city_news;
CREATE TABLE city_news(
    newsID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    city VARCHAR(255),
    province VARCHAR(255),
    title VARCHAR(255),
    newsURL VARCHAR(1024) ,
    imgURL VARCHAR(512) UNIQUE
)

DROP TABLE IF EXISTS google_search;
CREATE TABLE google_search(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    city VARCHAR(255),
    date varchar(255),
    count INT,
    -- city 和 date 作为联合主键
    UNIQUE KEY `city_date` (`city`, `date`)
)

DROP TABLE IF EXISTS youtube_search;
CREATE TABLE youtube_search(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    city VARCHAR(255),
    date varchar(255),
    count INT,
    -- city 和 date 作为联合主键
    UNIQUE KEY `city_date` (`city`, `date`)
)