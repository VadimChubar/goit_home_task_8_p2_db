PRAGMA foreign_keys = off;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS disciplines;
CREATE TABLE disciplines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name STRING UNIQUE NOT NULL,
    teacher_id REFERENCES teachers(id)
);
DROP TABLE IF EXISTS [groups];
CREATE TABLE [groups] (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name STRING UNIQUE
);
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id REFERENCES students (id),
    discipline_id REFERENCES disciplines (id),
    date_of DATE NOT NULL,
    grade INTEGER NOT NULL
);
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname STRING UNIQUE NOT NULL,
    group_id REFERENCES [groups] (id)
);
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname STRING UNIQUE NOT NULL
);
COMMIT TRANSACTION;
PRAGMA foreign_keys = on;