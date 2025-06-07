
  
    

create or replace transient table FAKESTORE_DEV_DB.DBT_MODELS_analytics.fact_carts
    

    
    as (SELECT
    c.CART_ID,
    d.DATE_ID, 
    c.QUANTITY,
    c.PRODUCT_ID,
    c.USER_ID
FROM 
    FAKESTORE_DEV_DB.DBT_MODELS_staging_layer.stg_carts c
JOIN 
    FAKESTORE_DEV_DB.DBT_MODELS_analytics.dim_date d ON c.DATE = d.DATE
LEFT JOIN FAKESTORE_DEV_DB.DBT_MODELS_analytics.dim_products p ON c.PRODUCT_ID = p.PRODUCT_ID
LEFT JOIN FAKESTORE_DEV_DB.DBT_MODELS_analytics.dim_users u ON c.USER_ID = u.USER_ID
    )
;


  