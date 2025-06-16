-- models/immunization_coverage.sql

select
  imm.vaccine,
  count(distinct patient_id) as patient_count
from
  dbt-demo-proj.dbt_demo_dataset.ehr_data_external,
  unnest(immunizations) as imm
group by imm.vaccine
