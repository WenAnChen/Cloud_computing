google cloud functions URL：
https://us-central1-extreme-tribute-293105.cloudfunctions.net/test-request

go into the container commad:
sudo docker exec -ti container_ID bash

start Nginx by docker-compose in the background
docker-compose up -d

restart docker-compose everytime after editing any files og Nginx
docker-compose restart
