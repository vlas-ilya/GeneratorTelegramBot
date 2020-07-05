FROM mongo:3.2.6

COPY ./mongo/data/ /opt/data/

RUN cd /opt/data/ && \
    mongod --fork --syslog --smallfiles && \
    sh run.sh

CMD ["mongod", "--smallfiles"]
