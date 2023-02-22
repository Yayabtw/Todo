import click
import io
import toudou.models as models
import toudou.services as services
from datetime import datetime
from flask import *


@click.group()
def cli():
    pass


@cli.command()
def init_db():
    models.init_db()


@cli.command()
@click.option("-t", "--task", prompt="Your task", help="The task to remember.")
@click.option("-d", "--due", type=click.DateTime(), default=None, help="Due date of the task.")
def create(task: str, due: datetime):
    models.create_todo(task, due=due)


@cli.command()
@click.option("-t", "--task", required=True, prompt="Your task", help="Todo.")
def get(todo: str):
    models.get_todo(todo)


@cli.command()
@click.option("--as-csv", is_flag=True, help="Ouput a CSV string.")
def get_all(as_csv: bool):
    if as_csv:
        click.echo(services.export_to_csv())
    else:
        click.echo(models.get_todos())


@cli.command()
@click.argument('csv_file', type=click.File('r'))
def import_csv(csv_file: io.TextIOWrapper):
    services.import_from_csv(csv_file.read())


@cli.command()
@click.option("-i", "--id", required=True, type=click.INT, help="Todo's id.")
@click.option("-c", "--complete", required=True, type=click.BOOL, help="True if the task is completed")
@click.option("-t", "--task", prompt="Your task", help="The task to remember.")
@click.option("-d", "--due", type=click.DateTime(), default=None, help="Due date of the task.")
def update(complete: bool, task: str, due: datetime):
    models.update_todo(task, complete, due)


@cli.command()
@click.option("--id", required=True, type=click.INT, help="Todo's id.")
def delete(todo: str):
    models.delete_todo(todo)


app = Flask(__name__)


@app.route('/')
@app.route('/<todos>')
def render(todos=None):
    return render_template("index.html", todos=models.get_todos())
