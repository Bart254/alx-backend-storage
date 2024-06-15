-- Lists all bands with glam rock as their main style, ranked by longevity
-- creates a function to calculate band's lifespan/longevity upto 2022
DELIMITER $$
CREATE FUNCTION calc_lifespan(formed YEAR, split YEAR)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE span INT;
    IF formed IS NULL THEN SET span = 0;
    ELSEIF split IS NULL THEN SET span = 2022 - formed;
    ELSE SET span = split - formed;
    END IF; 
    RETURN span;
END$$
DELIMITER ;

-- Query the database
SELECT band_name, calc_lifespan(formed, split) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', style)
ORDER BY lifespan DESC;
