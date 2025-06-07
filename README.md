# Product Data Warehouse Project

This project demonstrates an end-to-end ELT (Extract, Load, Transform) pipeline for building a data warehouse in Snowflake. It extracts data from the FakeStoreAPI, loads it into Snowflake, and then uses dbt (Data Build Tool) for in-warehouse transformations to create a dimensional model.

## Project Overview

The goal is to create a data warehouse that models product, user, and cart information, allowing for potential future analysis and business intelligence.

**Data Flow:**

1.  **Extract:** Python scripts (`data_call.py`) fetch data from the [FakeStoreAPI](https://fakestoreapi.com/) for products, users, and carts.
2.  **Load (Light Transform):** Python scripts (`light_cleaning.py`, `load_to_staging.py`) perform initial light cleaning (e.g., renaming columns, type conversions) and load the data into a raw staging schema in Snowflake.
3.  **Transform:** dbt models are used to:
    *   Clean and prepare the raw data in a staging layer.
    *   Build dimensional models (Dimension tables: `dim_products`, `dim_users`, `dim_date`).
    *   Build fact tables (Fact table: `fact_carts`).

## Technologies Used

*   **Python 3.13:** For data extraction and loading (EL part of ELT).
    *   `requests`: For making HTTP requests to the API.
    *   `pandas`: For data manipulation and structuring.
    *   `snowflake-connector-python`: For connecting to and interacting with Snowflake.
    *   `python-dotenv`: For managing environment variables (credentials, configurations).
*   **dbt (Data Build Tool):** For the transformation (T part of ELT) layer within Snowflake.
    *   `dbt-snowflake` adapter.
*   **Snowflake:** Cloud data warehouse.
*   **Git & GitHub:** For version control.

## Setup Instructions

1.  **Clone the Repository (if applicable):**
    ```bash
    git clone <repository-url>
    cd PRODUCT_WAREHOUSE
    ```

2.  **Set up Python Virtual Environment:**
    ```bash
    python -m venv venv
    # On Windows (Git Bash/MINGW64):
    source venv/Scripts/activate
    # On Windows (Command Prompt/PowerShell):
    # .\venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Snowflake Environment Variables:**
    *   Create a `.env` file in the `PRODUCT_WAREHOUSE` root directory by copying `.env.example` (if you create one) or by creating it from scratch.
    *   Populate it with your Snowflake credentials and configurations:
        ```env
    *   **Important:** Ensure the `.env` file is listed in your `.gitignore` file to prevent committing secrets.

5.  **Configure dbt Profile:**
    *   Ensure you have a `profiles.yml` file located at `~/.dbt/profiles.yml`.
    *   Configure a profile (e.g., `product_warehouse_dbt`) to connect to your Snowflake instance. It can use the environment variables set above:
      ```yaml
      # In ~/.dbt/profiles.yml
      product_warehouse_dbt:
        target: dev
        outputs:
          dev:
            type: snowflake
            account: "{{ env_var('SNOWFLAKE_ACCOUNT') }}"
            user: "{{ env_var('SNOWFLAKE_USER') }}"
            password: "{{ env_var('SNOWFLAKE_PASSWORD') }}"
            role: "{{ env_var('SNOWFLAKE_ROLE') }}"
            warehouse: "{{ env_var('SNOWFLAKE_WAREHOUSE') }}"
            database: "{{ env_var('SNOWFLAKE_DATABASE') }}"
            schema: "{{ env_var('SNOWFLAKE_DBT_DEFAULT_SCHEMA', 'DBT_MODELS') }}" # dbt's default output
            threads: 4
            client_session_keep_alive: False
      ```

## Running the Pipeline

Execute the steps in order:

1.  **Load Raw Data into Snowflake:**
    (Ensure your `.env` file is configured and your virtual environment is active)
    From the `PRODUCT_WAREHOUSE` root directory:
    ```bash
    python load_to_staging.py
    ```
    Verify in Snowflake that tables like `STG_PRODUCTS`, `STG_USERS`, `STG_CARTS` are created and populated in the schema defined by `SNOWFLAKE_SCHEMA_FOR_PYTHON_STAGING`.

2.  **Run dbt Transformations:**
    Navigate to your dbt project directory:
    ```bash
    cd product_warehouse_dbt
    ```
    Then run:
    ```bash
    dbt run       # Builds all models
    dbt test      # Runs all data tests
    ```
    Verify in Snowflake that your staging views (e.g., in `STAGING_LAYER` schema) and mart tables (e.g., in `ANALYTICS` schema) are created.

## dbt Project Details

*   **dbt project configuration:** `product_warehouse_dbt/dbt_project.yml`
*   **Source definitions:** `product_warehouse_dbt/models/staging/schema.yml`
*   **Staging models:** Located in `product_warehouse_dbt/models/staging/`
*   **Mart models (dimensions, facts):** Located in `product_warehouse_dbt/models/marts/`

Below are the images from Snowflake
![alt text](image.png)

![alt text](image-1.png)

