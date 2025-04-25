import pandas as pd
import json
import os

# Create output directory if it doesn't exist
os.makedirs('data/processed/', exist_ok=True)

# 1. Load the raw data
patients = pd.read_csv('data/raw/Patient_records.csv')
diseases = pd.read_csv('data/raw/disease.csv')
groups = pd.read_csv('data/raw/group.csv')
subgroups = pd.read_csv('data/raw/subgroup.csv')
subscribers = pd.read_csv('data/raw/subscriber.csv')  # make sure the file extension is correct
hospitals = pd.read_excel('data/raw/hospital.xlsx')

with open('data/raw/claims.json') as f:
    claims_data = json.load(f)
claims = pd.json_normalize(claims_data)

# 2. Clean: Drop duplicates, handle missing values (basic cleaning for now)
def basic_clean(df, name):
    print(f"\n--- Cleaning {name} ---")
    print("Before cleaning:", df.shape)
    df = df.drop_duplicates()
    df = df.dropna(how='all')  # Drop rows where all elements are NaN
    print("After cleaning:", df.shape)
    return df

patients = basic_clean(patients, "patients")
diseases = basic_clean(diseases, "diseases")
groups = basic_clean(groups, "groups")
subgroups = basic_clean(subgroups, "subgroups")
subscribers = basic_clean(subscribers, "subscribers")
hospitals = basic_clean(hospitals, "hospitals")
claims = basic_clean(claims, "claims")

# 3. (Optional) Rename columns or fix types (example)
if 'date_of_birth' in patients.columns:
    patients['date_of_birth'] = pd.to_datetime(patients['date_of_birth'], errors='coerce')

# 4. Save cleaned files to processed directory
patients.to_csv('data/processed/patients_clean.csv', index=False)
diseases.to_csv('data/processed/diseases_clean.csv', index=False)
groups.to_csv('data/processed/groups_clean.csv', index=False)
subgroups.to_csv('data/processed/subgroups_clean.csv', index=False)
subscribers.to_csv('data/processed/subscribers_clean.csv', index=False)
hospitals.to_excel('data/processed/hospitals_clean.xlsx', index=False)
claims.to_csv('data/processed/claims_clean.csv', index=False)

print("\n✅ All files cleaned and saved to data/processed/")
