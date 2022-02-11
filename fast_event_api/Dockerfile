FROM python:3.9
EXPOSE 8000
RUN pip install --upgrade pip
WORKDIR /fast_event_api
COPY requirements.txt /fast_event_api/
RUN pip install -r requirements.txt --no-cache-dir
