# coding = UTF8

from concurrent import futures
import logging

import grpc
from proto import calculator_pb2
from proto import calculator_pb2_grpc

from src.calculator import Calculator

class CalculatorSvr(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        num1 = request.num1
        num2 = request.num2
        return calculator_pb2.CalculatorResponse(
            result=Calculator.Add(num1, num2)
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorSvr(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
