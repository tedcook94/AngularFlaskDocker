# `router` directory

This directory contains the configuration files for the Nginx router.

The `dev.Dockerfile` file defines how the container's image is built.

The `dev.conf` file defines how traffic should be routed to different containers. 
Currently any `/api` traffic is routed to the Flask server, and all other traffic 
is routed to the Angular client.