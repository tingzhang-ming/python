#!/usr/bin/python
#-*-coding:utf-8-*-

import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)

socket.bind('tcp://*:5557')

while True:
    data = raw_input('input your data:')
    socket.send(data)