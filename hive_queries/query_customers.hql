-- HiveQL Script to summarize claims by hospital
CREATE DATABASE IF NOT EXISTS healthcare_db;

USE healthcare_db;

-- Create a table for claims
CREATE EXTERNAL TABLE IF NOT EXISTS claims (
    claim_id STRING,
    patient_id STRING,
    disease_name STRING,
    SUB_ID STRING,
    Claim_Or_Rejected STRING,
    claim_type STRING,
    claim_amount FLOAT,
    claim_date STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/claims/';

-- Create a table for patients
CREATE EXTERNAL TABLE IF NOT EXISTS patients (
    Patient_id STRING,
    Patient_name STRING,
    patient_gender STRING,
    patient_birth_date STRING,
    patient_phone STRING,
    disease_name STRING,
    city STRING,
    hospital_id STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/patients/';

-- Query to find average claim amount per hospital
SELECT p.hospital_id, AVG(c.claim_amount) AS avg_claim_amount
FROM claims c
JOIN patients p ON (c.patient_id = p.Patient_id)
GROUP BY p.hospital_id
ORDER BY avg_claim_amount DESC
LIMIT 10;
