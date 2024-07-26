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
docker-compose up -d -f kafka-with-zookeeper.yaml

### Connect docker and see logs in Windows Sublinux
Go to wsl ( you can install it in Powershell with wsl --install)

ZOOKEEPER_CLIENT_PORT is 2181
nc -vz localhost 22181
KAFKA PORT is 29092
nc -vz localhost 29092
Run:
docker-compose logs kafka | grep -i started

