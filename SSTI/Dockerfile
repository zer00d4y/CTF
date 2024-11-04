FROM python:3.11-slim

WORKDIR /app

RUN pip install Flask

COPY app.py .

EXPOSE 4000

CMD ["python", "app.py"]
