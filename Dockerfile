# FROM is used to specify the docker base image to be used
FROM tiangolo/uvicorn-gunicorn:python3.8-slim

COPY ./app/requirements.txt .

# RUN performs a command execution on CMD, this one below installs Python requirements
RUN python -m pip install -r requirements.txt

# WORKDIR is equivalent to CD in linux, used to move inside the folder to access the files easily 
WORKDIR /app

# Copying all file from outside folder to inside folder (in our case both are called app)
COPY /app /app

# Runs app.py to start streamlit
CMD ["streamlit", "run", "app.py", "--server.port", "5603"]