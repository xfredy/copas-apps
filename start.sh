#!/bin/bash

set -e 

service ssh start
ssh-keygen -t ed25519 -C "fredy" -f ~/.ssh/ansible -N ""
cp ~/.ssh/ansible.pub ~/.ssh/authorized_keys
ansible-playbook bootstrap.yml
ansible-playbook start.yml
cp /copas-app/index.html /noVNC/index.html

/copas-app/init.sh