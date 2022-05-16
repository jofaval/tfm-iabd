REM Moves to the infraestructure folder
call infrastructure.bat
cd ../services

REM Copy commons in all files
REM copy commons.sh /mongodb/commons.sh 
REM copy commons.sh /models/main/commons.sh 
REM copy commons.sh /mongodb/commons.sh 

copy commons.sh backend
copy commons.sh elasticsearch
copy commons.sh frontend
copy commons.sh kafka
copy commons.sh kibana
copy commons.sh logstash
copy commons.sh models/main
copy commons.sh module
copy commons.sh mongodb
copy commons.sh node-red
copy commons.sh spark
copy commons.sh zookeeper