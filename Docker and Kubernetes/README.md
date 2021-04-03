Docker Image:

Image creation was done using the Dockerfile, miniproject_docker.py, and requirements.txt.
After building, the docker image was then pushed to https://hub.docker.com/repository/docker/gozreh33/miniproject with the tag database.

Kubernetes:

The YAML file is used to create a deployment and service for the miniproject app. This is done by pulling the relevant image from docker hub.
