#!/usr/bin/bash
# Script to install Nginx on a list of servers

# Represents executables that are responsible for ssh connection to the web servers
servers=("web-01" "web-02" "lb-01")

for server in "${servers[@]}"; do
    echo "Connecting to $server..."
    $server << EOF
        sudo apt update &&
        sudo apt install -y nginx &&
        exit
EOF
    echo "Nginx installed on $server"
done
