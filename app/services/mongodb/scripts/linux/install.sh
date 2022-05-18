  apt-get update 
  apt-get install -y dirmngr gnupg apt-transport-https software-properties-common ca-certificates curl 
  curl -fsSL https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add - 
  add-apt-repository 'deb https://repo.mongodb.org/apt/debian buster/mongodb-org/4.2 main' 
  apt-get update 
  apt-get install -y mongodb-org 
  mkdir -p /data/db 
  chmod 777 /data/db