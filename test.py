import logging

import grpc
from proto import calculator_pb2
from proto import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.CalculatorRequest(num1=1, num2=4))
    print("Greeter client received: " + response.result)


if __name__ == '__main__':
    logging.basicConfig()
    run()