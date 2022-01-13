DROP DATABASE IF EXISTS logical_data_model;
CREATE DATABASE logical_data_model;

USE logical_data_model;


CREATE TABLE customers_data_platforms (
	platform_id CHAR(20) NOT NULL PRIMARY KEY,
	customer_name VARCHAR(255),
	plarform_details VARCHAR(255)
);

CREATE TABLE customers (
	customer_id BIGINT UNSIGNED NOT NULL UNIQUE PRIMARY KEY,
	customer_name VARCHAR(255),
	title CHAR(20),
	gender CHAR(3),
	customers_details VARCHAR(255),
	FOREIGN KEY (customer_name) REFERENCES customers_data_platforms(platform_id) ON UPDATE CASCADE
);

CREATE TABLE suppliers (
	supplier_id BIGINT UNSIGNED NOT NULL UNIQUE PRIMARY KEY,
	supplier_name VARCHAR(255),
	supplier_details VARCHAR(255)
);

CREATE TABLE services(
	service_code CHAR(20) NOT NULL UNIQUE PRIMARY KEY,
	service_name VARCHAR(255),
	services_details VARCHAR(255)
);

CREATE TABLE products_and_services(
	service_code CHAR(20),
	supplier_id BIGINT UNSIGNED NOT NULL,
	pr_sr_name VARCHAR(255),
	pr_sr_details VARCHAR(255),
	FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON UPDATE CASCADE,
	FOREIGN KEY (service_code) REFERENCES services(service_code) ON UPDATE CASCADE
);

CREATE TABLE channels(
	channel_id BIGINT UNSIGNED NOT NULL UNIQUE PRIMARY KEY,
	channel_name VARCHAR(255),
	channel_details VARCHAR(255)
);


CREATE TABLE staff(
	staff_id BIGINT UNSIGNED NOT NULL UNIQUE PRIMARY KEY,
	staff_name VARCHAR(255),
	staff_details VARCHAR(255)
);

CREATE TABLE artefacts(
	artefact_id BIGINT UNSIGNED NOT NULL UNIQUE PRIMARY KEY,
	artefact_name VARCHAR(255),
	artefact_details VARCHAR(255)
);

# secondary source table

CREATE TABLE locations (
	location_id BIGINT UNSIGNED NOT NULL UNIQUE PRIMARY KEY,
	location_name VARCHAR(255),
	location_details VARCHAR(255)
);

CREATE TABLE platforms(
	platform_id CHAR(20) NOT NULL PRIMARY KEY,
	platform_name VARCHAR(255),
	platform_details VARCHAR(255),
	acces_variables VARCHAR(255)
);

CREATE TABLE event_sequences(
	event_sequence_id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
	next_event_sequence_id BIGINT UNSIGNED,
	event_code CHAR(20),
	event_time DATETIME,
	event_details VARCHAR(255),
	event_source_file TEXT,
	event_source_variables VARCHAR(255)
);

CREATE TABLE events (
	event_id BIGINT UNSIGNED NOT NULL,
	artefact_id BIGINT UNSIGNED NOT NULL,
	channel_id	BIGINT UNSIGNED NOT NULL,
	customer_id BIGINT UNSIGNED NOT NULL,
	event_sequence_id BIGINT UNSIGNED NOT NULL,
	location_id	BIGINT UNSIGNED NOT NULL,
	platform_id VARCHAR(20) NOT NULL,
	service_code VARCHAR(20) NOT NULL,
	staff_id BIGINT UNSIGNED NOT NULL,
	event_amount BIGINT UNSIGNED NOT NULL,
	event_date_time DATETIME,
	booking_date_from DATETIME,
	booking_date_to DATETIME,
	other_details VARCHAR(255),
	FOREIGN KEY (location_id) REFERENCES locations(location_id) ON UPDATE CASCADE,
	FOREIGN KEY (event_id) REFERENCES event_sequences(event_sequence_id) ON UPDATE CASCADE,
	FOREIGN KEY (artefact_id) REFERENCES artefacts(artefact_id) ON UPDATE CASCADE,
	FOREIGN KEY (service_code) REFERENCES products_and_services(service_code) ON UPDATE CASCADE,
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON UPDATE CASCADE,
	FOREIGN KEY (platform_id) REFERENCES platforms(platform_id) ON UPDATE CASCADE,
	FOREIGN KEY (channel_id) REFERENCES channels(channel_id) ON UPDATE CASCADE,
	FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON UPDATE CASCADE
);

CREATE TABLE apps (
	app_code BIGINT UNSIGNED NOT NULL UNIQUE PRIMARY KEY,
	event_id BIGINT UNSIGNED,
	app_source_vars JSON,
	app_dialog JSON,
	data_clone LONGTEXT,
	FOREIGN KEY (event_id) REFERENCES events(event_id) ON UPDATE CASCADE
);

CREATE TABLE info_types(
	info_type_code CHAR(15) NOT NULL PRIMARY KEY,
	info_type_description VARCHAR(255),
	info_type_priority_id INT UNSIGNED UNIQUE
);

CREATE TABLE info(
	info_id BIGINT UNSIGNED NOT NULL UNIQUE PRIMARY KEY,
	event_id BIGINT UNSIGNED NOT NULL,
	info_type_code CHAR(15) NOT NULL,
	info_timeline JSON,
	info_loc_history JSON,
	info_details VARCHAR(255),
	FOREIGN KEY (event_id) REFERENCES events(event_id) ON UPDATE CASCADE,
	FOREIGN KEY (info_type_code) REFERENCES info_types(info_type_code) ON UPDATE CASCADE
);

-- INSERT INTO logical_data_model.customers_data_platforms
-- (platform_id, customer_name, plarform_details)
-- VALUES('123', '123', '123') ON UPDATE CASCADE;
-- 
-- 
