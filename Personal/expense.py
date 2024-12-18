from .database import Session, Expense, User, Category 
import click

@click.command()
@click.argument('user_id', type=int)
@click.argument('category_id', type=int)
@click.argument('amount', type=float)
def add_expense(user_id, category_id, amount):
    """Add a new expense."""
    session = Session()
    expense = Expense(user_id=user_id, category_id=category_id, amount=amount)
    session.add(expense)
    session.commit()
    session.close()
    click.echo(f"Expense of ${amount} added successfully!")

@click.command()
@click.argument('user_id', type=int)
def delete_expense(user_id):
    """Delete expenses by user ID."""
    session = Session()
    expenses = session.query(Expense).filter_by(user_id=user_id).all()
    if expenses:
        for expense in expenses:
            session.delete(expense)
        session.commit()
        click.echo(f"All expenses for user ID {user_id} deleted successfully!")
    else:
        click.echo("No expenses found for the specified user ID.")
    session.close()
