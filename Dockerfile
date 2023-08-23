FROM python:3.9-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY *.py .

# Expose port 5000 for Flask app
EXPOSE 5000

# Set the Flask app environment variable
ENV FLASK_APP=app.py

# Run the Flask app with host 0.0.0.0 and port 5000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]