-- Use the `ref` function to select from other models

select *
from FAKESTORE_DEV_DB.DBT_MODELS.my_first_dbt_model
where id = 1