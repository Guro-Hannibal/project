DROP TRIGGER IF EXISTS service_trigger;

DELIMITER $$
CREATE TRIGGER suppliers_trigger 
AFTER INSERT
ON suppliers
FOR EACH ROW
	BEGIN
		INSERT
	INTO
	services
VALUES (NEW.supplier_id);
	END$$
DELIMITER ;

