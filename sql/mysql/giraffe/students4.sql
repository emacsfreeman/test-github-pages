DROP TABLE student;

CREATE TABLE student (
    student_id INT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) DEFAULT 'undecided'
);

SELECT * FROM student;

DESCRIBE student;


ALTER TABLE student ADD gpa DECIMAL;

ALTER TABLE student DROP gpa;


INSERT INTO student(student_id, major) VALUES(1, 'Jack');

INSERT INTO student VALUES(2, 'Kate', 'Sociology');

INSERT INTO student(student_id, name) VALUES(3, NULL);

INSERT INTO student VALUES(4, 'Jack', 'Biology');

INSERT INTO student VALUES(5, 'Mike', 'Computer Science');

