FROM python:2.7.9

# hardwire some packages for caching purposes (fast repeated builds)

RUN pip install numpy
RUN pip install pandas

RUN mkdir -p /usr/src/app
COPY . /usr/src/app

WORKDIR /usr/src/app
RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]

