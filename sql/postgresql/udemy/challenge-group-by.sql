SELECT COUNT(amount), SUM(amount) 
FROM payment
GROUP BY staff_id;
