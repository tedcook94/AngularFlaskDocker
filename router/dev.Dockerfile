# Start with nginx base image
FROM nginx:1.19.2-alpine

# Copy config file
COPY ./dev.conf /etc/nginx/nginx.conf

# Expose port
EXPOSE 4200

# Start the router
ENTRYPOINT [ "nginx" ]
CMD [ "-g", "daemon off;" ]