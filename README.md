# Angular + Flask + Docker/Kubernetes Example

## Overview

This is an example of an application using an Angular front-end, Flask web 
server, PostgreSQL database, SQLAlchemy ORM and Nginx router. All of these 
components are packaged into individual Docker containers that can be run 
simultaneously using Docker Compose or Kubernetes.

Each directory represents its own container:

- `client` directory
  - Angular (v10.1.3)
- `database` directory
  - PostgreSQL (v13.0)
- `router` directory
  - Nginx (v1.19.2)
- `server` directory
  - Python (v3.8.5)
  - Flask (~=v1.1.2)
  - Flask-SQLAlchemy (~=v2.4.1)
  - Flask-Migrate (~=v2.5.2)

Each directory contains its own Dockerfile (`dev.Dockerfile`) that defines
how the container's image is built. Multiple Dockerfiles can exist to define
different build configurations (e.g. `ua.Dockerfile`, `prod.Dockerfile`, 
etc.).

`docker-compose.dev.yml` defines how all of the containers should run together
when started via Docker Compose. `dev.env` contains several environment 
variables used by one or more of the containers and is passed in via Docker 
Compose. Like the Dockerfiles, multiple Docker Compose and environment files 
can be defined for different configurations (e.g. `docker-compose.prod.yml` 
and `prod.env`).

For more information on each of the components, see the READMEs in their 
directories.

## Building and Running with Docker Compose

To run this project, begin by downloading Docker. On Linux, install Docker 
Engine via your distro's package manager. On Mac and Windows, install Docker 
Desktop via the installer found on Docker's site.

After installing Docker, clone this repo, open a terminal in the root 
directory of the project, and run the following command:

> `docker-compose -f .\docker-compose.dev.yml up`

This will build all of the images and start the containers in a controlled 
order. Once Docker has finished creating and starting the containers, the 
terminal will display the output of each container and you will be able to 
access the client at `localhost:8080`.

To stop the containers, press Ctrl+C in the terminal and wait for the 
containers to stop.

In the included `dev` configuration, changes made in the Angular client and 
Flask backend will be detected and trigger an automatic reload, meaning you 
should rarely have to restart the containers.

The following are more useful commands relating to Docker and Docker Compose:

- `docker-compose -f .\docker-compose.dev.yml up -d` will start the containers 
in "daemon mode", which detaches them from the terminal. This frees the terminal 
up to run other commands, but prevents the containers from displaying any 
output. To stop the containers once they are running in daemon mode, run 
`docker-compose -f .\docker-compose.dev.yml down`.
- `docker-compose -f .\docker-compose.dev.yml up --build` will force a rebuild 
of the container's images before running. This is required when making changes 
to Dockerfiles or any files referenced in a Dockerfile (e.g. changes in 
`requirements.txt` for the server).
- `docker container prune -f; && docker image prune -f; && docker volume prune -f` 
will remove all unused Docker containers, images and data volumes. This can be 
good if you're experiencing issues and want to clear out your environment.
  - NOTE: if you run the `docker volume prune` portion of this command while 
  the `database_container` is not running, your local copy of the PostgreSQL 
  database will be deleted.

## Building and Running with Kubernetes

This repo contains an example of a UA deployment to Kubernetes. The Kubernetes
configuration supports auto-scaling for the client and server components, as
well as rolling updates for the client, server and database.

To deploy to Kubernetes locally, download Docker as described above. Next, you
will need to install a local Kubernetes cluster. On Mac and Windows, this can
be done through Docker Desktop by selecting `Enable Kubernetes` under the Kubernetes
heading in Settings. On Linux, you will wall want to install
[minikube](https://minikube.sigs.k8s.io/docs/start/). After install, you can
confirm Kubernetes is running with the command `kubectl version`.

To install the UA deployment to your local Kubernetes cluster, run the `deploy.sh`
script in the `kubernetes/ua` folder. That script will create all of the necessary
Docker images, deployments, services, data claims, config maps and autoscalers,
as well as creating an ingress to access the Kubernetes network.

Once the script has completed, you should be able to access the client at
`localhost:80`.

The following are more useful commands relating to Kubernetes:

- `kubectl get pods` will show a short status of all the current pods, while
`kubectl describe pods` will show more information.
  - `pods` can be replaced with any other Kubernetes object (e.g. deployments,
  services, etc.) to get information on those.
  - You can also use the `kubectl get pod <pod-name>` to get information on a
  specific object.
- The server component has a `/api/cpu` endpoint that can be used to simulate high
CPU usage in order to test auto-scaling as follows:
  - Run `kubectl run -i --tty load-generator --rm --image=busybox --restart=Never`
  `--/bin/sh -c "while sleep 0.01; do wget -q -O- http://server-service:5000/api/cpu;`
  `done"` in a terminal.
  - Open a second terminal and run `kubectl get hpa` to see the status of all
  Horizontal Pod Autoscalers.
  - Watch how the CPU usage of the server pods will increase, eventually surpassing
  the 50% target.
  - The Autoscaler will then create a third pod, which you can see via `kubectl get pods`,
  dropping the CPU usage below 50%.
  - Stop the command in the first terminal, lowering the server CPU usage drastically.
  - After several minutes, the Autoscaler will determine that the third pod is no longer
  needed and terminate it.

## Miscellaneous

- `reqs.http` documents the REST endpoints available from the server, as well as 
their expected inputs. When used with the 
["REST Client" extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
in VS Code, it can also allow you to test the endpoints directly from the file.

- This repo uses a pre-commit Git hook to remind developers of some best practices 
before committing. This hook script uses terminal prompts, and thus doesn't work 
with most graphical Git clients (e.g. Sourcetree, VS Code's Git integration, etc.). 
If you prefer to use a graphical Git client, look for a setting that allows you to 
skip commit hooks.
  - Sourcetree has a "Commit options..." dropdown above the Commit button that 
  allows you to select "Bypass commit hooks".
  - VS Code should have support for this starting with v1.50 thanks to 
  [this PR](https://github.com/microsoft/vscode/pull/106335).