
  
    

create or replace transient table FAKESTORE_DEV_DB.DBT_MODELS_analytics.dim_users
    

    
    as (select
    USER_ID,
    USERNAME,
    EMAIL,
    ADDRESS_CITY
from FAKESTORE_DEV_DB.DBT_MODELS_staging_layer.stg_users
    )
;


  