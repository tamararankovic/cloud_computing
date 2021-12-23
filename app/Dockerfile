FROM python:3.9

WORKDIR /usr/src

RUN apt update
COPY pyproject.toml poetry.lock /usr/src
RUN pip install poetry
RUN poetry install
COPY webapp /usr/src/webapp

EXPOSE 8000

CMD cd webapp && \
    poetry run python manage.py makemigrations && \
    poetry run python manage.py migrate && \
    poetry run python manage.py runserver 0.0.0.0:8000