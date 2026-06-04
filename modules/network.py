import socket
from rich.table import Table
from rich.console import Console

console = Console()


def show_network():

    hostname = socket.gethostname()

    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "Unknown"

    table = Table(title="NETWORK INFORMATION")

    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Hostname", hostname)
    table.add_row("IP Address", ip)

    console.print(table)