# Start with the official Python image
FROM python:3.11

ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

COPY ./manage.py /app/

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY social_app /app/social_app
COPY user_management /app/user_management
COPY social_interactions /app/social_interactions

RUN python manage.py makemigrations
RUN python manage.py migrate

# Expose the localhost port
EXPOSE 8000

# Run the Django server
CMD ["python", "manage.py", "runserver"]