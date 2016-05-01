FROM python:3.3

RUN pip install pyTelegramBotAPI
RUN pip install pymongo

ADD ./ /opt/app/

CMD ["sh", "/opt/app/run.sh"]
