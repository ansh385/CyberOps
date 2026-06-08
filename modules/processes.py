import psutil
from rich.table import Table
from rich.console import Console

console = Console()

SYSTEM_PROCESSES = {
    "system",
    "idle",
    "registry",
    "smss.exe",
    "csrss.exe",
    "wininit.exe",
    "winlogon.exe",
    "services.exe",
    "lsass.exe",
    "svchost.exe",
    "fontdrvhost.exe",
    "dwm.exe",
    "sihost.exe",
    "taskhostw.exe",
    "runtimebroker.exe"
}


def show_processes():

    table = Table(title="ACTIVE USER PROCESSES")

    table.add_column(
        "PID",
        style="yellow",
        justify="right"
    )

    table.add_column(
        "Process Name",
        style="green"
    )

    table.add_column(
        "RAM (MB)",
        style="cyan",
        justify="right"
    )

    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "memory_info"]
    ):

        try:

            name = process.info["name"]

            if not name:
                continue

            if name.lower() in SYSTEM_PROCESSES:
                continue

            ram_mb = (
                process.info["memory_info"].rss
                / 1024
                / 1024
            )

            processes.append(
                (
                    process.info["pid"],
                    name,
                    ram_mb
                )
            )

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    processes.sort(
        key=lambda x: x[2],
        reverse=True
    )

    for pid, name, ram_mb in processes[:20]:

        table.add_row(
            str(pid),
            name,
            f"{ram_mb:.1f}"
        )

    console.print(table)