FROM python:3.8.10

COPY . /app

RUN pip3 install requirements.txt

WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python" ] 

CMD [ "lay.py" ]

