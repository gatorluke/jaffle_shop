from prefect import flow
from prefect_dbt.cli.commands import trigger_dbt_cli_command
import pathlib

dbt_path = pathlib.Path(__file__).resolve().parents[1]

@flow
def trigger_dbt_cli_command_flow():
    result = trigger_dbt_cli_command(
        "dbt debug",
        project_dir=f"{dbt_path}/dbt/"
    )
    return result

trigger_dbt_cli_command_flow()