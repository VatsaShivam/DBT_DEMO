-- models/patients_with_conditions.sql
with
    base as (
        select
            patient_id,
            first_name,
            last_name,
            date_of_birth,
            gender,
            contact_info.email as email,
            contact_info.phone as phone,
            med.condition as condition,
            med.diagnosis_date as diagnosis_date,
            med.status as condition_status
        from
            dbt - demo - proj.dbt_demo_dataset.ehr_data_external,
            unnest(medical_history) as med
    )

select *
from base
limit 500
