# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script into the container
COPY scripts/ /app/scripts/

# Install any dependencies (if required in the future)
RUN pip install --upgrade pip

# Set the default command to run when the container starts
ENTRYPOINT ["python", "/app/scripts/find_markdown_files.py"]
