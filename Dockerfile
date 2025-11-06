# Step 1: Start with a clean, official Python base image
# This is our "clean kitchen" with Python 3.10 already installed.
FROM python:3.10-slim

# Step 2: Set environment variables
# These tell Python not to buffer output (so logs show up immediately)
# and not to write .pyc files, which we don't need in a container.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 3: Create and set the "working directory" inside the container
# This is where all our app code will live.
WORKDIR /app

# Step 4: Install the Python dependencies (the "ingredients")
# We copy *only* the requirements file first and install.
# Docker is smart: it caches this step. If we don't change requirements.txt,
# it won't re-install everything every time we build, which is much faster.
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Step 5: Copy the rest of your Django project code into the container
# This copies everything (your "my_project" folder, "my_app" folder, manage.py, etc.)
# from your computer's current directory into the /app directory inside the container.
COPY . /app/

# Step 6: Expose the port the app will run on
# This tells Docker that our container will listen on port 8000.
# Note: This doesn't *run* the app, it's just metadata.
EXPOSE 8000

# Step 7: Define the command to run the application
# We use Gunicorn, a production-ready web server (which you should
# add to your requirements.txt).
# We are *not* using `python manage.py runserver`, as that is
# only for development and is insecure and inefficient.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]