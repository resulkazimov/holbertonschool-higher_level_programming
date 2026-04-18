-- Lists the number of records with the same score in the table second_table
-- SQL query to group records by score and count them
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
