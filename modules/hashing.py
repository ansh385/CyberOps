import hashlib
import os
from rich.console import Console
from rich.panel import Panel

console = Console()


def hash_file(filepath):

    try:

        if not os.path.exists(filepath):

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
                f"[green]{sha256.hexdigest()}[/green]",
                title=f"SHA256 : {os.path.basename(filepath)}"
            )
        )

    except Exception as e:

        console.print(
            f"[red]{e}[/red]"
        )