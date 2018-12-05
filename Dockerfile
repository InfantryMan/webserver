FROM ubuntu:16.04
MAINTAINER Rustam Migranov
RUN apt-get -y update
RUN apt-get install -y python3

ADD . ./server/

EXPOSE 80

CMD python3 ./server/launch.py