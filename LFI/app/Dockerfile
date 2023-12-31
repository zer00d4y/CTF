FROM python:3

WORKDIR /LFI

COPY app.py /LFI/app.py
COPY message /LFI/message
COPY flag.txt /LFI/flag.txt


RUN apt-get update  \
    && useradd -m ctf-player \
    && chown -R ctf-player /LFI

USER ctf-player

RUN pip install Flask

EXPOSE 4053

CMD ["python3", "app.py"]