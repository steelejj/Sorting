FROM python:3.12.6 as sorting

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app