#https://fastapi.tiangolo.com/deployment/docker/

FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /code

# On fait un "copié-collé"
COPY ./requirements.txt /code/requirements.txt  

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# on "copie-colle" tout ce qu'il y a dans src
COPY ./src /code/src

CMD ["uvicorn", "src.API:app", "--host", "0.0.0.0", "--port", "80"]


# # Use an official Python runtime as a parent image
# FROM python:3.10

# # Set the working directory in the container
# WORKDIR /code

# # Copy the current directory contents into the container at /code
# COPY . /code

# # Install any needed packages specified in requirements.txt
# COPY Docker/requirement.txt /code/
# RUN pip install --no-cache-dir -r requirement.txt

# # Make port 80 available to the world outside this container
# EXPOSE 80

# # Define environment variable
# ENV MODULE_NAME="API"
# ENV VARIABLE_NAME="app"

# # Run app.py when the container launchesp
# CMD ["uvicorn", "API:app", "--host", "0.0.0.0", "--port", "80"]

















