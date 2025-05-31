# Use Alpine-based Python for a small image
FROM python:3.13-alpine

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .

# Start the Flask app
CMD ["python", "app.py"]