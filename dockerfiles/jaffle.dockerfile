FROM prefecthq/prefect:2.13-python3.9

WORKDIR /usr/src/dbt

COPY . .
COPY ./profiles.yml /root/.dbt/

# Install the dbt Postgres adapter. This step will also install dbt-core
RUN pip install --upgrade pip
RUN pip install dbt-snowflake==1.2.0
RUN pip install pytz
RUN pip install "prefect-dbt[snowflake]"

ENTRYPOINT [ "python", "orchestration/scheduled_flow.py" ]