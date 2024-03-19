CREATE DATABASE universidad;

CREATE TABLE courses(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    capacity INT,
    creation_date DATE
)

INSERT INTO courses(name, capacity, creation_date)
VALUES ("Math", 150, "2022-10-10"),
       ("Physics", 50, "2021-09-17"),
       ("PE", 233, "2019-10-10"),
       ("English Studies", 120, "2019-10-09"),
       ("Social Studies", 200, "2018-05-20"),
       ("History", 222, "2022-06-16");

