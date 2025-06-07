
  
    

create or replace transient table FAKESTORE_DEV_DB.DBT_MODELS_analytics.dim_products
    

    
    as (select
    PRODUCT_ID,
    TITLE,
    PRICE,
    CATEGORY,
    RATING,
    RATING_COUNT
from FAKESTORE_DEV_DB.DBT_MODELS_staging_layer.stg_products
    )
;


  