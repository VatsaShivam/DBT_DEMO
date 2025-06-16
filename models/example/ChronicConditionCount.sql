-- models/chronic_conditions_count.sql

with med_hist as (
  select
    patient_id,
    med.condition
  from
    dbt-demo-proj.dbt_demo_dataset.ehr_data_external,
    unnest(medical_history) as med
)
select
  patient_id,
  count(distinct condition) as chronic_condition_count
from med_hist
group by patient_id
