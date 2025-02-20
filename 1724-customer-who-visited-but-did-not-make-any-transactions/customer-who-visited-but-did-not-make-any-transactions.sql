/* Write your T-SQL query statement below */
select v.customer_id, count(v.visit_id) as count_no_trans from visits v 
LEFT JOIN transactions t ON v.visit_id = t.visit_id where t.transaction_id is null
GROUP BY(v.customer_id);