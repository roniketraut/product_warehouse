SELECT
    c.CART_ID,
    d.DATE_ID, 
    c.QUANTITY,
    c.PRODUCT_ID,
    c.USER_ID
FROM 
    {{ ref('stg_carts') }} c
JOIN 
    {{ ref('dim_date') }} d ON c.DATE = d.DATE
LEFT JOIN {{ ref('dim_products') }} p ON c.PRODUCT_ID = p.PRODUCT_ID
LEFT JOIN {{ ref('dim_users') }} u ON c.USER_ID = u.USER_ID        