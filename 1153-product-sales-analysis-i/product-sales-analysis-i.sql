/* Write your T-SQL query statement below */
SELECT p.product_name, s.year, s.price 
from sales s JOIN product p on s.product_id = p.product_id;