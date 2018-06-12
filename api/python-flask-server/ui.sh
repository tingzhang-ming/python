#!/usr/bin/env bash

docker run -d --name=swagger-ui -p8081:8080 -e SWAGGER_JSON=/foo/swagger.yaml -v `pwd`/swagger_server/swagger:/foo registry.bst-1.cns.bstjpc.com:5000/swaggerapi/swagger-ui:latest