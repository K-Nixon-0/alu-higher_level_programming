-- lists score and name, excluding rows without a name, ordered by score desc
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
