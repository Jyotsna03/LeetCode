/* Write your T-SQL query statement below */
SELECT DISTINCT num AS ConsecutiveNums
FROM Logs l
WHERE 
    (SELECT COUNT(*) FROM Logs WHERE Logs.num = l.num AND Logs.id BETWEEN l.id AND l.id + 2) = 3;
