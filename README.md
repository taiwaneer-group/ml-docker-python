# ml-docker-python
Simple python in docker setup for Udacity ML course

The docker setup here will build and download all the dependencies for the mini project

## Docker introduction ##

### What is Docker? ###

[Docker introduction](https://docs.docker.com/engine/docker-overview/)

How to install docker in your machine?

[Docker for Mac] (https://docs.docker.com/docker-for-mac/install/)

[Docker for Window] (https://docs.docker.com/docker-for-windows/install/)

[Docker for linux Ubuntu] (https://docs.docker.com/install/linux/docker-ee/ubuntu/)

#### After docker is installed in your machine ####

Run this command in your terminal to download the codes to your desired location in your machine.

`git clone https://github.com/taiwaneer-group/ml-docker-python.git`

This repo contains mini project setup from Udacity.

Make sure you are in it's folder.

Run

`docker build -t ml-python-2.7 .`

(Don't forget the . at the end and you can change ml-python-2.7 to any name you like)

Docker will downloand and build the image.

After the image is built.

Run

`docker run -t -d --name ml-container -v ${PWD}:/usr/src/app ml-python-2.7`

(${PWD} means your current folder and you can change the ml-container to any name you like)

After it's done.

Run

`docker exec -it ml-container /bin/bash`

You will be in the docker container and should be able to run the python startup.py in tool directory.

Once you are done with the development, you can run

`docker stop ml-container`

to stop the container


To start from where you were.

Run

`docker start ml-container`

and

`docker exec -it ml-container /bin/bash`

it will go to the folder in the container and your works will still be there.

Any files you change in the host will immediately reflect in the container.

More details will be added in the future.












