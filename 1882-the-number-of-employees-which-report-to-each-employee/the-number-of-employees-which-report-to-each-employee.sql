# Write your MySQL query statement below


select employee_id,name, reports_count, average_age
from employees, (
    select reports_to,count(reports_to) as reports_count, 
    round(avg(age),0) as average_age from employees
    where reports_to is not null
    group by reports_to
) as ans
where employee_id=ans.reports_to
order by employee_id;