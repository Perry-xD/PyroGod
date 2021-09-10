FROM python:3.9

RUN apt update && apt upgrade -y
RUN apt install ffmpeg -y

RUN git clone https://github.com/Perry-xD/PyroGod.git /root/PyroGod

WORKDIR /root/PyroGod

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "./start.sh"]
