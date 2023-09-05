# coding = UTF8

from enum import Enum
import logging
from typing import Union

from src.util.error import WServiceError, ErrorCode

"""
Usage:
# create a timestamp with seconds (default)
ts_s = Timestamp(num)
# create a ts with milliseconds
ts_ms = Timestamp(num, TsType.MILLISECONDS)

# add timedelta with same unit but print a warning
# using Timedelta to fix this warning
ts2_s = ts_s + 100 # add 100 seconds
ts2_s = ts_s + Timedelta(100) # same effect without warning
ts2_ms = ts_ms + 100 # add 100 ms
ts2_ms = ts_ms + Timedelta(100, TsType.MILLISECONDS)

# compare with other ts object
ts_s > ts_ms # it works
ts_s > Timedelta(100) # raise error
"""

class TsType(Enum):
  SECONDS = 1
  MILLISECONDS = 2

class Timedelta:
  def __init__(self, num: int, ts_type: TsType = TsType.SECONDS) -> None:
    self.num = num
    self.ts_type = ts_type
  
  def get_milliseconds(self) -> int:
    if self.ts_type == TsType.SECONDS:
      return self.num * 1000
    elif self.ts_type == TsType.MILLISECONDS:
      return self.num
    raise WServiceError(ErrorCode.INTERNAL, 'Unknown ts type')

  def __neg__(self):
    return Timedelta(-self.num, self.ts_type)

class Timestamp:
  def __init__(self, num: int, ts_type: TsType = TsType.SECONDS) -> None:
    self.num = num
    self.ts_type = ts_type

  def get_milliseconds(self) -> int:
    if self.ts_type == TsType.SECONDS:
      return self.num * 1000
    elif self.ts_type == TsType.MILLISECONDS:
      return self.num
    raise WServiceError(ErrorCode.INTERNAL, 'Unknown ts type')

  def _add_number(self, num: int) -> 'Timestamp':
    logging.warning('Add number to timestamp might make some mistake, as the unit of number is not clear. Please use Timedelta to avoid any confuse.')
    return Timestamp(self.num + num, ts_type=self.ts_type)

  def _add_timedelta(self, td: 'Timedelta') -> 'Timestamp':
    if self.ts_type == TsType.SECONDS and td.ts_type == TsType.SECONDS:
      return Timestamp(self.num + td.num, ts_type=TsType.SECONDS)
    return Timestamp(self.get_milliseconds() + td.get_milliseconds(), ts_type=TsType.MILLISECONDS)

  def __add__(self, other: Union[int, 'Timedelta']) -> 'Timestamp':
    if isinstance(other, int):
      return self._add_number(other)
    elif isinstance(other, Timedelta):
      return self._add_timedelta(other)
    else:
      raise WServiceError(ErrorCode.INVALID_ARGUMENT, 'unsupported operand type(s) for +: \'Timestamp\' and \'' + str(type(other)) + '\'')

  def __sub__(self, other: Union[int, 'Timedelta']) -> 'Timestamp':
    if isinstance(other, int):
      return self._add_number(-other)
    elif isinstance(other, Timedelta):
      return self._add_timedelta(-other)
    else:
      raise WServiceError(ErrorCode.INVALID_ARGUMENT, 'unsupported operand type(s) for -: \'Timestamp\' and \'' + str(type(other)) + '\'')

  def __gt__(self, other: 'Timestamp') -> bool:
    if not isinstance(other, Timestamp):
      raise WServiceError(ErrorCode.INVALID_ARGUMENT, 'unsupported operand type(s) for >: \'Timestamp\' and \'' + str(type(other)) + '\'')
    return self.get_milliseconds() > other.get_milliseconds()

  def __ge__(self, other: 'Timestamp') -> bool:
    if not isinstance(other, Timestamp):
      raise WServiceError(ErrorCode.INVALID_ARGUMENT, 'unsupported operand type(s) for >=: \'Timestamp\' and \'' + str(type(other)) + '\'')
    return self.get_milliseconds() >= other.get_milliseconds()

  def __lt__(self, other: 'Timestamp') -> bool:
    if not isinstance(other, Timestamp):
      raise WServiceError(ErrorCode.INVALID_ARGUMENT, 'unsupported operand type(s) for <: \'Timestamp\' and \'' + str(type(other)) + '\'')
    return self.get_milliseconds() < other.get_milliseconds()

  def __le__(self, other: 'Timestamp') -> bool:
    if not isinstance(other, Timestamp):
      raise WServiceError(ErrorCode.INVALID_ARGUMENT, 'unsupported operand type(s) for <=: \'Timestamp\' and \'' + str(type(other)) + '\'')
    return self.get_milliseconds() <= other.get_milliseconds()

  def __eq__(self, other: 'Timestamp') -> bool:
    if not isinstance(other, Timestamp):
      raise WServiceError(ErrorCode.INVALID_ARGUMENT, 'unsupported operand type(s) for ==: \'Timestamp\' and \'' + str(type(other)) + '\'')
    return self.get_milliseconds() == other.get_milliseconds()

  def __ne__(self, other: 'Timestamp') -> bool:
    if not isinstance(other, Timestamp):
      raise WServiceError(ErrorCode.INVALID_ARGUMENT, 'unsupported operand type(s) for !=: \'Timestamp\' and \'' + str(type(other)) + '\'')
    return self.get_milliseconds() != other.get_milliseconds()

  def __neg__(self):
    return Timestamp(-self.num, self.ts_type)
