FROM python:3

WORKDIR /SSTI

COPY app.py /SSTI/app.py
COPY flag.txt /SSTI/flag.txt

RUN apt-get update  \
    && useradd -m ctf-player \
    && chown -R ctf-player /SSTI

USER ctf-player

RUN pip install Flask

EXPOSE 4000

CMD ["python3", "app.py"]
