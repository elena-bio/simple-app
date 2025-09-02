![tests](https://github.com/elena-bio/simple-app/actions/workflows/tests.yml/badge.svg)

# simple-app

Mini Docker + pytest sample.

## Run locally
pip install -r requirements.txt
pytest

## Run with Docker
docker build -t simple-python-app .
docker run --rm simple-python-app

