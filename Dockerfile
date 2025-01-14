FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy model and application files
COPY predict.py .
COPY credit_scoring.pkl .

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=predict.py
ENV FLASK_ENV=production

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]