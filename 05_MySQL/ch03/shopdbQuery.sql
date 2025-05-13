USE shopdb;

SELECT * FROM member_tbl;
SELECT * FROM product_tbl;

INSERT INTO member_tbl (`MEMBER_ID`, `MEMBER_NAME`, `MEMBER_ADDRESS`) VALUES ('NaoTa', '나오타', '주소불명');
DELETE FROM member_tbl WHERE (`MEMBER_ID` = 'NaoTa');

SELECT * FROM product_tbl;
SELECT MEMBER_NAME, MEMBER_ADDRESS FROM member_tbl;
SELECT * FROM member_tbl WHERE MEMBER_NAME = '지운이';
