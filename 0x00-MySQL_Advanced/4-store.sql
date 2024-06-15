-- Creates a trigger
-- Items number is reduced every time an order is made
DELIMITER $$
CREATE TRIGGER decrease_quant
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$
DELIMITER;
