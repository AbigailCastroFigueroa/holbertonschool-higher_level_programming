-- Give the average of all records in a table of the database
SELECT * FROM second_table WHERE average > ( SELECT AVG(score) FROM second_table);

