FROM python:3.8-slim-buster

RUN apt-get update -y

RUN /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run","--host=0.0.0.0"]
