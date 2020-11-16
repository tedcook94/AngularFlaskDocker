# Start with node base image
FROM node:14-alpine as build-stage

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

# Run build command
RUN ng build --prod --outputPath=./dist/build



# Get nginx image for hosting
FROM nginx:1.19.2-alpine

# Remove default nginx site
RUN rm -rf /usr/share/nginx/html/*

# Copy build output to nginx hosting folder
COPY --from=build-stage /app/dist/build /usr/share/nginx/html

# Copy config file
COPY ./nginx-ua.conf /etc/nginx/conf.d/angular.conf

# Expose port
EXPOSE 4200

# Start the router
CMD [ "nginx", "-g", "daemon off;" ]