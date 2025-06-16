import pandas as pd
import random
from faker import Faker

fake = Faker()

# Example diseases for the registry
diseases = ['Diabetes', 'Hypertension', 'Asthma', 'COPD', 'Cancer', 'Heart Disease']

data = []

for i in range(1000):
    patient_id = f"R{str(i+1).zfill(4)}"
    name = fake.name()
    age = random.randint(1, 90)
    gender = random.choice(['M', 'F'])
    disease = random.choice(diseases)
    diagnosis_date = fake.date_between(start_date='-10y', end_date='today')
    status = random.choice(['Active', 'Remission', 'Recovered', 'Deceased'])
    last_visit = fake.date_between(start_date=diagnosis_date, end_date='today')
    doctor = fake.name()
    hospital = fake.company()
    
    data.append({
        "PatientID": patient_id,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Disease": disease,
        "DiagnosisDate": diagnosis_date,
        "Status": status,
        "LastVisit": last_visit,
        "Doctor": doctor,
        "Hospital": hospital
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as Parquet
df.to_parquet("patient_disease_registry.parquet", index=False)

print("Parquet file 'patient_disease_registry.parquet' created with 1000 records.")
