
DELIMITER $$
CREATE TRIGGER artefacts.trigger
AFTER INSERT ON artefacts
FOR EACH ROW 
	BEGIN 
		IF NEW.artefacts IS NOT NULL 
			SET events.artefact_id = NEW.artefact_id;
		END IF;
	END;$$
DELIMITER ;
