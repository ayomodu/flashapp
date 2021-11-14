FROM python:3.8.10

COPY . /app

WORKDIR /app

RUN pip3 install requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ] 

CMD [ "lay.py" ]

