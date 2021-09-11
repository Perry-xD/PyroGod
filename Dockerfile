FROM python:3.9

RUN apt update && apt upgrade -y
RUN apt install ffmpeg -y

RUN git clone https://github.com/Perry-xD/PyroGod.git /root/pyrogod

WORKDIR /root/pyrogod

RUN pip3 install -U -r requirements.txt

CMD ["bash", "./start.sh"]
