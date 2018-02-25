# Docker file to Store Price project

This docker is prepared to run the storeprice project. No has PostgreSQL database service. You need your our SGDB service.

### Prerequisites

Your environment to run this docker is the Docker Engine and a PostgreSQL service.

- [Docker](https://docs.docker.com/install/)
- [PostgreSQL](https://www.postgresql.org/)

### Installing

Run this command to build your image:

```
docker build -t storeprice https://github.com/andre-carvalho/storeprice.git#container:docker

```
Just run the image and your service is starting. Note that command use the set env parameters to send the database connection information for storeprice service.

* --env HOST=&lt;your ip or hostname&gt;
* --env PORT=&lt;port&gt;
* --env DBUSER=&lt;username&gt;
* --env DBPASS=&lt;secret&gt;

```
docker run --env HOST=IP --env PORT=5432 --env DBUSER=postgres --env DBPASS=postgres -d storeprice
```

Or edit the database.ini inside the docker after it is running and set your connection informations.

To procced that, you may run the docker:

```
docker run -it storeprice sh
```
And just run these commands:
```
echo "[postgresql]" > database.ini
echo "host=localhost" >> database.ini
echo "database=bitcointoyou" >> database.ini
echo "user=postgres" >> database.ini
echo "password=postgres" >> database.ini
```

