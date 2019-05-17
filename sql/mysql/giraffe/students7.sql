DROP TABLE student;

CREATE TABLE student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    major VARCHAR(20)
);


INSERT INTO student(name, major) VALUES('Pam', 'Biology');

INSERT INTO student(name, major) VALUES('Jack', 'Biology');

INSERT INTO student(name, major) VALUES('Kate', 'Sociology');

INSERT INTO student(name, major) VALUES('Clara', 'Sociology');

INSERT INTO student(name, major) VALUES('Claire', 'Chemistry');

INSERT INTO student(name, major) VALUES('Clark', 'Chemistry');

INSERT INTO student(name, major) VALUES('Mike', 'Computer Science');

INSERT INTO student(name, major) VALUES('Michelle', 'Computer Science');

INSERT INTO student(name, major) VALUES('Paul', 'Linguistics');

INSERT INTO student(name, major) VALUES('Pauline', 'Linguistics');

INSERT INTO student(name, major) VALUES('Stephan', 'Mathematics');

INSERT INTO student(name, major) VALUES('Molly', 'Mathematics');

INSERT INTO student(name, major) VALUES('Francis', 'Philosophy');

INSERT INTO student(name, major) VALUES('Ella', 'Philosophy');

INSERT INTO student(name, major) VALUES('Janet', 'Economics');

INSERT INTO student(name, major) VALUES('Jean', 'Economics');

INSERT INTO student(name, major) VALUES('Julia', 'Logic');

INSERT INTO student(name, major) VALUES('Julius', 'Logic');

SELECT * FROM student;

/* sélctionne uniquement la colonne des noms */
SELECT name
FROM student;


UPDATE student
SET major = 'Bioche'
WHERE major = 'Biology' OR major = 'Chemistry';

UPDATE student
SET major = 'Socio'
WHERE major = 'Sociology';

UPDATE student
SET major = 'CS'
WHERE major = 'Computer Science';

UPDATE student
SET major = 'Maths'
WHERE major = 'Mathematics';

UPDATE student
SET major = 'Philo'
WHERE major = 'Philosophy';

UPDATE student
SET major = 'Eco'
WHERE major = 'Economics';


/* sélctionne uniquement les colonnes des noms et majors */
SELECT name, major
FROM student
LIMIT 15;


/* 
    sélctionne uniquement les colonnes des noms et majors 
    en classant par ordre alphabétique selon les noms
*/
SELECT name, major
FROM student
ORDER BY name;

/* 
    sélctionne uniquement les colonnes des noms et majors 
    en classant par ordre alphabétique selon les majors
    dans l'ordre décroissant
*/
SELECT name, major
FROM student
ORDER BY major DESC;


/* 
    sélctionne uniquement les colonnes des noms et majors 
    en classant par ordre alphabétique selon les majors
    puis par ID si meme major
*/
SELECT *
FROM student
ORDER BY major, student_id;


/* 
    sélctionne uniquement les colonnes des noms et majors 
    en classant par ordre alphabétique selon les majors, par
    ordre décroissant, puis par nom, par ordre croissant, 
    si meme major
*/
SELECT *
FROM student
ORDER BY major DESC, name;



/* 
    sélctionne uniquement les colonnes des noms et majors 
    en classant par ordre alphabétique selon les majors, par
    ordre croissant, puis par nom, par ordre décroissant, 
    si meme major avec une limite de 5 résultats
*/
SELECT *
FROM student
ORDER BY major, name DESC
LIMIT 5;

/* 
    sélctionne uniquement les colonnes des noms et majors 
    en classant par ordre alphabétique selon les majors, par
    ordre décroissant, puis par nom, par ordre croissant, 
    si meme major avec une limite de 5 résultats
*/
SELECT *
FROM student
ORDER BY major DESC, name ASC
LIMIT 5;



SELECT *
FROM student 
WHERE major = 'Bioche' OR name = 'Paul';

-- sélectionne tous les étudiants qui ne font pas Bioche
SELECT *
FROM student 
WHERE major <> 'Bioche';


-- sélectionne tous les étudiants qui ne font pas Bioche
-- ET dont l'identifiant est supérieur à 9
SELECT *
FROM student 
WHERE major <> 'Bioche' AND student_id > 9;


-- sélectionne tous les étudiants dont le nom est sur la liste
SELECT *
FROM student 
WHERE name IN ('Claire', 'Kate', 'Mike');


-- sélectionne tous les étudiants dont le nom est sur la liste
-- ET dont l'identifiant est inférieur à 7
SELECT *
FROM student 
WHERE name IN ('Claire', 'Kate', 'Mike') AND student_id < 7;
