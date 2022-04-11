#!/bin/bash

docker build -t cripto-check .
docker-compose down
docker-compose up -d
