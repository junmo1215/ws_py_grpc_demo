# coding = UTF8

import logging
import asyncio
import concurrent.futures
import threading

# class TaskPool:
#   def __init__(self, max_workers=2):
#     self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)
#     self.loop = asyncio.new_event_loop()

#     self.stop_flag = threading.Event()

#   def start(self):
#     # Start the event loop in a separate thread
#     self.t = threading.Thread(target=self._run_loop)
#     self.t.start()
#     # self.loop.run_forever()

#   def stop(self):
#     # Stop the event loop
#     self.loop.stop()
#     self.loop.close()
#     self.executor.shutdown(wait=False)

#   def run_task(self, coro):
#     return self.loop.run_in_executor(self.executor, asyncio.ensure_future, coro)

#   async def run_task_async(self, coro):
#     return await self.run_task(coro)

#   def _run_loop(self):

#     # Run the event loop until stopped
#     self.loop.run_forever()

class TaskRunner:
    def __init__(self):
        self.loop = asyncio.new_event_loop()
        self.tasks = []

    def run_async(self, coroutine):
        task = self.loop.create_task(coroutine)
        self.tasks.append(task)
        # asyncio.gather(*self.tasks)
        self.loop.run(coroutine)

    def run(self, function):
        return function()

    def start(self):
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

    def run_async(self):
        # def async_task():
        async def print_async():
            logging.debug("Async task: Start")
            # await asyncio.sleep(1)
            logging.debug("Async task: End")
        self.task_runner.run_async(print_async())

    def run(self):
        def sync_task():
            logging.debug("Sync task: Start")
            result = 1 + 1
            logging.debug(f"Sync task: Result = {result}")
            logging.debug("Sync task: End")
        self.task_runner.run(sync_task)

