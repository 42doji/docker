docker search python:3
docker pull python:3
docker run -itd --name mypy3 -p 80:80 python:3 bash
docker cp . mypy3:/home/
docker exec -it mypy3 bash -c "apt-get update && apt-get install -y python3-pip && pip3 install Flask" 
docker exec -it mypy3 python3 -c "/home/app.py"
docker commit mypy3 python_david
docker stop $(docker ps -aq -f ancester=python:3)
docker rm $(docker ps -aq -f ancester=python:3)
