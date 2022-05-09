apt-get update
apt-get install -y openssh-server sudo nano iputils-ping
useradd -ms /bin/bash admin
passwd -d admin
usermod -aG sudo admin