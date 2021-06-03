FROM python:3.8

RUN apt-get update && apt-get install -y \
    python-pip
RUN pip install --upgrade pip

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt 

# ENV FLASK_APP=main.py

# VOLUME [ ".", ".", ]

# CMD [ "flask", "run", "--host", "0.0.0.0", "-p", "5000"  ]