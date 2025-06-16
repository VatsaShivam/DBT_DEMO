-- models/latest_a1c.sql

with labs as (
  select
    patient_id,
    lab.test_name,
    lab.result,
    lab.unit,
    lab.test_date
  from
    dbt-demo-proj.dbt_demo_dataset.ehr_data_external,
    unnest(lab_results) as lab
  where lab.test_name = "Hemoglobin A1c"
)
select
  patient_id,
  result,
  unit,
  test_date
from (
  select *,
    row_number() over (partition by patient_id order by test_date desc) as rn
  from labs
)
where rn = 1
