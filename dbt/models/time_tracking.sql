{{ config(materialized='incremental') }}

select current_timestamp() as date_inserted