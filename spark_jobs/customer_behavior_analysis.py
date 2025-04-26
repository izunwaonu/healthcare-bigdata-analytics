# PySpark script to analyze average claim amount per hospital
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Start Spark session
spark = SparkSession.builder \
    .appName("Healthcare Claim Analysis") \
    .getOrCreate()

# Load cleaned claims data
claims_df = spark.read.csv("../data/processed/claims_clean.csv", header=True, inferSchema=True)

# Load cleaned patient data
patients_df = spark.read.csv("../data/processed/patients_clean.csv", header=True, inferSchema=True)

# Join claims with patients on patient ID
merged_df = claims_df.join(patients_df, claims_df.patient_id == patients_df.Patient_id, "inner")

# Group by hospital_id and calculate average claim_amount
avg_claims = merged_df.groupBy("hospital_id").agg(avg("claim_amount").alias("average_claim_amount"))

# Show results
avg_claims.show(10)

# Stop Spark session
spark.stop()
