# coding = UTF8

import os

from src.util.singleton import SingletonType

class Config(metaclass=SingletonType):
  GRPC_PORT = int(os.getenv("GRPC_PORT", "50051"))

g_config = Config()
