# `server` directory

This directory contains the source for the Flask server portion of the application.

The `api` directory holds definitions for different API endpoints. 

The `models` directory holds definitions for different data models. These models
are used as Python classes, but also can be used to define database tables to be
created by the SQLAlchemy ORM. 

`dev.Dockerfile` defines how the container's image is built.

`config.py` pulls environment variables that were provided via Docker Compose.

`database.py` initializes the database connection through SQLAlchemy.

`entrypoint.sh` runs a SQLAlchemy database migration before starting the Flask 
server, which updates, adds and removes tables from the database to reflect any 
changes made to the model classes.

`manage.py` exposes methods used by `entrypoint.sh` to perform database migrations.

`requirements.txt` defines the required Python libraries that are installed during 
image creation.
- NOTE: While not required to run the application, it may be helpful to install
these libraries on your host system for code completion support in your IDE.