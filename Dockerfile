FROM python:3.12.7

WORKDIR /app

COPY src /app/src
COPY requirements.txt /app/

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app/src

CMD ["python", "src/main.py"]

