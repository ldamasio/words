FROM python:3.11.3-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./api /app/api
COPY ./bin /app/bin
COPY wsgi.py /app/wsgi.py
WORKDIR /app

EXPOSE 8080

ENTRYPOINT ["sh", "/app/bin/run.sh"]