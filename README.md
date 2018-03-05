# Docker file to Store Price project

This docker is prepared to run the storeprice project. No has PostgreSQL database service. You need your our SGDB service.

### Prerequisites

Your environment to run this docker is the Docker Engine and a PostgreSQL service.

- [Docker](https://docs.docker.com/install/)
- [PostgreSQL](https://www.postgresql.org/)

### Installing

#### Build your image

Run this command to build your image:

```sh
docker build -t storeprice https://github.com/andre-carvalho/storeprice.git#container:docker

```

#### Run the container

Just run the image and your service is starting. Note that command use the set env parameters to send the database connection information for storeprice service.

* --env HOST=&lt;your ip or hostname&gt;
* --env PORT=&lt;port&gt;
* --env DBUSER=&lt;username&gt;
* --env DBPASS=&lt;secret&gt;
* --env DBNAME=&lt;database name&gt;

```sh
docker run --env HOST=IP --env PORT=5432 --env DBNAME=bitcointoyou --env DBUSER=postgres --env DBPASS=postgres -d storeprice
```

You may run with less parameters, like this:

```sh
docker run --env HOST=IP --env DBNAME=dbname --env DBPASS=postgres -d storeprice
```

Or run docker accessing the terminal and set your connection informations.

To procced that, you may run the docker:

```sh
docker run -it storeprice sh
```
And just run these commands to create the database.ini file setting your values:
```sh
echo "[postgresql]" > database.ini
echo "host=localhost" >> database.ini
echo "port=5432" >> database.ini
echo "database=bitcointoyou" >> database.ini
echo "user=postgres" >> database.ini
echo "password=postgres" >> database.ini
```

### Run the container changing the sampler time between each request

Changing the sampler time via env var too. Adding the SAMPLE_TIME into run docker command:

* --env SAMPLE_TIME=&lt;time in seconds&gt;

```sh
docker run --env HOST=IP --env SAMPLE_TIME=30 --env DBNAME=bitcointoyou -d storeprice
```
