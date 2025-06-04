USE world2;
-- -----------------------------------------
-- 	SQL문제 1번
-- -----------------------------------------
-- 1-1
SELECT * FROM city;

-- 1-2
SELECT Language, Percentage
FROM countrylanguage
WHERE CountryCode LIKE "CHE";

-- 1-3
INSERT INTO city VALUES(NULL, 'Cairo', 'EGY', 'Cario Governorate', 9500000);

-- 1-4
UPDATE city
SET Name = 'GoodSite'
WHERE CountryCode = 'PNG';

-- 1-5
SELECT *
FROM country
ORDER BY Name DESC;

-- -----------------------------------------
-- 	SQL문제 2번
-- -----------------------------------------
-- 2-1
SELECT UPPER(Name)
FROM city;

-- 2-2
SELECT CONCAT(ID, '-', CountryCode)
FROM city;

-- 2-3
SELECT LENGTH(District)
FROM city;

-- 2-4
SELECT AVG(Population)
FROM city;

-- 2-5
SELECT Continent, MAX(GNP)
FROM country
GROUP BY Continent
ORDER BY MAX(GNP) ASC;

-- -----------------------------------------
-- 	SQL문제 3번
-- -----------------------------------------
-- 3-1
SELECT Ci.Name 'cityName', Co.Name 'countryName'
FROM city Ci
	JOIN country Co
    ON Ci.CountryCode = Co.Code;

-- 3-2
SELECT C.Name, Cl.Language
FROM country C
	LEFT OUTER JOIN countrylanguage Cl
    ON C.Code = Cl.CountryCode;

-- 3-3
SELECT Name
FROM city
WHERE Population = (
	SELECT MAX(Population)
    FROM city);