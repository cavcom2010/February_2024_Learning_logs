# Use an official Python runtime as a parent image
FROM python:3.11-bullseye

# set the working directory in the container
WORKDIR /usr/src/app

# copy the current directory contents into the container at /usr/src/app
COPY . .

# install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# make port 8000 available to the world outside this container.
EXPOSE 8000

# define environment variable
ENV DJANGO_SETTINGS_MODULE=django_project.settings

# run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
