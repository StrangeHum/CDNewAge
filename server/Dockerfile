FROM python:3.12.8

RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry install --no-root

CMD ["python", "main.py"]