# Import Flask for web framework, Redis for connecting to the Redis service
from flask import Flask
import redis

# Create a Flask application instance
app = Flask(__name__)

# Create a Redis client that connects to the 'redis' container on port 6379
# decode_responses=True ensures returned values are strings, not bytes
r = redis.Redis(host='redis', port=6379, decode_responses=True)

# Define a route at the root URL '/'
@app.route('/')
def hello():
    # Increment the Redis key 'hits' by 1
    r.incr('hits')
    
    # Fetch the current value of 'hits' and return it in a message
    return f"Hello! This page has been viewed {r.get('hits')} times."

# Run the Flask app if this script is executed directly
# host='0.0.0.0' allows the app to be accessible from outside the container
if __name__ == '__main__':
    app.run(host='0.0.0.0')