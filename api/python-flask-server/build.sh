#!/usr/bin/env bash

image=registry.bst-1.cns.bstjpc.com:5000/mhc/bms-python:180610

docker build --build-arg http_proxy=http://109.105.4.159:9527 --build-arg https_proxy=http://109.105.4.159:9527 -t ${image} .

#docker push ${image}