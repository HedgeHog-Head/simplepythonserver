FROM python:3

COPY . /simpleapp

WORKDIR /simpleapp

RUN make install

CMD ["python", "main.py"]