# Use an official lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file first to utilize Docker caching
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of your application files
COPY . .

# Expose port 7860 (Hugging Face Spaces strictly look for port 7860)
EXPOSE 7860

# Run Gunicorn binding explicitly to port 7860
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:7860"]