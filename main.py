from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from pyfiglet import Figlet
import shutil

from modules.sysinfo import show_sysinfo
from modules.network import show_network
from modules.processes import show_processes
from modules.hashing import hash_file
from modules.password_generator import generate_password
from modules.password_checker import check_password_strength
from modules.monitor import show_monitor

console = Console()


def show_banner():

    width = shutil.get_terminal_size().columns

    if width < 80:
        font = "small"

    elif width < 120:
        font = "standard"

    else:
        font = "slant"

    fig = Figlet(font=font)

    banner = fig.renderText("CyberOps")

    console.print(
        banner,
        style="bold green"
    )

    console.print(
        Panel(
            "[bold green]SYSTEM STATUS : ONLINE[/bold green]\n"
            "[cyan]CyberOps Command Center[/cyan]",
            title="[red]CYBEROPS[/red]",
            border_style="green",
            expand=False
        )
    )


def show_help():

    table = Table(title="CYBEROPS COMMANDS")

    table.add_column(
        "Command",
        style="cyan",
        no_wrap=True
    )

    table.add_column(
        "Description",
        style="green"
    )

    table.add_row(
        "help",
        "Show all commands"
    )

    table.add_row(
        "sysinfo",
        "System information"
    )

    table.add_row(
        "network",
        "Network information"
    )

    table.add_row(
        "processes",
        "Running processes"
    )

    table.add_row(
        "hash",
        "Generate SHA256 hash"
    )

    table.add_row(
        "password",
        "Generate strong password"
    )

    table.add_row(
        "checkpass",
        "Check password strength"
    )

    table.add_row(
        "monitor",
        "System monitor"
    )

    table.add_row(
        "clear",
        "Clear screen"
    )

    table.add_row(
        "exit",
        "Exit CyberOps"
    )

    console.print(table)


show_banner()

while True:

    command = input(
        "\ncyberops> "
    ).strip()

    cmd = command.lower()

    if cmd == "help":

        show_help()

    elif cmd == "sysinfo":

        show_sysinfo()

    elif cmd == "network":

        show_network()

    elif cmd == "processes":

        show_processes()

    elif cmd == "hash":

        filepath = input(
            "Enter file path: "
        ).strip()

        hash_file(filepath)

    elif cmd == "password":

        try:

            length = int(
                input(
                    "Password Length: "
                )
            )

            password = generate_password(
                length
            )

            console.print(
                f"\n[bold green]Generated Password:[/bold green] {password}"
            )

        except ValueError:

            console.print(
                "[bold red]Please enter a valid number[/bold red]"
            )

    elif cmd == "checkpass":

        password = input(
            "Enter Password: "
        )

        check_password_strength(
            password
        )

    elif cmd == "monitor":

        show_monitor()

    elif cmd == "clear":

        console.clear()
        show_banner()

    elif cmd == "exit":

        console.print(
            "\n[bold red]Shutting Down CyberOps...[/bold red]"
        )

        break

    else:

        console.print(
            "[bold red]Unknown Command[/bold red]"
        )