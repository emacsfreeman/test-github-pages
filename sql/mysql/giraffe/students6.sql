DROP TABLE student;

CREATE TABLE student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    major VARCHAR(20)
);

SELECT * FROM student;

UPDATE student
SET major = 'Biochemistry'
WHERE major = 'Biology' OR major = 'Chemistry';

UPDATE student
SET major = 'Socio'
WHERE major = 'Sociology';

UPDATE student
SET major = 'CS'
WHERE major = 'Computer Science';

INSERT INTO student(name, major) VALUES('Jack', 'Biology');

INSERT INTO student(name, major) VALUES('Kate', 'Sociology');

INSERT INTO student(name, major) VALUES('Claire', 'Chemistry');

INSERT INTO student(name, major) VALUES('Mike', 'Computer Science');

INSERT INTO student(name, major) VALUES('Mike', 'Computer Science');

DELETE FROM student
WHERE student_id = 5;
