# `client` directory

This directory contains the source for the Angular client portion of the application.

The `src` directory holds the source code and assets for the frontend. 

The `dev.Dockerfile` file defines how the container's image is built.

The `.dockerignore` file excludes the `node_modules` directory from being copied to
the image since the dependencies will already be installed there.

`healthcheck.js` defines a health check test that is used by Docker at an interval
to confirm the container is still running as it should be.