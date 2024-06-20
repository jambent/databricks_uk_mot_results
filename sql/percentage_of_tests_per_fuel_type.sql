WITH fuel_type_count AS (
    SELECT fuel_type, COUNT(*) AS count
    FROM personaldatabricks.uk_mot_results.test_result
    WHERE fuel_type IN ('PE','DI','HY','EL')
    GROUP BY fuel_type
)
SELECT
CASE WHEN fuel_type_count.fuel_type = 'PE' THEN 'Petrol'
    WHEN fuel_type_count.fuel_type = 'DI' THEN 'Diesel' 
    WHEN fuel_type_count.fuel_type = 'HY' THEN 'Hydrogen' 
    WHEN fuel_type_count.fuel_type = 'EL' THEN 'Electric'
END as fuel_type,
CASE
    WHEN fuel_type_count.fuel_type IN ('PE','DI','HY','EL') THEN
        ROUND(CAST(fuel_type_count.count AS DECIMAL(12,2))
            /(SELECT COUNT(*) FROM personaldatabricks.uk_mot_results.test_result) * 100,2)
END as percentage_of_all_cars_tested
FROM fuel_type_count
ORDER BY percentage_of_all_cars_tested DESC
;