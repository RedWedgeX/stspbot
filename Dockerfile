#FROM python:3.11-buster
FROM rust:buster

RUN mkdir /build
WORKDIR /build


RUN apt-get update && apt-get install -y wget build-essential \
    libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev \
    libbz2-dev libffi-dev zlib1g-dev

RUN wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz
RUN tar xzf Python-3.10.8.tgz

WORKDIR /build/Python-3.10.8

RUN ./configure --enable-optimizations
RUN make install

RUN apt-get install -y python3-pip
#
#
#WORKDIR /build
#
#ENV PATH="${PATH}:/root/.cargo/bin"
#RUN curl --proto '=https' --tlsv1.2 -o rust.sh -sSf https://sh.rustup.rs
#RUN chmod +x rust.sh;./rust.sh -y
## RUN apt-get update && apt-get install -y sudo nano wget curl libpq-dev gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils nano ffmpeg
#
#
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
#
WORKDIR /usr/src/app
#
COPY . .
#
CMD [ "python3", "bot.py"]
#

