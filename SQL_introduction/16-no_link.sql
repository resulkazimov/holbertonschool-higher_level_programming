-- Lists all records of the table second_table with a name value
-- SQL query to list score and name, filtering out empty names, ordered by score
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
