SELECT COUNT(DISTINCT(user_id))
FROM restaurants_reviews;

SELECT *
FROM restaurt_project.public.misc_categories;

DO $$
DECLARE
    col_name TEXT;
    tabl_name TEXT := 'misc_categories'; -- Replace 'your_table_name' with the actual name of your table
    count_query TEXT;
    null_counts INT;
BEGIN
    FOR col_name IN
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = 'public.' || tabl_name
    LOOP
        count_query := format('SELECT COUNT(*) FROM %I WHERE %I IS NULL', tabl_name, col_name);
        EXECUTE count_query INTO null_counts;
        RAISE NOTICE 'Column % has % NULL values', col_name, null_counts;
    END LOOP;
END $$;