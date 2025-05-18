FROM python:3.11-slim

WORKDIR /app

# Install graphviz system binary
RUN apt-get update && apt-get install -y graphviz && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p ./public

ENV FLASK_ENV=development

EXPOSE 5000

CMD ["python", "run.py"]
