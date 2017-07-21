#!/bin/bash

chmod +x -R .

./bof/comp.sh
./luck/comp.sh
./luck2/comp.sh

docker-compose up -d