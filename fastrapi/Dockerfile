FROM python:3.10-bullseye
RUN python -m pip install --upgrade pip
WORKDIR /app

# Copy the top-level files
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY authenticator.py authenticator.py

# Copy all of the subdirectories that contain your application

COPY queries queries
COPY routers routers
COPY migrations migrations

RUN python -m pip install -r requirements.txt
CMD python -m migrations up && uvicorn main:app --host 0.0.0.0 --port 80
