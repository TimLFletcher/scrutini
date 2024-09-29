FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy your script and dependencies into the container
COPY . .

# Install any Python dependencies here
RUN pip install -r requirements.txt

# Set up environment variables
# The actual values will be passed when the container is run in GitHub Actions
ENV ANALYZERS=""
ENV OUTPUT_FORMAT="text"

# Entry point for the container
CMD ["python", "script.py", "--dir", "${INPUT_PATH}"]
