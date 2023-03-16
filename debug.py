# coding = UTF8

import os
import grpc
from proto import calculator_pb2, calculator_pb2_grpc

from src.util.env import load_env
from src.util.log import config_logger

def grpc_debug():
  grpc_port = int(os.getenv("GRPC_PORT", "50051"))
  with grpc.insecure_channel(f"localhost:{grpc_port}") as channel:
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    response = stub.Add(calculator_pb2.CalculatorAddRequest(num1=1, num2=2))
    print(response.result)

def main():
  grpc_debug()

if __name__ == '__main__':
  load_env()
  config_logger("ws_py_grpc_demo_debug")
  main()
