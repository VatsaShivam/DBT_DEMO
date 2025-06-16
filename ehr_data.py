import json
import random
from faker import Faker

fake = Faker()

diagnoses = ['Hypertension', 'Diabetes', 'Asthma', 'COPD', 'Heart Disease']
allergens = ['Penicillin', 'Peanuts', 'Latex', 'Shellfish', 'None']
medications = ['Lisinopril', 'Metformin', 'Albuterol', 'Atorvastatin', 'Insulin']
procedures = ['Appendectomy', 'Cataract Surgery', 'Angioplasty', 'Colonoscopy', 'None']
vaccines = ['Influenza', 'COVID-19', 'Tetanus', 'Hepatitis B']

records = []

for i in range(1000):
    gender = random.choice(['M', 'F'])
    med_hist = [{
        "condition": random.choice(diagnoses),
        "diagnosis_date": str(fake.date_between(start_date='-10y', end_date='today')),
        "status": random.choice(['Active', 'Resolved'])
    }]
    allergy = [{
        "allergen": random.choice(allergens),
        "reaction": random.choice(['Rash', 'Anaphylaxis', 'None']) if allergens else "None"
    }]
    med = [{
        "medication_name": random.choice(medications),
        "dosage": f"{random.randint(1, 100)}mg",
        "frequency": random.choice(['Once daily', 'Twice daily']),
        "start_date": str(fake.date_between(start_date='-5y', end_date='today')),
        "end_date": None
    }]
    lab = [{
        "test_name": "Hemoglobin A1c",
        "result": f"{round(random.uniform(5.0, 9.0), 1)}",
        "unit": "%",
        "test_date": str(fake.date_between(start_date='-1y', end_date='today'))
    }]
    proc = [{
        "procedure_name": random.choice(procedures),
        "date": str(fake.date_between(start_date='-10y', end_date='today')),
        "provider": fake.company()
    }]
    imm = [{
        "vaccine": random.choice(vaccines),
        "date": str(fake.date_between(start_date='-2y', end_date='today'))
    }]
    encounter = [{
        "encounter_date": str(fake.date_between(start_date='-1y', end_date='today')),
        "provider": fake.name(),
        "reason": random.choice(['Routine Checkup', 'Follow-up', 'Acute Illness']),
        "notes": fake.sentence()
    }]
    record = {
        "patient_id": f"P{str(i+1).zfill(4)}",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "date_of_birth": str(fake.date_of_birth(minimum_age=1, maximum_age=90)),
        "gender": gender,
        "contact_info": {
            "email": fake.email(),
            "phone": fake.phone_number()
        },
        "medical_history": med_hist,
        "allergies": allergy,
        "medications": med,
        "lab_results": lab,
        "procedures": proc,
        "immunizations": imm,
        "encounters": encounter
    }
    records.append(record)

# Save to NDJSON file for BigQuery
with open("ehr_data_1000.json", "w") as f:
    for record in records:
        f.write(json.dumps(record) + "\n")
