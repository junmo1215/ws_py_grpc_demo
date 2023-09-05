# coding = UTF8

import unittest

from src.util.error import WServiceError
from src.util.timestamp import Timestamp, Timedelta, TsType

# Usage:
# # create a timestamp with seconds (default)
# ts_s = Timestamp(num)
# # create a ts with milliseconds
# ts_ms = Timestamp(num, TsType.MILLISECONDS)

# # add timedelta with same unit but print a warning
# # using Timedelta to fix this warning
# ts2_s = ts_s + 100 # add 100 seconds
# ts2_s = ts_s + Timedelta(100) # same effect without warning
# ts2_ms = ts_ms + 100 # add 100 ms
# ts2_ms = ts_ms + Timedelta(100, TsType.MILLISECONDS)

# # compare with other ts object
# ts_s > ts_ms # it works
# ts_s > Timedelta(100) # raise error

class TestTimestamp(unittest.TestCase):
  def test_add_witherror(self):
    "timestamp can't add with timestamp"
    ts = Timestamp(1)
    ts2 = Timestamp(1)
    self.assertRaises(WServiceError, ts.__add__, ts2)

  def test_add_num(self):
    "1 seconds + 1 = 2 seconds"
    ts = Timestamp(1)
    num = 1
    ts2 = ts + num
    self.assertEqual(ts2.get_milliseconds(), 2000)

  def test_add_num2(self):
    "1 milliseconds + 1 = 2 milliseconds"
    ts = Timestamp(1, TsType.MILLISECONDS)
    num = 1
    ts2 = ts + num
    self.assertEqual(ts2.get_milliseconds(), 2)

  def test_add_timedelta(self):
    "1 seconds + 100 milliseconds = 1100 milliseconds"
    ts = Timestamp(1)
    ts2 = Timedelta(100, TsType.MILLISECONDS)
    ts3 = ts + ts2
    self.assertEqual(ts3.get_milliseconds(), 1100)

  def test_add_timedelta2(self):
    "1 milliseconds + 100 milliseconds = 101 milliseconds"
    ts = Timestamp(1, TsType.MILLISECONDS)
    ts2 = Timedelta(100, TsType.MILLISECONDS)
    ts3 = ts + ts2
    self.assertEqual(ts3.get_milliseconds(), 101)

  def test_add_timedelta3(self):
    "1 milliseconds + 1 seconds = 1001 milliseconds"
    ts = Timestamp(1, TsType.MILLISECONDS)
    ts2 = Timedelta(1, TsType.SECONDS)
    ts3 = ts + ts2
    self.assertEqual(ts3.get_milliseconds(), 1001)

  def test_add_timedelta4(self):
    "1 seconds + 1 seconds = 2000 milliseconds"
    ts = Timestamp(1, TsType.SECONDS)
    ts2 = Timedelta(1, TsType.SECONDS)
    ts3 = ts + ts2
    self.assertEqual(ts3.get_milliseconds(), 2000)

  def test_sub_num(self):
    "100 milliseconds - 100 = 0 milliseconds"
    ts = Timestamp(100, TsType.MILLISECONDS)
    ts2 = ts - 100
    self.assertEqual(ts2.get_milliseconds(), 0)

  def test_sub_num2(self):
    "100 seconds - 100 = 0 seconds"
    ts = Timestamp(100, TsType.SECONDS)
    ts2 = ts - 100
    self.assertEqual(ts2.get_milliseconds(), 0)

  def test_sub_witherror(self):
    "timestamp minus timestamp throws exception"
    ts = Timestamp(100, TsType.MILLISECONDS)
    ts2 = Timestamp(100, TsType.MILLISECONDS)
    self.assertRaises(WServiceError, ts.__sub__, ts2)

  def test_sub_timedelta1(self):
    "100 milliseconds - 100 milliseconds = 0 milliseconds"
    ts = Timestamp(100, TsType.MILLISECONDS)
    ts2 = Timedelta(100, TsType.MILLISECONDS)
    ts3 = ts - ts2
    self.assertEqual(ts3.get_milliseconds(), 0)

  def test_sub_timedelta2(self):
    "1 second - 1 millisecond = 999 seconds"
    ts = Timestamp(1, TsType.SECONDS)
    td = Timedelta(1, TsType.MILLISECONDS)
    ts2 = ts - td
    self.assertEqual(ts2.get_milliseconds(), 999)
    self.assertEqual(ts2.ts_type, TsType.MILLISECONDS)

  def test_compare1(self):
    "999 milliseconds < 1 second"
    ts = Timestamp(999, TsType.MILLISECONDS)
    ts2 = Timestamp(1, TsType.SECONDS)
    self.assertTrue(ts < ts2)

  def test_compare2(self):
    "1 second > 999 milliseconds"
    ts = Timestamp(1, TsType.SECONDS)
    ts2 = Timestamp(999, TsType.MILLISECONDS)
    self.assertTrue(ts > ts2)

  def test_compare3(self):
    "1 second == 1 second"
    ts = Timestamp(1, TsType.SECONDS)
    ts2 = Timestamp(1, TsType.SECONDS)
    self.assertTrue(ts == ts2)
  
  def test_compare4(self):
    "1 second == 1000 millisecond"
    ts = Timestamp(1, TsType.SECONDS)
    ts2 = Timestamp(1000, TsType.MILLISECONDS)
    self.assertTrue(ts == ts2)

  def test_compare5(self):
    "1 second != 1 millisecond"
    ts = Timestamp(1, TsType.SECONDS)
    ts2 = Timestamp(1, TsType.MILLISECONDS)
    self.assertTrue(ts != ts2)

  def test_negitave(self):
    "-1 second"
    ts = Timestamp(1, TsType.SECONDS)
    ts2 = -ts
    self.assertEqual(ts2.get_milliseconds(), -1000)
    self.assertEqual(ts2.ts_type, TsType.SECONDS)
