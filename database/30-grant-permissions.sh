#!/bin/bash
echo 'Granting user permissions on database...'

psql postgres://postgres@:5432/postgres -tAc "GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} to ${DB_USER};"

echo 'Permissions granted!'