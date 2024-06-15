-- Creates a procedure
-- procedure handles bonus scores
DELIMITER $$
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    DECLARE proj_id INT;
    IF project_name IN (SELECT name FROM projects) THEN
    SET proj_id = (SELECT id FROM projects WHERE name = project_name);
    ELSE 
    BEGIN
        INSERT INTO projects(name) VALUES (project_name);
        SET proj_id = LAST_INSERT_ID();
    END;
    END IF;
    INSERT INTO corrections(user_id, project_id, score)
    VALUES (user_id, proj_id, score);
END$$
DELIMITER ;
