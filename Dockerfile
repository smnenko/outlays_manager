FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /outlays_manager

COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pip install pipenv
RUN pipenv install

COPY . .