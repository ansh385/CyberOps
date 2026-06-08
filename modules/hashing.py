import hashlib
import os
from rich.console import Console
from rich.panel import Panel

console = Console()


def hash_file(filepath):

    try:

        filepath = filepath.strip()

        filepath = filepath.strip('"')

        filepath = filepath.strip("'")

        if not filepath:

            console.print(
                "[red]Please enter a file path.[/red]"
            )

            return

        if not os.path.isfile(filepath):

            console.print(
                "[red]File not found.[/red]"
            )

            return

        sha256 = hashlib.sha256()

        with open(filepath, "rb") as file:

            while True:

                chunk = file.read(4096)

                if not chunk:
                    break

                sha256.update(chunk)

        console.print(
            Panel(
                f"[bold green]{sha256.hexdigest()}[/bold green]",
                title=f"SHA256 : {os.path.basename(filepath)}",
                border_style="green"
            )
        )

    except PermissionError:

        console.print(
            "[red]Permission denied.[/red]"
        )

    except Exception as e:

        console.print(
            f"[red]Error: {e}[/red]"
        )