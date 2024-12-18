from .database import Session, Category
import click

@click.command()
@click.argument('name')
def add_category(name):
    """Add a new category."""
    session = Session()
    category = Category(name=name)
    session.add(category)
    session.commit()
    session.close()
    click.echo(f"Category '{name}' added successfully!")

@click.command()
@click.argument('category_id', type=int)
def delete_category(category_id):
    """Delete a category by ID."""
    session = Session()
    category = session.query(Category).get(category_id)
    if category:
        session.delete(category)
        session.commit()
        click.echo(f"Category ID {category_id} deleted successfully!")
    else:
        click.echo("Category not found!")
    session.close()
