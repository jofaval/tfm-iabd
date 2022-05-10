# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/nodered/node-red

FROM nodered/node-red:2.2.2-12

# Copy the requirements file
COPY ./node-red/data/package.json /data/package.json
RUN cd /data && npm install

# Copy Node-RED configuration files
COPY ./node-red/data/settings.js /data/settings.js
COPY ./node-red/data/flows_cred.json /data/flows_cred.json
COPY ./node-red/data/flows.json /data/flows.json

# Copy all the utilities scripts
COPY ./node-red/scripts/linux/boot.sh /scripts/linux/boot.sh
COPY ./node-red/scripts/linux/install.sh /scripts/linux/install.sh
COPY ./node-red/scripts/linux/root.sh /scripts/linux/root.sh
COPY ./node-red/scripts/linux/start.sh /scripts/linux/start.sh

WORKDIR /usr/src/node-red
RUN /scripts/linux/boot.sh