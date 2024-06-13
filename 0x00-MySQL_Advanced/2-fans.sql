-- Script ranks country bands based on fans
-- We group by origin to use SUM function
SELECT origin, SUM(fans) as nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
