This are dockerfiles for Testing data pipeline that can not be created locally on Windows.

Just go to https://docs.docker.com/desktop/install/windows-install/ and install Docker Desktop for Windows.

That way you can install images and run containers in clean way not as service or manual process.

# Testing dockerfiles 

dbt-dummy is taken from project by George Myrianthous 

# Geting work tips for docker

## Howto check container id, run:
docker ps

## Attach bash to postgresql /dbt or other container




## Run docker kafka-with-zookeeper
docker-compose -f kafka-with-zookeeper.yaml up -d 

### Connect docker and see logs in Windows Sublinux
Go to wsl ( you can install it in Powershell with wsl --install)

Check if connections exist :
ZOOKEEPER_CLIENT_PORT is 22181
 
nc -vz localhost 22181
KAFKA PORT is 29092
nc -vz localhost 29092
Run:
docker-compose logs kafka | grep -i started

### Postgre docker file tips:
Get postgresql sample config file 

docker run -i --rm postgres cat /usr/share/postgresql/postgresql.conf.sample > my-postgres.conf

# run postgres with custom config
docker run -d --name postgres -v "$PWD/my-postgres.conf":/etc/postgresql/postgresql.conf -e POSTGRES_PASSWORD=example postgres -c 'config_file=/etc/postgresql/postgresql.conf'