import os
from flask_migrate import Migrate, upgrade
from app import app, db

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)


@app.cli.command("db", help="Perform database migrations")
def database_migrations():
    upgrade()


if __name__ == '__main__':
    app.run()
