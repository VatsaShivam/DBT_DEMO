-- models/active_medications.sql

select
  patient_id,
  first_name,
  last_name,
  med.medication_name,
  med.dosage,
  med.frequency,
  med.start_date
from
  dbt-demo-proj.dbt_demo_dataset.ehr_data_external,
  unnest(medications) as med
where med.end_date is null
