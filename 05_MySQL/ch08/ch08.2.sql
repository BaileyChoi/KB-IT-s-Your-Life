USE sqldb;

CREATE VIEW v_usertbl
AS
SELECT userid, name, addr FROM usertbl;
SELECT * FROM v_usertbl;

CREATE VIEW v_userbuytbl
AS
SELECT U.userid, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
	INNER JOIN buytbl B
			ON U.userID = B.userID;
SELECT * FROM v_userbuytbl;
SELECT * FROM v_userbuytbl WHERE name = '김범수';

SHOW VARIABLES LIKE 'innodb_data_file_path';

SHOW VARIABLES LIKE 'innodb_file_per_table';

CREATE TABLESPACE ts_a ADD DATAFILE 'ts_a.ibd';
CREATE TABLESPACE ts_b ADD DATAFILE 'ts_b.ibd';
CREATE TABLESPACE ts_c ADD DATAFILE 'ts_c.ibd';

USE employees;
CREATE VIEW employees_info AS
    SELECT emp_no, birth_date, first_name, last_name, gender, hire_date,
		title, t.from_date AS t_from, t.to_date AS t_to,
        salary, s.from_date AS s_from, s.to_date AS s_to
    FROM employees
		JOIN titles t USING(emp_no)
		JOIN salaries s USING(emp_no);
SELECT * FROM employees_info;
DROP VIEW IF EXISTS emp_dept_info;

CREATE VIEW emp_dept_info AS
SELECT emp_no, dept_emp.dept_no, dept_name, from_date, to_date
FROM dept_emp
	JOIN departments 
    ON dept_emp.dept_no = departments.dept_no;
SELECT * FROM emp_dept_info
ORDER BY emp_no;

SELECT * FROM emp_dept_info
WHERE to_date = '9999-01-01'
ORDER BY emp_no;








