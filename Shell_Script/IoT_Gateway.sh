 docker-compose -f docker/addons/influxdb-writer/docker-compose.yml up -d
 docker-compose -f docker/docker-compose.yml -f docker/aedes.yml up -d
 docker-compose -f docker/addons/lora-adapter/docker-compose.yml up -d
 vi .bash_profile