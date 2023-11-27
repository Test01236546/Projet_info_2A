#https://fastapi.tiangolo.com/deployment/docker/

FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /code

# On fait un "copié-collé"
COPY ./requirements.txt /code/requirements.txt  

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# on "copie-colle" tout ce qu'il y a dans src
COPY ./src /code/src

CMD ["uvicorn", "src.API:app", "--host", "0.0.0.0", "--port", "8000"]




