import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Set seed for reproducibility
Faker.seed(42)
np.random.seed(42)

# Define number of records
num_records = 1000

# Define possible diagnoses and treatments
possible_diagnoses = ['Diabetes', 'Hypertension', 'Asthma', 'Cancer', 'Heart Disease']
possible_treatments = {
    'Diabetes': ['Insulin', 'Metformin'],
    'Hypertension': ['Beta Blockers', 'ACE Inhibitors'],
    'Asthma': ['Inhaler', 'Steroids'],
    'Cancer': ['Chemotherapy', 'Radiation'],
    'Heart Disease': ['Bypass Surgery', 'Medication']
}

# Generate data
records = []
for i in range(1, num_records + 1):
    diagnosis = random.choice(possible_diagnoses)
    treatment = random.choice(possible_treatments[diagnosis])
    record = {
        'PatientID': i,
        'Name': fake.name(),
        'Age': random.randint(1, 100),
        'Gender': random.choice(['M', 'F']),
        'Diagnosis': diagnosis,
        'Treatment': treatment,
        'VisitDate': fake.date_between(start_date='-2y', end_date='today').isoformat()
    }
    records.append(record)

# Create DataFrame
df = pd.DataFrame(records)

# Save to CSV
csv_filename = 'health_care_data_1000.csv'
df.to_csv(csv_filename, index=False)

# Preview first 5 rows
# preview = df.head().to_dict(orient='records')

# preview