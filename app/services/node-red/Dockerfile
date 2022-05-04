# https://docs.docker.com/engine/reference/builder/
# Official doc: https://hub.docker.com/nodered/node-red

FROM nodered/node-red

# Copy package.json to the WORKDIR so npm builds all
# of your added nodes modules for Node-RED
COPY data/package.json .

# Copy _your_ Node-RED project files into place
# NOTE: This will only work if you DO NOT later mount /data as an external volume.
#       If you need to use an external volume for persistence then
#       copy your settings and flows files to that volume instead.
COPY data/settings.js /data/settings.js
COPY data/flows_cred.json /data/flows_cred.json
COPY data/flows.json /data/flows.json

COPY scripts/* scripts/*

# You should add extra nodes via your package.json file but you can also add them here:
WORKDIR /usr/src/node-red
RUN scripts/linux/boot.sh
