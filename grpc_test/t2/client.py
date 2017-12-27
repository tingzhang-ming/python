#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
import helloworld_pb2, helloworld_pb2_grpc

_HOST = 'localhost'
_PORT = '50051'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = helloworld_pb2_grpc.MhcTestStub(channel=conn)
    response = client.Test1(helloworld_pb2.HelloRequest(name='hahahahahah'))
    print("received: " + response.message)

if __name__ == '__main__':
    run()