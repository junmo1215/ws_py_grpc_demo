# coding = UTF8

import asyncio
import concurrent.futures
import unittest
import time
from src.util.task_pool import TaskPool

import threading
import logging

class TestTaskPool(unittest.TestCase):
  def setUp(self):
    self.tasks = TaskPool()
    self.tasks.start()

  def tearDown(self):
    self.tasks.stop()

  def test_run_task_async(self):
    """ create a tmp_list and append some number into it with the execute order
    with the sleep pattern, most of the order can be certain
    the result should be [1, 2, 3, 4, 5] or [1, 3, 2, 4, 5]
    """
    async def async_task_coroutine(task_name, delay, tmp_list, num_pair):
      before, after = num_pair
      logging.debug(f"{task_name} start")
      tmp_list.append(before)
      await asyncio.sleep(delay)
      logging.debug(f"{task_name}: Done")
      tmp_list.append(after)

    tmp_list = []
    logging.debug("run2")
    tmp_list.append(1)
    self.tasks.run_async(async_task_coroutine("test aaa", 0.5, tmp_list, (3, 4)))
    tmp_list.append(2)
    time.sleep(1)
    logging.debug("wait end")
    tmp_list.append(5)

    logging.debug(tmp_list)
    # tmp_list should be [1, 2, 3, 4, 5] or [1, 3, 2, 4, 5]
    self.assertEqual(tmp_list[0], 1)
    self.assertEqual(tmp_list[3], 4)
    self.assertEqual(tmp_list[4], 5)

  def test_run_task_normal(self):
    async def async_task():
      logging.debug("run test_run_task_normal")
    
    self.tasks.run_async(async_task())
    time.sleep(1)

  def test_run_task_with_exception(self):
    event = threading.Event()
    exception_obj = None
    async def async_task_coroutine():
      raise Exception("The exception is raised in unittest test_run_task_with_exception, you can ignore it in unittest")

    def catch_excaption(e):
      nonlocal exception_obj
      exception_obj = e
      event.set()
      logging.debug("catch exception in unittest")

    self.tasks.run_async(async_task_coroutine(), catch_excaption)
    event.wait()
    assert exception_obj is not None
