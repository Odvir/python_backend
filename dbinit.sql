/* This should already be done (Ofir end) */ 

CREATE DATABASE IF NOT EXISTS wifi_crowdsourcing; 

/* Sets the wifi_crowdsourcing datbase as the current databse. */
USE wifi_crowdsourcing;

/* Creates SQL users named jasmine and ofir in the wifi_crowdsourcing databse, with CREATE privileges 
on the database (allows them to create tables in the database). */ 
-- CREATE USER IF NOT EXISTS jasmine; 
-- GRANT CREATE ON DATABASE wifi_crowdsourcing TO jasmine; 

-- CREATE USER IF NOT EXISTS ofir; 
-- GRANT CREATE ON DATABASE wifi_crowdsourcing TO ofir; 

/* Creates a schema for seaparate users and gives permission to the other user . */
-- DROP SCHEMA IF EXISTS jasmine_schema CASCADE;
-- CREATE SCHEMA jasmine_schema AUTHORIZATION jasmine;
-- GRANT USAGE ON SCHEMA jasmine_schema TO ofir;

-- DROP SCHEMA IF EXISTS ofir_schema CASCADE;
-- CREATE SCHEMA ofir_schema AUTHORIZATION ofir;
-- GRANT USAGE ON SCHEMA ofir_schema TO jasmine;

/* NOTE: TIMESTAMP stores by default in UTC, need to create a column in PST. */
CREATE TABLE wifi_data (
    latitude FLOAT, 
    longitude FLOAT, 
    floor_id INT, 
    building_id INT, 
    date_time TIMESTAMP, 
    wifi_name STRING, 
    download_speed FLOAT, 
    upload_speed FLOAT, 
    outage BOOL
); 

/* Converts from UTC to PST. */
-- SELECT (<yourtime> at time zone 'UTC') AT TIME ZONE 'Pacific Standard Time';
-- SELECT TIMEZONE('PST', date_time) FROM jasmine_schema.wifi_crowdsourcing;

SELECT date_time AT TIME ZONE 'UTC' AT TIME ZONE 'Pacific Standard Time' AS
       LocalTime
FROM wifi_data; 