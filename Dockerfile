FROM python:3.9

# Allow statements and log messages to immediately appear in the Cloud Run logs
ENV PYTHONUNBUFFERED True

COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy local code to the container image.
ENV APP_HOME /myapp
WORKDIR $APP_HOME
COPY . ./

CMD exec gunicorn \
 --bind :$PORT \
 --worker-class "sync" \
 --workers 1 \
 --threads 1 \
 --timeout 0 \
 main:app
