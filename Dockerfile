FROM python:3.7.12
WORKDIR /recommender

RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends tini

RUN \
  pip install --upgrade pip && \
  pip install "poetry==1.1.11"

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . .

ENTRYPOINT ["tini", "--"]
CMD ["python", "-m", "poetry", "run", "gunicorn", "wsgi"]
