FROM python:3.7-alpine

RUN adduser -D ada

WORKDIR /home/ada

COPY requirements.txt requirements.txt
RUN apk add gcc gfortran build-base wget freetype-dev libpng-dev openblas-dev jpeg-dev
RUN python -m venv venv
RUN venv/bin/pip install --upgrade setuptools
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY ada ada
COPY upload upload
COPY neural_network.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP neural_network.py

RUN chown -R ada:ada ./
USER ada

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]