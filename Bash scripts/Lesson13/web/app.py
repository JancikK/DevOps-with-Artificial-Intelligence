from flask import Flask # type: ignore
import redis # type: ignore

# Create a new Flask app
app = Flask(__name__)

# Connect to the Redis container (hostname 'redis' comes from docker-compose)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

# Define a simple web route
@app.route('/')
def home():
    # Increment the 'visits' counter each time the page is accessed
    r.incr('visits')
    # Fetch the counter value and display it
    return f"Visited {r.get('visits')} times!"

# Run the Flask development server
# host='0.0.0.0' makes it accessible from outside the container
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)