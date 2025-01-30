/* Write your T-SQL query statement below */
select emp1.unique_id , emp.name from Employees emp LEFT JOIN EmployeeUNI emp1 ON emp.id = emp1.id