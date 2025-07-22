docker build -t david:v1.0 .
docker tag david:v1.0 jidoil/david:v1.0
docker login
docker push jidoil/david:v1.0
