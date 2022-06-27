FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python-pip libmysqlclient-dev && \
    apt-get clean && \
    pip install flask
    
RUN mkdir -p /app
COPY ./ /app/
WORKDIR /app

ENTRYPOINT ["python"]

CMD ["app.py"]
