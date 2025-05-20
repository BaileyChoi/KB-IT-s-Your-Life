USE sqldb;

SELECT *
FROM buytbl
INNER JOIN usertbl
	ON buytbl.userID = usertbl.userID;
    
SELECT *
FROM buytbl
INNER JOIN usertbl
	ON buytbl.userID = usertbl.userID
WHERE buytbl.userID = 'JYP';

SELECT U.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
	LEFT OUTER JOIN buytbl B
		ON U.userID = B.userID
ORDER BY U.userID;    

CREATE TABLE stdtbl (
	stdName VARCHAR(10) NOT NULL PRIMARY KEY,
    addr CHAR(4) NOT NULL
);

CREATE TABLE clubtbl (
	clubName VARCHAR(10) NOT NULL PRIMARY KEY,
	roomNo CHAR(4) NOT NULL
);

CREATE TABLE stdclubtbl (
	num int AUTO_INCREMENT NOT NULL PRIMARY KEY,
	stdName VARCHAR(10) NOT NULL,
	clubName VARCHAR(10) NOT NULL,
	FOREIGN KEY(stdName) REFERENCES stdtbl(stdName),
	FOREIGN KEY(clubName) REFERENCES clubtbl(clubName)
);

SELECT S.stdName, S.addr, SC.clubName, C.roomNO
FROM stdtbl S
	INNER JOIN stdclubtbl SC
		ON S.stdName = SC.stdName
	INNER JOIN clubtbl C
		ON SC.clubName = C.clubName
ORDER BY S.stdName;

SELECT C.clubName, C.roomNo, S.stdName, S.addr
FROM stdtbl S
	INNER JOIN stdclubtbl SC
		ON SC.stdName = S.stdName
	INNER JOIN clubtbl C
		ON SC.clubName = C.clubName
ORDER BY C.clubName;

USE employees;
SELECT COUNT(*) AS '데이터개수'
FROM employees
	CROSS JOIN titles;

USE sqldb;
CREATE TABLE emptbl(emp CHAR(3), manager CHAR(3), empTel VARCHAR(8));
INSERT INTO empTbl VALUES('나사장', NULL, '0000');
INSERT INTO empTbl VALUES('김재무', '나사장', '2222');
INSERT INTO empTbl VALUES('김부장', '김재무', '2222-1');
INSERT INTO empTbl VALUES('이부장', '김재무', '2222-2');
INSERT INTO empTbl VALUES('우대리', '이부장', '2222-2-1');
INSERT INTO empTbl VALUES('지사원', '이부장', '2222-2-2');
INSERT INTO empTbl VALUES('이영업', '나사장', '1111');
INSERT INTO emptbl VALUES('한과장', '이영업', '1111-1');
INSERT INTO empTbl VALUES('최정보', '나사장', '5355');
INSERT INTO empTbl VALUES('윤차장', '최정보','3355-1');
INSERT INTO empTbl VALUES('이주임', '윤자장', '5335-1-1');
SELECT * FROM empTbl;

SELECT A.emp AS '부하직원', B.emp AS '직속상관', B.empTel AS '직속상관연락처'
FROM empTbl A
	INNER JOIN empTbl B
		ON A.manager = B.emp
WHERE A.emp = '우대리';

USE sqldb;
SELECT stdName, addr 
FROM stdtbl
	UNION ALL
	SELECT clubName, roomNo 
    FROM clubtbl;

SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' 
FROM usertbl
WHERE name NOT IN (
	SELECT name 
    FROM usertbl 
    WHERE mobile1 IS NULL
);

SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' 
FROM usertbl
WHERE name IN (
	SELECT name 
    FROM usertbl 
    WHERE mobile1 IS NULL
);

USE employees;
SELECT E.emp_no, E.first_name, E.last_name, T.title
FROM employees E
	INNER JOIN titles T
		ON E.emp_no = T.emp_no
WHERE T.to_date = '9999-01-01';

SELECT E.*, T.title, S.salary
FROM employees E
	JOIN titles T
		ON E.emp_no = T.emp_no
	INNER JOIN salaries S
		ON E.emp_no = S.emp_no
WHERE T.to_date = '9999-01-01' AND S.to_date = '9999-01-01';

SELECT E.emp_no, E.first_name, E.last_name, D.dept_name
FROM employees E
	INNER JOIN dept_emp DE
		ON E.emp_no = DE.emp_no
	INNER JOIN departments D
		ON DE.dept_no = D.dept_no
WHERE DE.to_date = '9999-01-01'
ORDER BY E.emp_no;

SELECT D.dept_no, D.dept_name, Count(*)
FROM departments D
	JOIN dept_emp DE using(dept_no)
WHERE DE.to_date = '9999-01-01'
GROUP BY dept_no
ORDER BY dept_no;

SELECT E.emp_no, E.first_name, E.last_name, D.dept_name, DE.from_date, DE.to_date
FROM employees E
	JOIN dept_emp DE
		ON E.emp_no = DE.emp_no
	JOIN departments D 
		ON DE.dept_no = D.dept_no
WHERE E.emp_no = 10209;

CREATE TABLE sellings (
	car_id INT,
    employee_id INT PRIMARY KEY,
    created_at DATETIME,
    price INT
);
INSERT INTO `sqldb`.`sellings` (`car_id`, `employee_id`, `created_at`, `price`) VALUES ('352', '2455', '2016-08-16 02:52:10', '3700');
INSERT INTO `sqldb`.`sellings` (`car_id`, `employee_id`, `created_at`, `price`) VALUES ('352', '2499', '2016-11-26 01:33:15', '6200');
INSERT INTO `sqldb`.`sellings` (`car_id`, `employee_id`, `created_at`, `price`) VALUES ('352', '3010', '2016-11-06 11:35:44', '10800');
INSERT INTO `sqldb`.`sellings` (`car_id`, `employee_id`, `created_at`, `price`) VALUES ('306', '2955', '2016-12-25 06:55:46', '1000');
SELECT * FROM sellings;

USE sqldb;
SELECT SUM(price) AS 판매액
FROM sellings
WHERE created_at like '2016-11%';