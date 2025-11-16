FROM python:3.12-slim


RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*




WORKDIR /app

COPY . .


ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
