# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/nodered/node-red

FROM nodered/node-red:2.2.2-12

# Copy the requirements file
COPY ./data/package.json /data/package.json
RUN cd /data && npm install

# Copy Node-RED configuration files
COPY ./data/settings.js /data/settings.js
COPY ./data/flows_cred.json /data/flows_cred.json
COPY ./data/flows.json /data/flows.json
COPY ./files/movies_list_2012-2020.csv /usr/src/node-red/movies_list_2012-2020.csv
COPY ./files/metacritic_comments_clean.csv /usr/src/node-red/metacritic_comments_clean.csv

# Copy all the utilities scripts
COPY ./scripts/linux/boot.sh /usr/src/node-red/boot.sh
COPY ./scripts/linux/install.sh /usr/src/node-red/install.sh
COPY ./scripts/linux/root.sh /usr/src/node-red/root.sh
COPY ./scripts/linux/start.sh /usr/src/node-red/start.sh


WORKDIR /usr/src/node-red