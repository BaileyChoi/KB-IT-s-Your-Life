DROP DATABASE if exists tabledb;
CREATE DATABASE tabledb;
USE tabledb;

DROP TABLE IF EXISTS usertbl;
CREATE TABLE usertbl(
	userID		CHAR(8) NOT NULL PRIMARY KEY,
    name		VARCHAR(10) NOT NULL,
    birth_year 	INT NOT NULL,
    addr		CHAR(2) NOT NULL,
    mobile1		CHAR(3) NULL,
    mobile2		CHAR(8) NULL,
    height		SMALLINT NULL,
    m_date		DATE NULL
);

ALTER TABLE usertbl
CHANGE user_id userID CHAR(8);

DROP TABLE IF EXISTS buytbl;
CREATE TABLE buytbl(
	num 		INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    userid 		CHAR(8) NOT NULL,
    prod_name 	CHAR(6) NOT NULL,
    group_name 	CHAR(4) NULL,
    price 		INT NOT NULL,
    amount 		SMALLINT NOT NULL,
    FOREIGN KEY(userid) REFERENCES usertbl(userID)
);

INSERT INTO usertbl
VALUES
('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8'),
('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4'),
('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
SELECT * FROM usertbl;

INSERT INTO buytbl VALUES(NULL, 'KBS', '운동화', NULL, 30, 2);
INSERT INTO buytbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
-- INSERT INTO buytbl VALUES(NULL, 'JYP', '모니터', '전자', 200, 1); 
SELECT * FROM buytbl;

DROP TABLE IF EXISTS usertbl2;
CREATE TABLE usertbl2 (
	userID 		CHAR(8) NOT NULL,
    name 		VARCHAR(10) NOT NULL,
    birth_year 	INT NOT NULL,
    CONSTRAINT PRIMARY KEY PK_userTBL_userID(userID)
);

DROP TABLE IF EXISTS prodtbl;
CREATE TABLE prodTbl (
	prodCode 	CHAR(3) NOT NULL,
	prodID 		CHAR(4) NOT NULL,
	prodDate 	DATETIME NOT NULL,
	prodCur 	CHAR(10) NULL,
CONSTRAINT PK_prodtbl_proCode_prodID
		   PRIMARY KEY (prodCode, prodID)
);
SHOW INDEX FROM prodTbl;

-- 인덱스 정렬
SELECT * FROM employees.employees
WHERE employees.last_name = 'Facello';
SELECT * FROM employees.employees
WHERE employees.emp_no = '32138';

ALTER TABLE buyTBL
	ADD CONSTRAINT FK_userTBL_buyTBL
    FOREIGN KEY(userID)
    REFERENCES userTBL(userID);
    -- ON DELETE CASCADE;

ALTER TABLE userTBL 
ADD COLUMN email CHAR(30) NULL UNIQUE;

ALTER TABLE userTBL
ADD CONSTRAINT CK_birth CHECK (birth_year >= 1900 AND birth_year <= 2023),
ADD CONSTRAINT CK_name CHECK (name IS NOT NULL);

ALTER TABLE userTBL
CHANGE COLUMN birth_year birth_year INT NOT NULL DEFAULT -1 ,
CHANGE COLUMN addr addr CHAR(2) NOT NULL DEFAULT '서울' ,
CHANGE COLUMN height height SMALLINT NULL DEFAULT 170 ;

ALTER TABLE `tabledb`.`usertbl` 
CHANGE COLUMN `birth_year` `birth_year` INT NOT NULL DEFAULT 2000 ;

INSERT INTO usertbl VALUES ('LHL', '이혜리', default, default,'011', '1234567', default, '2023-12-12', NULL);
INSERT INTO usertbl(userID, name) VALUES('KAY', '김아영');
INSERT INTO usertbl VALUES ('WB', '원빈', 1982, '대전', '019', '9876543', 176, '2020-05-05', NULL);
SELECT * FROM usertbl;

ALTER TABLE usertbl
ADD homepage VARCHAR(30) -- 열 추가
DEFAULT 'http://www.hanbit.co.kr' -- 디폴트 값
NULL; -- NULL 허용함

ALTER TABLE usertbl
DROP COLUMN email;

ALTER TABLE usertbl
CHANGE COLUMN name u_name VARCHAR(20) NULL;

SHOW CREATE TABLE buyTBL;


