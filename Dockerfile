FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x /app/docker-entrypoint.sh && adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
CMD ["/app/docker-entrypoint.sh"]