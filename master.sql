DROP DATABASE IF EXISTS logical_data_model;
CREATE DATABASE logical_data_model;

USE logical_data_model;

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

CREATE TABLE customers_data_platforms (
	platform_id CHAR(20),
	customer_name VARCHAR(255),
	plarform_details VARCHAR(255)
);

CREATE TABLE customers (
	customer_id BIGINT UNSIGNED UNIQUE PRIMARY KEY,
	customer_name VARCHAR(255),
	title CHAR(20),
	gender CHAR(3),
	customers_details VARCHAR(255)
);

CREATE TABLE suppliers (
	supplier_id BIGINT UNSIGNED UNIQUE PRIMARY KEY,
	supplier_name VARCHAR(255),
	supplier_details VARCHAR(255)
);

CREATE TABLE products_and_services(
	pr_sr_code CHAR(20),
	suppliers_id BIGINT UNSIGNED,
	pr_sr_name VARCHAR(255),
	pr_sr_details VARCHAR(255)
);

CREATE TABLE channels(
	channel_id BIGINT UNIQUE UNSIGNED PRIMARY KEY,
	channel_name VARCHAR(255),
	channel_details VARCHAR(255)
);


