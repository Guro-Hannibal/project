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

create table customers_data_platforms (
	platform_id CHAR(20),
	customer_name VARCHAR(255),
	plarform_details VARCHAR(255)
);

create table customers (
	customer_id SERIAL PRIMARY KEY,
	customer_name VARCHAR(255),
	title CHAR(20),
	gender CHAR(3),
	important_details VARCHAR(255)
);

