SELECT 
(Salary * Months) as earnings , count(*) 
FROM Employee 
GROUP BY earnings 
ORDER BY earnings desc 
LIMIT 1;