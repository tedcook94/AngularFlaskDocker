#!/bin/bash
echo 'Waiting for PostreSQL to be ready...'

# Check to make sure Postgres has had time to completely start (and create the database if it's the first run)
while [ "$( psql postgres://${DB_USER}:${DB_PASSWORD}@database:5432/${DB_NAME} -tAc "SELECT 1 FROM pg_database WHERE datname='${DB_NAME}'" )" != '1' ]
do
  echo 'PostgreSQL not ready yet...'
  sleep 1
done

echo 'PostgreSQL ready!'

echo 'Starting db init...'
python manage.py db init
echo 'Finished db init!'

echo 'Starting db migrate...'
python manage.py db migrate
echo 'Finished db migrate!'

echo 'Starting db upgrade...'
python manage.py db upgrade
echo 'Finished db upgrade!'

echo 'Starting Flask server...'
python main.py