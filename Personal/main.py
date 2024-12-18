import click
from .database import initialize_db
from .user import add_user, delete_user
from .category import add_category, delete_category
from .expense import add_expense, delete_expense

@click.group()
def cli():
    """Personal Expense Tracker CLI"""
    pass

@cli.command()
def initialize():
    """Initialize the database."""
    initialize_db()
    click.echo("Database initialized successfully!")

# User commands
cli.add_command(add_user)
cli.add_command(delete_user)

# Category commands
cli.add_command(add_category)
cli.add_command(delete_category)

# Expense commands
cli.add_command(add_expense)
cli.add_command(delete_expense)

if __name__ == "__main__":
    cli()
