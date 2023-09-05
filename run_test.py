# coding = UTF8

"""
运行方法：
运行指定用例 python -m unittest test.testFileName.TestClassName
运行指定文件 python -m unittest test.testFileName
运行所有测试 python run_test.py
"""

import unittest
import logging
from src.util.env import load_env

# pylint: disable=unused-import
from test.test_task_pool import TestTaskPool
from test.test_timestamp import TestTimestamp
# pylint: enable=unused-import

def main():
  unittest.main()

if __name__ == "__main__":
  load_env()
  logging.basicConfig(level=logging.CRITICAL, format=(
    "%(asctime)s - %(levelname)s - "
    "Thread %(thread)d (%(threadName)s) - "
    "%(module)s:%(funcName)s:%(lineno)d - %(message)s"
  ))
  main()
