import redis # type: ignore
import time

# Connect to Redis container (Docker handles hostname)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

print("Worker running...")

# Continuously wait for jobs in the Redis list
while True:
    # Block and wait for up to 5 seconds for new jobs
    job = r.blpop("jobs", timeout=5)
    
    # If job received, print it
    if job:
        print("Job received:", job[1])
    
    # Optional short sleep to reduce CPU usage
    time.sleep(1)