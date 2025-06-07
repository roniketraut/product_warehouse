with raw_dates as (
    SELECT DISTINCT CAST(DATE AS DATE) as DATE
    from {{ref('stg_carts')}}
)

SELECT 
    date,
    TO_CHAR(date, 'YYYYMMDD')::INT AS DATE_ID,
    EXTRACT(YEAR FROM date)::int AS YEAR,
    EXTRACT(MONTH FROM date)::int AS MONTH,
    EXTRACT(DAY FROM date)::int AS DAY,
    TO_CHAR(date, 'Day') AS DAY_NAME,
    TO_CHAR(date, 'Month') AS MONTH_NAME,
    EXTRACT(quarter FROM date)::int AS QUARTER
FROM raw_dates
