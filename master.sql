DROP DATABASE IF EXISTS logical_data_model;
CREATE DATABASE logical_data_model;

USE logical_data_model;

-- source table

CREATE TABLE customers_data_platforms (
	platform_id CHAR(20),
	customer_name VARCHAR(255),
	plarform_details VARCHAR(255)
);

-- source table

CREATE TABLE customers (
	customer_id BIGINT UNSIGNED UNIQUE PRIMARY KEY,
	customer_name VARCHAR(255),
	title CHAR(20),
	gender CHAR(3),
	customers_details VARCHAR(255)
);

-- source table

CREATE TABLE suppliers (
	supplier_id BIGINT UNSIGNED UNIQUE,
	supplier_name VARCHAR(255),
	supplier_details VARCHAR(255)
);

-- source table

CREATE TABLE products_and_services(
	pr_sr_code CHAR(20),
	suppliers_id BIGINT UNSIGNED,
	pr_sr_name VARCHAR(255),
	pr_sr_details VARCHAR(255)
);

-- source table

CREATE TABLE channels(
	channel_id BIGINT UNSIGNED UNIQUE PRIMARY KEY,
	channel_name VARCHAR(255),
	channel_details VARCHAR(255)
);

-- source table

CREATE TABLE staff(
	staff_id BIGINT UNSIGNED UNIQUE PRIMARY KEY,
	staff_name VARCHAR(255),
	staff_details VARCHAR(255)
);

-- secondary source table

CREATE TABLE services(
	service_code CHAR(20),
	service_name VARCHAR(255),
	other_details VARCHAR(255)
);

-- secondary source table

CREATE TABLE artefacts(
	artefact_id BIGINT UNSIGNED UNIQUE PRIMARY KEY,
	artefact_name VARCHAR(255),
	artefact_details VARCHAR(255)
);

-- secondary source table

CREATE TABLE locations (
	location_id BIGINT UNSIGNED PRIMARY KEY,
	location_name VARCHAR(255),
	location_details VARCHAR(255)
);

-- secondary source table

CREATE TABLE platforms(
	platform_id CHAR(15),
	platform_name VARCHAR(255),
	platform_details VARCHAR(255),
	acces_variables VARCHAR(255)
);

-- secondary source table

CREATE TABLE event_sequences(
	event_sequence_id BIGINT UNSIGNED UNIQUE,
	next_event_sequence_id BIGINT UNSIGNED UNIQUE,
	event_code CHAR(20),
	event_time DATETIME,
	event_details VARCHAR(255),
	event_source_file TEXT,
	event_source_variables VARCHAR(255)
);

-- result table

CREATE TABLE events (
	event_id SERIAL PRIMARY KEY,
	artefact_id BIGINT UNSIGNED,
	channel_id	BIGINT UNSIGNED,
	customer_id BIGINT UNSIGNED,
	event_sequence_id BIGINT UNSIGNED,
	location_id	BIGINT UNSIGNED,
	platform_code VARCHAR(20),
	service_code VARCHAR(20),
	staff_id BIGINT UNSIGNED,
	event_amount BIGINT,
	event_date_time DATETIME,
	booking_date_from DATETIME,
	booking_date_to DATETIME,
	other_details VARCHAR(255)
);

-- manual analazing data

CREATE TABLE mess_and_data_app (
	app_code BIGINT UNSIGNED UNIQUE PRIMARY KEY,
	app_backup_vars JSON,
	app_source_vars JSON,
	app_security_vars JSON,
	app_dialog JSON,
	data_clone LONGTEXT
);

-- information variables

CREATE TABLE info_types(
	info_type_code CHAR(15),
	info_type_description VARCHAR(255),
	info_type_priority_id INT UNSIGNED UNIQUE
);

-- auto analasing data

CREATE TABLE info(
	info_id BIGINT UNSIGNED UNIQUE PRIMARY KEY,
	event_id BIGINT,
	priority_code INT UNSIGNED,
	info_timeline JSON,
	info_loc_history JSON,
	info_details VARCHAR(255)
);

