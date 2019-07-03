/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT * 
FROM (
    SELECT CITY C, LENGTH(CITY) L
    FROM STATION
    ORDER BY L DESC, C)
WHERE ROWNUM =  1;

SELECT * 
FROM (
    SELECT CITY as C, LENGTH(CITY) as L
    FROM STATION
    ORDER BY L, C)
WHERE ROWNUM = 1;



