FROM python:3.10-slim
WORKDIR /app
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt
COPY backend/ ./backend
CMD ["python", "backend/app.py"]