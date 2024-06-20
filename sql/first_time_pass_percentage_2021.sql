WITH first_time_pass_count AS (
    SELECT make, COUNT(*) as count
    from personaldatabricks.uk_mot_results.test_result
    WHERE test_class_id = 4
    AND test_result = 'P'
    AND make in ('FORD', 'BMW', 'CITROEN', 'TOYOTA','VOLKSWAGEN',
    'VOLVO', 'HYUNDAI','MERCEDES-BENZ', 'KIA','SKODA','AUDI')
    GROUP BY make
),
all_tests_count AS (
    SELECT make, COUNT(*) as count
    from personaldatabricks.uk_mot_results.test_result
    WHERE test_class_id = 4
    AND make in ('FORD', 'BMW', 'CITROEN', 'TOYOTA','VOLKSWAGEN',
    'VOLVO', 'HYUNDAI','MERCEDES-BENZ', 'KIA','SKODA','AUDI')
    GROUP BY make
)
SELECT first_time_pass_count.make, 
ROUND(CAST(first_time_pass_count.count AS DECIMAL(11,2))/CAST(all_tests_count.count AS DECIMAL(11,2)),4) * 100 as first_time_pass_percentage
FROM first_time_pass_count
RIGHT OUTER JOIN
all_tests_count
ON first_time_pass_count.make = all_tests_count.make
ORDER BY first_time_pass_percentage DESC;