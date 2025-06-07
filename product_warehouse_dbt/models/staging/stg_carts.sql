WITH raw_source AS (
    SELECT
        ID AS CART_ID,
        CAST(DATE AS DATE) AS DATE,
        QUANTITY,
        PRODUCTID AS PRODUCT_ID,
        USERID AS USER_ID
    FROM {{ source('python_raw_data', 'STG_CARTS')}}
)  

SELECT *
FROM raw_source