USE sqldb;

SELECT CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 개수' FROM buytbl;
SELECT CONVERT(AVG(amount), SIgned INTEGER) AS '평균 구매 개수' FROM buytbl;

SELECT IF (100>200, '참', '거짓');

SELECT CASE 10
	WHEN 1 THEN '일'
    WHEN 5 THEN '오'
	WHEN 10 THEN '십'
	END AS 'CASE연습';
    
SELECT ASCII('A'), CHAR(65);

SELECT CONCAT_WS('/', '2025', '01', '01');

SELECT u.userID, u.name, GROUP_CONCAT(b.prodName SEPARATOR ',') AS '상품목록'
FROM usertbl u
	LEFT OUTER JOIN buytbl b
    ON u.userID = b.userID
GROUP BY u.userID, u.name
ORDER BY u.userID;

SELECT INSERT('abcdefghi', 3, 4, '@@@@'), INSERT('abcdefghi', 3, 2, '@@@@');

SELECT LEFT('abcdefghi', 3), RIGHT('abcdefghi', 3);

SELECT TRIM(' 이것이 '), TRIM(BOTH 'ᄏ' FROM 'ᄏᄏᄏ재밌어요.ᄏᄏᄏᄏ');

SELECT REPLACE('이것이 MySQL이다', '이것이', 'This is');

SELECT SUBSTRING('대한민국만세', 3, 2);	



    