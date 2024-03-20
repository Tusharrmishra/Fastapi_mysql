#!/bin/bash

# Start PostgreSQL container with a named volume
docker run -d \
    --name postgres \
    -e POSTGRES_PASSWORD=root \
    -p 5432:5432 \
    -v postgres_data:/var/lib/postgresql/data \
    postgres

# Start phpMyAdmin container
docker run -d \
    --name pgmyadmin \
    --link postgres:db \
    -p 8080:80 \
    phpmyadmin/phpmyadmin


docker volume create postgres_data

docker run --name postgres_container -e POSTGRES_PASSWORD=root -d -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres