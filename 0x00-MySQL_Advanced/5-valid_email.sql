DELIMITER $$
CREATE TRIGGER validate_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        IF OLD.valid_email = 1 THEN SET NEW.valid_email = 0;
        ELSE SET NEW.valid_email = 1;
        END IF;
    END IF;
END$$
DELIMITER ;
