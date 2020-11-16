# Start with Python base image
FROM python:3.8.5-alpine

# Prevent Docker from buffering Python output to terminal
ENV PYTHONUNBUFFERED 1

# Change working directory in image
RUN mkdir -p /app
WORKDIR /app

# Copy directory
COPY . .

# Give execute permission to entrypoint script
RUN chmod 777 ./entrypoint.sh

# Install necessary libraries and Python dependencies
RUN \
 apk add --no-cache postgresql-libs postgresql-client && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# Expose port
EXPOSE 5000

# Start the server
CMD ["sh", "./entrypoint.sh"]