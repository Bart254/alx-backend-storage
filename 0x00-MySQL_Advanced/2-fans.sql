-- Script ranks country bands based on fans
-- We group by origin to use SUM function
CREATE INDEX origin_fan_idx ON metal_bands(origin, fans);

SELECT origin, SUM(fans) as nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
