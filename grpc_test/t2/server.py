#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
import time
from concurrent import futures
import helloworld_pb2, helloworld_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '50051'

class MhcTest(helloworld_pb2_grpc.MhcTestServicer):
    def Test1(self, request, context):
        str = request.name
        print str
        return helloworld_pb2.HelloReply(message=str.upper())

def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    helloworld_pb2_grpc.add_MhcTestServicer_to_server(MhcTest(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)

if __name__ == '__main__':
    serve()