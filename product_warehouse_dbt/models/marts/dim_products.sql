select
    PRODUCT_ID,
    TITLE,
    PRICE,
    CATEGORY,
    RATING,
    RATING_COUNT
from {{ ref('stg_products') }}