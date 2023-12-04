from prefect import flow
from prefect_dbt.cli.commands import trigger_dbt_cli_command
import pathlib

dbt_path = pathlib.Path(__file__).resolve().parents[1]

@flow
def trigger_dbt_cli_command_flow():
    result = trigger_dbt_cli_command(
        "dbt build --select time_tracking",
        project_dir=f"{dbt_path}/dbt/"
    )
    return result

# If we want to _deploy_ this flow to _automate_ it with prefect,
# we need to use the serve method rather than just calling the python script
if __name__ == "__main__":
    # Call at every minute
    trigger_dbt_cli_command_flow.serve(name="flow_2_deployed", cron="* * * * *")