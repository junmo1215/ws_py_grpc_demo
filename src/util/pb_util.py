# coding = UTF8

from google.protobuf.json_format import MessageToJson
from google.protobuf.message import Message

class PbHelper:
  @classmethod
  def pb2str(cls, pb_message: Message) -> str:
    "PB转字符串"
    return MessageToJson(pb_message, indent=0).replace("\n", "")
