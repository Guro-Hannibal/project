DROP TRIGGER IF EXISTS services_trigger;

DELIMITER $$
CREATE TRIGGER services_trigger 
BEFORE INSERT
ON services
FOR EACH ROW
	BEGIN
		INSERT INTO suppliers_services_join(service_code, service_name, supplier_name) 
		SELECT service_code, service_name, supplier_name  FROM service ;
	END
	$$
DELIMITER ;
