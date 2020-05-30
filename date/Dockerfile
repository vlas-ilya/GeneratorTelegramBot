FROM mongo:3.2.6

VOLUME ./mongo/db/ /data/db/

VOLUME ./mongo/data/ /opt/data/

RUN cd /opt/data/

CMD ["mongod", "--smallfiles"]