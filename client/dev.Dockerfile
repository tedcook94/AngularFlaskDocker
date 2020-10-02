# Start with node base image
FROM node:14-alpine

# Change working directory in image
RUN mkdir - p /app
WORKDIR /app

# Copy dependency list and install
COPY package.json .
RUN npm install

# Copy rest of directory
COPY . .

# Install Angular CLI
RUN npm install -g @angular/cli@10.1.3

# Expose ports
EXPOSE 4200 49153

# Start dev server
# Listen on all hosts since we will be accessing the container from the host
# Set polling rate for live reload
CMD ng serve --host 0.0.0.0 --poll 100