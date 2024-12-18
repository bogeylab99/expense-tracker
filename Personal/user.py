from .database import Session, User
import click

@click.command()
@click.argument('name')
@click.argument('email')
def add_user(name, email):
    """Add a new user."""
    session = Session()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.close()
    click.echo(f"User '{name}' added successfully!")

@click.command()
@click.argument('user_id', type=int)
def delete_user(user_id):
    """Delete a user by ID."""
    session = Session()
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        click.echo(f"User ID {user_id} deleted successfully!")
    else:
        click.echo("User not found!")
    session.close()
