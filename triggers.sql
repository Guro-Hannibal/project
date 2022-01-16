DROP TRIGGER IF EXISTS services_trigger;

DELIMITER $$
CREATE TRIGGER services_trigger 
AFTER INSERT
ON services
FOR EACH ROW
	BEGIN
		INSERT INTO suppliers_services_join (service_code, supplier_id, service_name, suppliers_name)
		VALUES (service_code, supplier_id, service_name, suppliers_name);
	END
	$$
DELIMITER ;

