-- models/first_encounter.sql

with encounters as (
  select
    patient_id,
    encounter.encounter_date
  from
    dbt-demo-proj.dbt_demo_dataset.ehr_data_external,
    unnest(encounters) as encounter
)
select
  patient_id,
  min(encounter_date) as first_encounter_date
from encounters
group by patient_id
