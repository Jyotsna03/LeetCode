/* Write your T-SQL query statement below */
WITH CTE AS (
    SELECT employee_id, department_id,
    RANK() OVER(PARTITION BY employee_id ORDER BY primary_flag DESC) as r FROM Employee
)
SELECT employee_id, department_id FROM CTE 
WHERE r = 1