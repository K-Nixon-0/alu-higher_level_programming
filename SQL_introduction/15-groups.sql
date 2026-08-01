-- lists number of records per score, ordered by count desc
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
