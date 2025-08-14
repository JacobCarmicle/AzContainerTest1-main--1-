FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY event_job.py .
# Default command (can be overridden in the job)
CMD ["python", "event_job.py"]
