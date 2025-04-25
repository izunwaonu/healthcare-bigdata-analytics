import pandas as pd
import json

# Load CSVs
patients = pd.read_csv('data/raw/Patient_records.csv')
diseases = pd.read_csv('data/raw/disease.csv')
groups = pd.read_csv('data/raw/group.csv')
subgroups = pd.read_csv('data/raw/subgroup.csv')
subscribers = pd.read_csv('data/raw/subscriber.csv')  # make sure this is renamed from .cs

# Load Excel
hospitals = pd.read_excel('data/raw/hospital.xlsx')

# Load JSON
with open('data/raw/claims.json') as f:
    claims_data = json.load(f)
claims = pd.json_normalize(claims_data)  # flatten nested JSON

# Preview
print("Patients:\n", patients.head(), "\n")
print("Diseases:\n", diseases.head(), "\n")
print("Claims:\n", claims.head(), "\n")
print("Hospitals:\n", hospitals.head(), "\n")
