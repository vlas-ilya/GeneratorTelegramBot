docker build .
docker run -i -t -d <id>

docker-compose rm -f
docker-compose pull
docker-compose build
docker-compose up -d