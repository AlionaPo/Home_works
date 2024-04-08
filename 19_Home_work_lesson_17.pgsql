CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name varchar(50) NOT NULL,
    age INTEGER
);

INSERT INTO  students (id, name, age) 
VALUES 
    (2, 'Eddy', 21),
    (3, 'Lily', 22),
    (4, 'Jenny', 19),
    (1, 'Bae', 22) 


CREATE TABLE subjects(
    id INTEGER PRIMARY KEY,
    name varchar(50) NOT NULL
);

INSERT INTO subjects (id, name) 
VALUES (1, 'English'), (2, 'Matth') , (3, 'Spanish'), (4, 'Ukrainian')


CREATE TABLE student_subjects(
    id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students (id),
    FOREIGN KEY (subject_id)
        REFERENCES subjects (id)
    );

INSERT INTO student_subjects (id, student_id, subject_id)
VALUES (1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 1, 3)



SELECT * FROM students;
SELECT * FROM subjects;
SELECT * FROM student_subjects;
