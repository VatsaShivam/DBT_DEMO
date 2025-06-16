-- models/patients_with_anaphylaxis.sql

select
  patient_id,
  first_name,
  last_name,
  allergy.allergen,
  allergy.reaction
from
  dbt-demo-proj.dbt_demo_dataset.ehr_data_external,
  unnest(allergies) as allergy
where
  lower(allergy.reaction) = "anaphylaxis"
