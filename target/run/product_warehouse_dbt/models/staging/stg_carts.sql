
  create or replace   view FAKESTORE_DEV_DB.DBT_MODELS_staging_layer.stg_carts
  
   as (
    WITH raw_source AS (
    SELECT
        ID AS CART_ID,
        CAST(DATE AS DATE) AS DATE,
        QUANTITY,
        PRODUCTID AS PRODUCT_ID,
        USERID AS USER_ID
    FROM FAKESTORE_DEV_DB.PYTHON_STAGING.STG_CARTS
)  

SELECT *
FROM raw_source
  );

