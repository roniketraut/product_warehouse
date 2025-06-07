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
        {{source('python_raw_data', 'STG_PRODUCTS')}}
)

SELECT ID AS PRODUCT_ID, TITLE, PRICE, DESCRIPTION, CATEGORY, RATING, RATING_COUNT 

FROM source