FROM python:3.6-alpine

LABEL maintainer="afacarvalho@yahoo.com.br"

WORKDIR /usr/local

# Clone the storeprice
RUN git clone https://github.com/andre-carvalho/storeprice.git && \
    pip install -r storeprice/requirements.txt

# Clone the bitcointoyou library
RUN cd storeprice/  && \
    git clone https://github.com/andre-carvalho/libbitcointoyou.git

# Create the database config parameters from example file
RUN cp database.ini.example database.ini

WORKDIR /usr/local/bitcointoyou

# Start storeprice service
CMD ["python", "storeprice.py"]