select
    USER_ID,
    USERNAME,
    EMAIL,
    ADDRESS_CITY
from {{ ref('stg_users') }}