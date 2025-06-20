SELECT *
FROM travel9;

DROP TABLE IF EXISTS tbl_travel;
CREATE TABLE tbl_travel
(
    no          INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    district    VARCHAR(50)        NOT NULL,
    title       VARCHAR(512)       NOT NULL,
    description TEXT,
    address     VARCHAR(512),
    phone       VARCHAR(256)
);

SELECT *
FROM tbl_travel;

DROP TABLE IF EXISTS tbl_travel_image;
CREATE TABLE tbl_travel_image
(
    no        INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    filename  VARCHAR(512)       NOT NULL,
    travel_no INT,
    CONSTRAINT FOREIGN KEY (travel_no) REFERENCES tbl_travel (no)
        ON DELETE CASCADE
);

SELECT *
FROM tbl_travel_image;

SELECT t.*, ti.no as tino, ti.filename, ti.travel_no
FROM tbl_travel t
    LEFT OUTER JOIN tbl_travel_image ti
        ON t.no = ti.travel_no
WHERE t.no = 1;