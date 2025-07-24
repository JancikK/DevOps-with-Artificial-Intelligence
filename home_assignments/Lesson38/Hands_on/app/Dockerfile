# -------- Stage 1: Build dependencies --------
FROM python:3.12-alpine as builder

WORKDIR /app

# Install build tools only in this stage
RUN apk add --no-cache build-base

# Copy and install Python dependencies to a temp folder
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# -------- Stage 2: Minimal runtime image --------
FROM python:3.12-alpine

# Create a secure non-root user and group
RUN addgroup -S pinggroup && adduser -S pinguser -G pinggroup

# Set up working directory and permissions
WORKDIR /app
COPY --from=builder /install /usr/local/
COPY app.py logging.conf ./
COPY templates ./templates/
RUN mkdir /logs && chown -R pinguser:pinggroup /logs

# Use non-root user
USER pinguser

EXPOSE 5000
CMD ["python", "app.py"]
