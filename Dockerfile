# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy local code to container
COPY . .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Set Render-friendly PORT (default to 8501 if not provided)
ENV PORT=8501

# Expose the port (informative)
EXPOSE 8501

# Command to run the application using the PORT environment variable
CMD sh -c "streamlit run app.py --server.port $PORT --server.address 0.0.0.0"
