import psutil
from rich.table import Table
from rich.console import Console

console = Console()

def show_monitor():

    table = Table(title="SYSTEM MONITOR")

    table.add_column("Resource", style="cyan")
    table.add_column("Usage", style="green")

    table.add_row(
        "CPU",
        f"{psutil.cpu_percent(interval=1)}%"
    )

    table.add_row(
        "RAM",
        f"{psutil.virtual_memory().percent}%"
    )

    table.add_row(
        "Disk",
        f"{psutil.disk_usage('/').percent}%"
    )

    console.print(table)