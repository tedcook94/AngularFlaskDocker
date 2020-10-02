# `database` directory

This directory contains the necessary files to configure the startup of the
PostgreSQL database container.

The `dev.Dockerfile` file defines how the container's image is built.

Any `.sh` or `.sql` scripts are ran during the database container's initialization.
They are run in alphabetical order, so their filenames should be prefixed by an
ordered number to ensure they are executed in the proper sequence. These scripts
are only run if the database container finds that there is no existing database, so
they provide a handy way of conducting initial database configuration.

The database's data is stored in a Docker Volume, and as such will not be found
anywhere in this repo.