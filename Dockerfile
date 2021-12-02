FROM gorialis/discord.py:3.8.6-slim-buster-master-minimal

RUN mkdir /build
WORKDIR /build

RUN apt-get update && apt-get install -y sudo nano wget curl libpq-dev gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils nano ffmpeg


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./bot.py"]