#!/bin/bash

if command -v dos2unix ; then dos2unix **/* ; fi

docker-compose build --no-cache
docker-compose up -d --force-recreate

cat << EOF

------------------------------------------------
Use 'docker ps' to view running machines.
Attach to a machine using 'docker exec -it <machineName> bash'

When you are finished, stop the machines using 'sh 2_stop_docker.sh'
To delete/remove all installed docker machines, use '3_remove_all_docker_images.sh'
------------------------------------------------

EOF
