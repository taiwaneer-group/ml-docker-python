FROM python:2.7

# Updating repository
RUN apt-get update

# Create a folder in container
RUN mkdir /usr/src/app

# set the working directory in the container
WORKDIR /usr/src/app

# Copying requirements.txt file
COPY requirements.txt requirements.txt

# Pip install
RUN pip install --no-cache -r requirements.txt

# Copy current files to container
COPY . .

CMD [ "python" ]