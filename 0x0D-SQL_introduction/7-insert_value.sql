-- 7-insert_value.sql
INSERT INTO first_table (id, name)
SELECT 89, 'Best School' FROM DUAL
WHERE NOT EXISTS (
    SELECT 1 FROM first_table WHERE id = 89
) LIMIT 1;
