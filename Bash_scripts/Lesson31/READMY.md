### Website Request Tool

This is a simple Python program that:
- Asks the user to enter a website URL
- Sends a GET request to the website
- Saves the response into a CSV file
- Logs results and errors to a log file
- Shows how many lines were written to the CSV

### How to Use

### 🔹 Without Docker
1. Install dependencies:
   pip install -r requirements.txt
2. Run the program:
   python website_request_tool.py

### 🔹 With Docker
1. Build the image:
   make build
2. Run the container:
   docker run -it -v ${PWD}:/app lesson31-app
    ## in the future - can be changed just to simple make run

### File Descriptions
- processor.py – Core logic (requests, CSV)
- website_request_tool.py – Program entry point
- decorators.py – Custom decorators
- logger.py – Logging helper
- requirements.txt – Python packages
- Dockerfile – Image definition
- docker-compose.yml – Docker service config
- Makefile – Docker shortcuts
- log/ – Log files folder
- output.csv – Saved website response

### Tasks Covered (From Lesson)
This program resolves the following 6 tasks:
1. **Decorator Application** – Measures and prints function execution time.
2. **File I/O** – Reads and analyzes a text/CSV file line count.
3. **Decorator with Arguments** – Adds messages before/after decorated functions.
4. **Requests Library** – Fetches data from a user-provided website.
5. **Class Decorator** – Tracks how many times class methods are called.
6. **File I/O with NumPy** – Uses NumPy to process CSV and count lines.