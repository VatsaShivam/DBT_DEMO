-- models/flatten_medical_history.sql

select
  patient_id,
  first_name,
  last_name,
  date_of_birth,
  gender,
  med.condition,
  med.diagnosis_date,
  med.status
from
  dbt-demo-proj.dbt_demo_dataset.ehr_data_external,
  unnest(medical_history) as med
