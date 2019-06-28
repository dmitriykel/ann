FROM python:3.7-alpine

RUN adduser -D ann

WORKDIR /home/ann

COPY . ./
RUN apk add gcc gfortran build-base wget freetype-dev libpng-dev openblas-dev jpeg-dev
RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN chmod +x boot.sh

ENV FLASK_APP neural_network.py

RUN chown -R ann:ann ./
USER ann

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]