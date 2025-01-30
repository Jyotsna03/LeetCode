/* Write your T-SQL query statement below */
select emp.name from Employee emp where 
(select COUNT(managerId) from Employee where emp.id = managerID ) >= 5 ;