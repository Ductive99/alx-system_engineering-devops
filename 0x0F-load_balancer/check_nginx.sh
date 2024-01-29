#!/usr/bin/bash
# Script to check if Nginx is installed on a list of servers

# Represents executables that are responsible for ssh connection to the web servers
servers=("web-01" "web-02" "lb-01")

for server in "${servers[@]}"; do
    echo "Connecting to $server..."
    $server << EOF
        nginx -v &&
        exit
EOF
done
