FROM python:3.8-slim-buster as local

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/api/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 as production

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/api/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./app /app

WORKDIR /app

ENTRYPOINT ["/start"]

