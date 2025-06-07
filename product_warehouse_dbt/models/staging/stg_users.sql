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
     FROM {{ source('python_raw_data', 'STG_USERS')}}
)

SELECT ID AS USER_ID, EMAIL, USERNAME, PASSWORD, ADDRESS_CITY
FROM source