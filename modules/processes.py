import psutil
from rich.table import Table
from rich.console import Console

console = Console()


def show_processes():

    table = Table(title="RUNNING PROCESSES")

    table.add_column("PID", style="yellow")
    table.add_column("Process Name", style="green")

    count = 0

    for process in psutil.process_iter(["pid", "name"]):

        try:

            pid = str(process.info["pid"])
            name = process.info["name"]

            if name:

                table.add_row(pid, name)

                count += 1

            if count >= 25:
                break

        except:
            pass

    console.print(table)