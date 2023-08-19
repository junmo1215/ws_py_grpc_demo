import time
import asyncio
import threading

def loop_in_thread():
  global loop
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  loop.run_forever()

def stop_all_task():
  global loop
  loop.call_soon_threadsafe(loop.stop)
  # self.loop.close()

def async_task(task_name, delay):
  global loop
  print(f"{task_name}: Start")
  asyncio.run_coroutine_threadsafe(async_task_coroutine(task_name, delay), loop)
  print(f"{task_name}: End")

async def async_task_coroutine(task_name, delay):
  await asyncio.sleep(delay)
  print(f"{task_name}: Done")

if __name__ == "__main__":
  loop_thread = threading.Thread(target=loop_in_thread)
  loop_thread.start()

  async_task("Task 1", 2)
  async_task("Task 2", 1)

  time.sleep(5)
  stop_all_task()

  loop_thread.join()