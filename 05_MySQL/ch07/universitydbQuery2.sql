USE universitydb;
-- GROUP BY / HAVING
-- [문제1] 화학과를 제외하고 학과별로 학생들의 평점 평균을 검색하시오
-- 평균을 소수이하 2째 자리에서 반올림
-- 테이블 : STUDENT
SELECT major, ROUND(AVG(avr), 2)
FROM student
GROUP BY major
HAVING major != '화학';
-- [문제2] 화학과를 제외한 각 학과별 평균 평점 중에 평점이 2.0 미만인 정보를 검색하시오 
-- 테이블 : STUDENT
SELECT major, ROUND(AVG(avr), 2)
FROM student
GROUP BY major
HAVING major != '화학' AND ROUND(AVG(avr), 2) < 2.0;

-- JOIN
-- [문제1] 송강 교수가 강의하는 과목을 검색하시오.
-- 테이블 : PROFESSOR P, COURSE C
-- 컬럼 : PNO, PNAME, CNO, CNAME
SELECT P.pno, P.pname, C.cno, C.cname
FROM professor P
	JOIN course C USING(pno)
WHERE P.pname = '송강';
-- [문제2] 화학 관련 과목을 강의하는 교수의 명단을 검색하시오 
-- 테이블 : PROFESSOR P, COURSE C
-- 컬럼 : PNO, PNAME, CNO, CNAME
SELECT P.pno, P.pname, C.cno, C.cname
FROM professor P
	JOIN course C USING(pno)
WHERE C.cname LIKE '%화학%';
-- [문제3] 화학과 1학년 학생의 기말고사 성적을 검색하시오
-- 테이블: STUDENT ST, SCORE SC, COURSE CO
-- 컬럼: SNO, SNAME, MAJOR, SYEAR, CNO, CNAME, RESULT
SELECT sno, sname, major, syear, cno, cname, result
FROM student
	JOIN score USING(sno)
    JOIN course USING(cno)
WHERE major = '화학' AND syear = 1;
-- [문제4] 화학과 1학년 학생의 일반화학 기말고사 점수를 검색하시오
-- 테이블: STUDENT ST, SCORE SC, COURSE CO
-- 컬럼: SNO, SNAME, MAJOR, SYEAR, CNO, CNAME, RESULT
SELECT sno, sname, major, syear, cno, cname, result
FROM student
	JOIN score USING(sno)
    JOIN course USING(cno)
WHERE major = '화학' AND syear = 1 AND cname = '일반화학';
-- [문제5] 학생 중에 동명이인을 검색하여 이름으로 오름차순하고, 만약 같은 이름은 번호로 오름차순하시오 (SELF JOIN)
-- 테이블 : STUDENT
-- 컬럼 : SNO, SNAME
SELECT A.sno, A.sname
FROM student A
JOIN student B 
	ON (A.sno != B.sno AND A.sname = B.sname)
ORDER BY A.sname, A.sno;


