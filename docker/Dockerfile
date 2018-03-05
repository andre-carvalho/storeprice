FROM python:3.6-alpine

LABEL maintainer="afacarvalho@yahoo.com.br"

RUN apk upgrade
RUN apk add --no-cache --update \
    git \
    gcc \
    python-dev \
    musl-dev \
    postgresql-dev \
    tzdata

ENV TZ=America/Sao_Paulo

WORKDIR /usr/local

# Clone the storeprice
RUN git clone https://github.com/andre-carvalho/storeprice.git && \
    pip install -r storeprice/requirements.txt

# Clone the bitcointoyou library
RUN cd storeprice/  && \
    git clone https://github.com/andre-carvalho/libbitcointoyou.git

WORKDIR /usr/local/storeprice

# Start storeprice service
CMD ["python", "storeprice.py"]
