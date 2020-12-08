FROM python:3.9

RUN apt-get update

WORKDIR /code

COPY requirements.txt /code/requirements.txt

COPY entrypoint.sh /code/entrypoint.sh

RUN pip3 install -r requirements.txt

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]
