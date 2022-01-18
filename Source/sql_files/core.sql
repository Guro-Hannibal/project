DROP DATABASE IF EXISTS friendship;
CREATE DATABASE friendship;

USE friendship;

CREATE TABLE events (
	event_id INT UNSIGNED NOT NULL,
	artefact_id INT UNSIGNED NOT NULL,
	channel_id	INT UNSIGNED NOT NULL,
	customer_id INT UNSIGNED NOT NULL,
	event_sequence_id INT UNSIGNED NOT NULL,
	location_id	INT UNSIGNED NOT NULL,
	platform_id INT UNSIGNED NOT NULL,
	service_code INT UNSIGNED NOT NULL,
	staff_id INT UNSIGNED NOT NULL,
	event_amount INT UNSIGNED NOT NULL,
	event_date_time DATETIME NOT NULL,
	booking_date_from DATETIME NOT NULL,
	booking_date_to DATETIME NOT NULL,
	other_details VARCHAR(255)
);

CREATE TABLE suppliers_services_join(
	service_code INT UNSIGNED NOT NULL PRIMARY KEY,
	supplier_id INT UNSIGNED NOT NULL,
	service_name VARCHAR(30),
	supplier_name VARCHAR(30)
);

CREATE TABLE event_sequences(
	event_sequence_id INT UNSIGNED NOT NULL PRIMARY KEY,
	next_event_sequence_id INT UNSIGNED NOT NULL,
	event_code SMALLINT,
	event_time DATETIME,
	event_details TINYTEXT,
	event_source_file TEXT,
	event_source_variables VARCHAR(60)
);

CREATE TABLE channels(
	channel_id INT UNSIGNED NOT NULL PRIMARY KEY,
	channel_name VARCHAR(30),
	channel_details TINYTEXT
);

CREATE TABLE staff(
	staff_id INT UNSIGNED NOT NULL PRIMARY KEY,
	staff_name VARCHAR(30),
	staff_details TINYTEXT
);

CREATE TABLE artefacts(
	artefact_id INT UNSIGNED NOT NULL PRIMARY KEY,
	artefact_name VARCHAR(40),
	artefact_details TINYTEXT
);

# secondary source table

CREATE TABLE locations (
	location_id INT UNSIGNED  NOT NULL PRIMARY KEY,
	location_name VARCHAR(15),
	location_details TINYTEXT
);

CREATE TABLE platforms(
	platform_id INT UNSIGNED NOT NULL PRIMARY KEY,
	platform_name VARCHAR(10),
	platform_details TINYTEXT,
	acces_variables VARCHAR(10)
);

CREATE TABLE apps (
	app_code INT UNSIGNED NOT NULL UNIQUE PRIMARY KEY,
	event_id INT UNSIGNED,
	app_source_vars TINYTEXT,
	app_dialog TINYTEXT,
	data_clone LONGTEXT
);

CREATE TABLE info_types(
	info_type_code CHAR(4) NOT NULL PRIMARY KEY,
	info_type_description VARCHAR(100),
	info_type_priority_id INT UNSIGNED UNIQUE
);

CREATE TABLE info(
	info_id INT UNSIGNED NOT NULL UNIQUE PRIMARY KEY,
	event_id INT UNSIGNED NOT NULL,
	info_type_code CHAR(4) NOT NULL,
	info_timeline TINYTEXT,
	info_loc_history TINYTEXT,
	info_details VARCHAR(100)
);

CREATE TABLE customers (
	customer_id INT UNSIGNED NOT NULL PRIMARY KEY,
	customer_name VARCHAR(100) NOT NULL,
	title CHAR(15),
	gender CHAR(10),
	customers_details VARCHAR(100)
);

CREATE TABLE customers_data_platforms (
	platform_id INT UNSIGNED NOT NULL PRIMARY KEY,
	customer_name VARCHAR(100) NOT NULL,
	platform_details VARCHAR(100)
);


CREATE TABLE suppliers (
	supplier_id INT UNSIGNED NOT NULL PRIMARY KEY,
	supplier_name VARCHAR(100) NOT NULL,
	supplier_details VARCHAR(100)
);

CREATE TABLE services (
	service_code INT UNSIGNED NOT NULL PRIMARY KEY,
	service_name VARCHAR(14),
	supplier_name VARCHAR(15)
);

	


-- 	FOREIGN KEY (platform_id) REFERENCES platforms(platform_id) ON UPDATE CASCADE,


-- );
-- -- 
-- ALTER TABLE customers (

-- );

ALTER TABLE events ADD (
	FOREIGN KEY (event_id) REFERENCES staff(staff_id) ON UPDATE CASCADE,
	FOREIGN KEY (event_id) REFERENCES channels(channel_id) ON UPDATE CASCADE,
	FOREIGN KEY (event_id) REFERENCES customers(customer_id) ON UPDATE CASCADE,
	FOREIGN KEY (event_id) REFERENCES artefacts(artefact_id) ON UPDATE CASCADE,
	FOREIGN KEY (event_id) REFERENCES platforms(platform_id) ON UPDATE CASCADE,
	FOREIGN KEY (event_id) REFERENCES locations(location_id) ON UPDATE CASCADE,
	FOREIGN KEY (event_id) REFERENCES suppliers_services_join(service_code) ON UPDATE CASCADE,
	FOREIGN KEY (event_id) REFERENCES event_sequences(event_sequence_id) ON UPDATE CASCADE,
	FOREIGN KEY (event_id) REFERENCES event_sequences(event_sequence_id) ON UPDATE CASCADE
);

-- ALTER TABLE customers ADD (
-- 	FOREIGN KEY (customer_name) REFERENCES customers_and_platforms PRIMARY KEY
-- );


ALTER TABLE event_sequences ADD (
	FOREIGN KEY (next_event_sequence_id) REFERENCES event_sequences(event_sequence_id) ON UPDATE CASCADE
);

ALTER TABLE suppliers_services_join ADD (
	FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON UPDATE CASCADE
);

ALTER TABLE suppliers_services_join ADD (
	FOREIGN KEY (service_code) REFERENCES services(service_code) ON UPDATE CASCADE
);

ALTER TABLE apps ADD (
	FOREIGN KEY (event_id) REFERENCES events(event_id) ON UPDATE CASCADE
);

ALTER TABLE info ADD (
	FOREIGN KEY (info_id) REFERENCES events(event_id) ON UPDATE CASCADE,
	FOREIGN KEY (info_type_code) REFERENCES info_types(info_type_code) ON UPDATE CASCADE
);

