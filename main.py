from rich.console import Console
from rich.panel import Panel
from pyfiglet import Figlet
import shutil

from modules.sysinfo import show_sysinfo
from modules.network import show_network
from modules.processes import show_processes
from modules.hashing import hash_file

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


show_banner()

while True:

    command = input(
        "\ncyberops> "
    ).strip()

    cmd = command.lower()

    if cmd == "help":

        console.print(
            "\n[bold cyan]Available Commands[/bold cyan]\n"
        )

        console.print(
            "[green]help[/green]       - Show commands"
        )

        console.print(
            "[green]sysinfo[/green]    - System information"
        )

        console.print(
            "[green]network[/green]    - Network information"
        )

        console.print(
            "[green]processes[/green]  - Running processes"
        )

        console.print(
            "[green]hash[/green]       - Generate file SHA256 hash"
        )

        console.print(
            "[green]clear[/green]      - Clear screen"
        )

        console.print(
            "[green]exit[/green]       - Exit CyberOps"
        )

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