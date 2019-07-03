SELECT con.continent, floor(avg(c.population))
FROM city c INNER JOIN country con
ON c.countrycode = con.code
GROUP BY con.continent;