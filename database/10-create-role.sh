#!/bin/bash
echo 'Creating role...'

psql postgres://postgres@:5432/postgres -tAc "CREATE ROLE ${DB_USER} LOGIN PASSWORD '${DB_PASSWORD}';"

echo 'Role created!'