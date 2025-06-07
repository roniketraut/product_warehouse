
  create or replace   view FAKESTORE_DEV_DB.DBT_MODELS_staging_layer.stg_users
  
   as (
    with source as (
    SELECT
        ID,
        EMAIL,
        USERNAME,
        PASSWORD,
        ADDRESS_GEOLOCATION_LAT,
        ADDRESS_GEOLOCATION_LONG,
        ADDRESS_CITY,
        ADDRESS_STREET,
        ADDRESS_NUMBER,
        ADDRESS_ZIPCODE,
        FIRSTNAME,
        LASTNAME
     FROM FAKESTORE_DEV_DB.PYTHON_STAGING.STG_USERS
)

SELECT ID AS USER_ID, EMAIL, USERNAME, PASSWORD, ADDRESS_CITY
FROM source
  );

