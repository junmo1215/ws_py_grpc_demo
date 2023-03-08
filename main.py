# coding = UTF8

from concurrent import futures
import logging

import os
import grpc
from proto import calculator_pb2, calculator_pb2_grpc

from src.util.env import load_env
from src.util.log import config_logger
from src.util.error import catch_inner_error_wrapper

from src.calculator import Calculator

class CalculatorSvr(calculator_pb2_grpc.CalculatorServicer):
  @catch_inner_error_wrapper(calculator_pb2.CalculatorAddResponse)
  def Add(self, request, context):
    num1 = request.num1
    num2 = request.num2
    return calculator_pb2.CalculatorAddResponse(
      result=Calculator.Add(num1, num2)
    )

def serve():
  grpc_port = os.getenv("GRPC_PORT", 50051)
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorSvr(), server)
  server.add_insecure_port(f'[::]:{grpc_port}')
  server.start()
  logging.info("gRPC server started")
  server.wait_for_termination()

if __name__ == '__main__':
  load_env()
  config_logger("ws_py_grpc_demo")
  serve()
