from rich.console import Console

console = Console()

def check_password_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in "!@#$%^&*" for c in password):
        score += 1

    if score <= 2:
        console.print("[red]Weak Password[/red]")

    elif score <= 4:
        console.print("[yellow]Medium Password[/yellow]")

    else:
        console.print("[green]Strong Password[/green]")