# coding = UTF8

import logging
import asyncio
import concurrent.futures
import threading

class TaskRunner:
  def __init__(self):
    self.loop = asyncio.new_event_loop()

  def run_async(self, coroutine, exception_callback=None):
    """ run a task async, the task is a coroutine
    can simple use it like the following:
    ``` py
    async def test():
      print("async func begin")
      await asyncio.sleep(1)
      print("async func end")
    
    run_async(test())
    ```

    with exception catch:
    
    ``` py
    def exception_handler(e):
        print("catch an exception", e)
    
    run_async(test(), exception_handler)
    ```
    """
    async def _warapper(coroutine):
      try:
        await coroutine
      except Exception as e:
        logging.error("TaskRunner encounter an exception when execute corountine: %s", e)
        # print(e, stack_info=True, stderr=True)
        # the following statement is running in the loop thread also, maybe can consider deleving it into the origin threadd
        if exception_callback is not None:
          exception_callback(e)
    asyncio.run_coroutine_threadsafe(_warapper(coroutine), self.loop)
    # future = asyncio.run_coroutine_threadsafe(_warapper(coroutine), self.loop)
    # future.result()

  def start(self):
    # start should run in a single thread, so that the event loop and it's task can also in this thread
    asyncio.set_event_loop(self.loop)
    self.loop.run_forever()

  def destroy(self):
    self.loop.call_soon_threadsafe(self.loop.stop)
    # self.loop.close()

class TaskPool:
  def __init__(self) -> None:
    self.task_runner = TaskRunner()
    self.task_thread = threading.Thread(target=self.task_runner.start)

  def start(self):
    self.task_thread.start()

  def stop(self):
    # Optionally, wait for the tasks to complete and then destroy the runner
    self.task_runner.destroy()
    self.task_thread.join()

  def run_async(self, coroutine, exception_callback=None):
    self.task_runner.run_async(coroutine, exception_callback)
