# Write your MySQL query statement below

Select 'Low Salary' as category, 
sum(income < 20000)as accounts_count from Accounts 
union 
Select 'Average Salary' as category,
sum(income>= 20000 and income<=50000) as accounts_count from Accounts
union
Select 'High Salary' as category, 
sum(income>50000) as accounts_count from Accounts;