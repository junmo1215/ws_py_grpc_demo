# coding = UTF8

import os
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler

def config_logger(log_name: str) -> None:
  """ 配置 python 的 logging 模块并满足以下要求：
  记录日志内容到logs文件夹下面的文件中
  其中 {log_name}_{time}_{pid}_full.log 记录所有级别的日志内容
  {log_name}_{time}_{pid}_info.log 记录 INFO 级别以上的日志内容
  {time} 为当前时间，精确到分钟
  {pid} 为进程 id
  去除控制台的打印
  """
  # 获取进程 ID
  pid = os.getpid()
  time = datetime.now().strftime("%Y%m%d%H%M")

  # 设置日志文件夹路径
  logs_folder = "./logs"

  # 如果日志文件夹不存在，则创建
  if not os.path.exists(logs_folder):
    os.makedirs(logs_folder)

  # 创建 RotatingFileHandler，同时记录所有级别的日志和 INFO 级别以上的日志
  all_handler = RotatingFileHandler(
    os.path.join(logs_folder, f"{log_name}_{time}_{pid}_full.log"),
    maxBytes=1024 * 1024 * 5,
    backupCount=10
  )
  all_handler.setLevel(logging.DEBUG)

  info_handler = RotatingFileHandler(
    os.path.join(logs_folder, f"{log_name}_{time}_{pid}_info.log"),
    maxBytes=1024 * 1024 * 5,
    backupCount=10
  )
  info_handler.setLevel(logging.INFO)

  # 创建 Formatter，用于格式化日志信息
  formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

  # 设置 Formatter
  all_handler.setFormatter(formatter)
  info_handler.setFormatter(formatter)

  # 获取根 Logger，并设置 Handler
  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)
  logger.addHandler(all_handler)
  logger.addHandler(info_handler)

  # 禁用控制台输出
  logger.propagate = False
