FROM python:3
WORKDIR /youtube_api
COPY requirements.txt /youtube_api/
RUN pip install -r requirements.txt
COPY ./search /youtube_api/search/
COPY ./youtube_api /youtube_api/youtube_api/
COPY ./templates /youtube_api/templates/
COPY manage.py /youtube_api/
COPY youtube_polling.py /youtube_api/
COPY run.sh /youtube_api/
