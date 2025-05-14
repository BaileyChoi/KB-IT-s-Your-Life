-- USE 구문
USE employees;

-- SELECT와 FROM
SELECT * FROM titles;
SELECT first_name FROM employees;
SELECT first_name, last_name, gender	-- 이름과 성별 열을 가져옴
FROM employees;

-- 조회
SHOW DATABASES;
SHOW TABLES;
DESCRIBE employees;

-- 열 이름의 별칭
SELECT first_name AS 이름, gender AS 성별, hire_date '회사 입사일'
FROM employees;

-- 기본적인 WHERE절
USE sqldb;
SELECT * FROM usertbl
WHERE name = '김경호';

-- 다른 DB TABLE 검색
SELECT * FROM employees.employees
WHERE first_name = 'Georgi';

-- 관계 연산자의 사용
SELECT userid, name FROM usertbl
WHERE birthyear >= 1970 AND height >= 182;

-- BETWEEN... AND와 IN() 그리고 LIKE
SELECT name, height FROM usertbl
WHERE height BETWEEN 180 AND 183;
SELECT name, addr FROM usertbl
WHERE addr IN ('경남', '전남', '경북');
SELECT name, height FROM usertbl
WHERE name LIKE '김%';

-- 서브 쿼리
SELECT name, height FROM usertbl 
WHERE height > (SELECT height FROM usertbl WHERE name='김경호');

-- ANY
SELECT name, height FROM usertbl
WHERE height >= ANY(SELECT height FROM usertbl WHERE addr = '경남');
SELECT name, height FROM usertbl
WHERE height = ANY(SELECT height FROM usertbl WHERE addr = '경남');
SELECT name, height FROM usertbl
WHERE height IN (SELECT height FROM usertbl WHERE addr = '경남');

-- ALL
SELECT name, height FROM usertbl
WHERE height > ALL (SELECT height FROM usertbl WHERE addr = '경남');

-- ORDER BY절
SELECT name, mDate FROM usertbl ORDER BY mDate ASC;
SELECT name, mDate FROM usertbl ORDER BY mDate DESC;
SELECT name, height FROM usertbl ORDER BY height DESC, name ASC;

-- DISTINCT
SELECT DISTINCT addr FROM usertbl;

-- LIMIT
USE employees;
SELECT emp_no, hire_date FROM employees
ORDER BY hire_date ASC
LIMIT 5; 
SELECT emp_no, hire_date FROM employees
ORDER BY hire_date ASC
LIMIT 0, 5; 

-- CREATE TABLE...SELECT
CREATE TABLE buytbl2 (SELECT * FROM buytbl);
SELECT * FROM buytbl2;
CREATE TABLE buytbl3 (SELECT userID AS uID, prodName 'pName' FROM buytbl);
SELECT * FROM buytbl3;

-- GROUP BY절
-- SELECT userID, amount FROM buytbl;
SELECT userID, SUM(amount) FROM buytbl GROUP BY userID;
SELECT userID AS '사용자 아이디', SUM(amount) AS '총 구매 개수'
FROM buytbl
GROUP BY userID;
SELECT userID AS '사용자 아이디', SUM(amount * price) AS '총 구매액'
FROM buytbl
GROUP BY userID;

-- 집계 함수
SELECT AVG(amount) AS '평균 구매 개수' 
FROM buytbl;
SELECT userID, AVG(amount) AS '평균 구매 개수'
FROM buytbl
GROUP BY userID;
SELECT name, MAX(height), MIN(height)
FROM usertbl
GROUP BY name;
SELECT name, height
FROM usertbl
WHERE height = (SELECT MAX(height) FROM usertbl)
OR height = (SELECT MIN(height) FROM usertbl);
SELECT COUNT(*) FROM usertbl;
SELECT COUNT(mobile1) AS '휴대폰이 있는 사용자'
FROM usertbl;

-- HAVING절
SELECT userID AS '사용자 아이디', SUM(amount * price) AS '총 구매액'
FROM buytbl
GROUP BY userID
HAVING SUM(price * amount) > 1000;

