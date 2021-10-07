FROM python:3.8.10

RUN pip3 install Flask==1.1.2

COPY . /app

WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python" ] 

CMD [ "lay.py" ]

