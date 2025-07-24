from flask import Flask, request, jsonify, render_template
import requests
import logging.config
import time
import os
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Logging config
logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger("ping_logger")

# Prometheus metrics
REQUEST_COUNT = Counter("request_count", "Total number of /ping requests")
REQUEST_LATENCY = Histogram("request_latency_seconds", "Latency for /ping request")
PING_FAILURES = Counter("ping_failures", "Failed pings")

@app.route("/")
def index():
    return render_template("ping.html")

@app.route("/ping", methods=["POST"])
def ping():
    start = time.time()
    REQUEST_COUNT.inc()

    data = request.get_json()
    url = data.get("url")
    logger.info(f"Received ping request for URL: {url}")

    try:
        response = requests.get(url, timeout=5)
        latency = time.time() - start
        REQUEST_LATENCY.observe(latency)
        logger.info(f"Ping success: {url} - {response.status_code}")
        return jsonify({"url": url, "status_code": response.status_code, "latency": latency}), 200
    except Exception as e:
        latency = time.time() - start
        REQUEST_LATENCY.observe(latency)
        PING_FAILURES.inc()
        logger.error(f"Ping failed for {url}: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

@app.route("/healthz")
def healthz():
    return "OK", 200

if __name__ == "__main__":
    os.makedirs("/logs", exist_ok=True)
    app.run(host="0.0.0.0", port=5000)
