
  create or replace   view FAKESTORE_DEV_DB.DBT_MODELS_staging_layer.stg_products
  
   as (
    with source as (
    SELECT
        ID,
        TITLE,
        PRICE,
        DESCRIPTION,
        CATEGORY,
        IMAGE,
        RATING,
        RATING_COUNT
    FROM 
        FAKESTORE_DEV_DB.PYTHON_STAGING.STG_PRODUCTS
)

SELECT ID AS PRODUCT_ID, TITLE, PRICE, DESCRIPTION, CATEGORY, RATING, RATING_COUNT 

FROM source
  );

