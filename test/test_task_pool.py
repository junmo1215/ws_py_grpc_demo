# coding = UTF8

import asyncio
import concurrent.futures
import unittest
import time
from src.util.task_pool import TaskPool

class TestTaskPool(unittest.TestCase):
  # def setUp(self):
  #   self.tasks = TaskPool()
  #   self.tasks.start()

  # def tearDown(self):
  #   self.tasks.stop()

  async def _test_coroutine(self, expected_result):
    # A sample coroutine that returns a value after a delay
    print(expected_result)
    return expected_result

  def test_submit_task(self):
    # Submit a new coroutine and wait for its result
    # result = None
    # self.tasks.submit_task(self._test_coroutine("aaa"))
    # sleep_ts = 2
    # while sleep_ts > 0:
    #   time.sleep(1)
    #   sleep_ts -= 1
    tasks = TaskPool()
    tasks.start()
    tasks.run()
    time.sleep(1)
    tasks.run_async()
    time.sleep(3)
    tasks.stop()

    # coroutine = self._test_coroutine('Hello, world!')
    # future = asyncio.run_coroutine_threadsafe(self.tasks.run_task(coroutine), self.tasks.loop)
    # future.result()
    # result = future.result()

    # # Assert that the result is as expected
    # self.assertEqual(result, 'Hello, world!')
