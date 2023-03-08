# coding = UTF8

from src.util.env import load_env
from src.util.log import config_logger

from src.calculator import Calculator

def main():
  result = Calculator.Add(1, 2)
  print(result)

if __name__ == '__main__':
  load_env()
  config_logger("ws_py_grpc_demo_cli")
  main()
