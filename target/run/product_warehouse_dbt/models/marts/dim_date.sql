
  
    

create or replace transient table FAKESTORE_DEV_DB.DBT_MODELS_analytics.dim_date
    

    
    as (with raw_dates as (
    SELECT DISTINCT CAST(DATE AS DATE) as DATE
    from FAKESTORE_DEV_DB.DBT_MODELS_staging_layer.stg_carts
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
    )
;


  