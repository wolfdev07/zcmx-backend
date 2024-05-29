# Use a slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy your Django project code
COPY . .

# Expose port (adjust if needed)
EXPOSE 8080

# Run Gunicorn as the main process
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "src.wsgi:application"]