-- ROLLUP
SELECT num, groupName, SUM(price * amount) AS '비용'
FROM buytbl
GROUP BY groupName, num
WITH ROLLUP;
SELECT groupName, SUM(price * amount) AS '비용'
FROM buytbl
GROUP BY groupName
WITH ROLLUP;

-- INSERT 데이터 삽입
USE sqldb;
CREATE TABLE testTbl1(id INT, username CHAR(3), age INT);
INSERT INTO testTbl1 VALUES(1, '홍길동', 25);
INSERT INTO testTbl1(id, username)  VALUES(2, '설현');
INSERT INTO testTbl1(username, age, id)  VALUES('하나', 26, 3);

USE sqldb;
CREATE TABLE testTbl2(
	id INT AUTO_INCREMENT PRIMARY KEY,
	userName CHAR(3),
    age INT
);
INSERT INTO testTbl2 VALUES (NULL, '지인', 25);
INSERT INTO testTbl2 VALUES (NULL, '유나', 22);
INSERT INTO testTbl2 VALUES (NULL, '유경', 21);
SELECT * FROM testTbl2;

USE sqldb;
CREATE TABLE testTbl4(id INT, Fname VARCHAR(50), Lname VARCHAR(50));
INSERT INTO testTbl4
SELECT emp_no, first_name, last_name
FROM employees.employees;
SELECT * FROM testTbl4;

-- UPDATE 데이터 수정
UPDATE testTbl4
SET Lname = '없음'
WHERE Fname = 'Kyoichi';
UPDATE buytbl
SET price = price * 1.5;

-- DELETE FROM
DELETE FROM testtbl4
WHERE Fname = 'Aamer';
DELETE FROM testtbl4
WHERE Fname = 'Aamer'
LIMIT 5;

-- 기본 문제
USE world;
SELECT Population 
FROM city
WHERE CountryCode = 'KOR'
ORDER BY Population DESC;

SELECT CountryCode, Population
FROM city
ORDER BY CountryCode, Population DESC;

SELECT Count(*)
FROM city
WHERE CountryCode = 'KOR';

SELECT *
FROM city
WHERE CountryCode in ('KOR', 'CHN', 'JPN');

SELECT * 
FROM city
WHERE CountryCode = 'KOR' AND Population >= 1000000;

SELECT *
FROM city
WHERE CountryCode = 'KOR'
ORDER BY Population DESC
LIMIT 10;

SELECT *
FROM city
WHERE CountryCode = 'KOR' AND Population BETWEEN 1000000 AND 5000000;

-- 심화 문제
USE world;

SELECT MIN(Population) AS 최소값
FROM city
WHERE CountryCode = 'KOR';

SELECT AVG(Population)
FROM city
WHERE CountryCode = 'KOR';

SELECT MAX(Population) AS 최대값
FROM city
WHERE CountryCode = 'KOR';

SELECT CHAR_LENGTH(Name) 
FROM country;

SELECT CONCAT(UPPER(LEFT(Name, 3)), SUBSTRING(Name, 4))
FROM country;

SELECT ROUND(LifeExpectancy, 1)
FROM country;

USE employees;

SELECT * 
FROM dept_manager
WHERE to_date = '9999-01-01';

SELECT *
FROM dept_manager
WHERE dept_no = 'd005' AND to_date = '9999-01-01';

SELECT *
FROM employees
ORDER BY hire_date DESC
LIMIT 20 OFFSET 140;

SELECT COUNT(DISTINCT emp_no)
FROM dept_emp
WHERE to_date = '9999-01-01';

SELECT AVG(salary)
FROM salaries
WHERE to_date = '9999-01-01';

SELECT *
FROM salaries
WHERE to_date = '9999-01-01' 
	AND salary >=
	(SELECT AVG(salary)
	FROM salaries
	WHERE to_date = '9999-01-01');
    
SELECT dept_no, COUNT(emp_no)
FROM dept_emp
GROUP BY dept_no
ORDER BY dept_no;
