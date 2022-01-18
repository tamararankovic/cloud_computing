FROM python:3.9

WORKDIR /usr/src

RUN apt update && pip install poetry
COPY pyproject.toml poetry.lock /usr/src/
RUN poetry install
COPY webapp /usr/src/webapp

CMD cd webapp && \
    poetry run python manage.py makemigrations && \
    poetry run python manage.py migrate && \
    poetry run gunicorn --bind 0.0.0.0:8000 webapp.wsgi