# Store Price

Reads bitcoin price from bitcointoyou API and store it into postgresql db.

### Prerequisites

Your environment to run is compound of Python to execute the service and a PostgreSQL SGDB installed and running with a database created.

- [Python 3](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)
- [libbitcointoyou](https://github.com/andre-carvalho/libbitcointoyou)

### Installing

Use Docker to test it.
Run this command to use a directory called docker in the branch container:

```
docker build -t storeprice https://github.com/andre-carvalho/storeprice.git#container:docker

```
Just run the image and your service is starting.
```
docker run -d storeprice
```

Or build your test environment to develop or production.
