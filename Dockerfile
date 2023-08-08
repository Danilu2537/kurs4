FROM python:3.11.4-slim

ENV POETRY_VERSION=1.5.1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /opt/app

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root --no-dev

COPY run.py .
COPY ./project/. ./project/.

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]
