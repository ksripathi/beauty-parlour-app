FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python-pip libmysqlclient-dev && \
    apt-get clean && \
    pip install flask flask-mysqldb
    
RUN mkdir -p /app
COPY backend/ /app/
WORKDIR /app

ENTRYPOINT ["python"]

CMD ["app.py"]
