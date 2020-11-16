# Start with PostgreSQL base image
FROM postgres:13.0-alpine

# Copy init bash script to startup directory
COPY *.sh /docker-entrypoint-initdb.d/