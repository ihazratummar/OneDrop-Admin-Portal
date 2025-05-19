# Use official Streamlit image or Python base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all app files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
