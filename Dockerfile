FROM ubuntu:14.04

RUN apt-get update
RUN apt-get upgrade -y

# compilers and basic tools
RUN apt-get install -y gfortran make gcc git-core build-essential curl wget 

# install python
RUN apt-get update
RUN apt-get install -y python2.7 python2.7-dev

# database client
# sqllite, postgresql, mysql client
RUN apt-get install -y libsqlite3-dev sqlite3 postgresql-client postgresql-client-common libpq5 libpq-dev libmysqlclient-dev

# needed for httplib2
RUN apt-get install -y libxml2-dev libxslt-dev

# distribute
RUN wget http://python-distribute.org/distribute_setup.py; python distribute_setup.py; rm -f /distribute*

# pip
# RUN wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py; python get-pip.py; rm -f /get-pip.py

ADD . /code
WORKDIR /code

RUN pip2.7 install -r requirements.txt

CMD [ "python2.7", "main.py" ]

