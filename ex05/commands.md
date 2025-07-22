docker build -t david:v1.0 .
docker run -d -p 80:80 --name david-web-app david:v1.0
curl localhost:80
docker exec -it david-web-app bash
