#!/bin/bash
echo 'Creating database...'

psql postgres://postgres@:5432/postgres -tAc "CREATE DATABASE ${DB_NAME};"

echo 'Database created!'