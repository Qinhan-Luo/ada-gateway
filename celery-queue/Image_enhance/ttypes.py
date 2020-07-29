#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class ImageData:
  """
  Attributes:
   - name
   - data
   - ID
   - option
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'data', None, None, ), # 2
    (3, TType.STRING, 'ID', None, None, ), # 3
    (4, TType.STRING, 'option', None, None, ), # 4
  )

  def __init__(self, name=None, data=None, ID=None, option=None,):
    self.name = name
    self.data = data
    self.ID = ID
    self.option = option

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.data = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.ID = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.option = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ImageData')
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.data is not None:
      oprot.writeFieldBegin('data', TType.STRING, 2)
      oprot.writeString(self.data)
      oprot.writeFieldEnd()
    if self.ID is not None:
      oprot.writeFieldBegin('ID', TType.STRING, 3)
      oprot.writeString(self.ID)
      oprot.writeFieldEnd()
    if self.option is not None:
      oprot.writeFieldBegin('option', TType.STRING, 4)
      oprot.writeString(self.option)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
    if self.data is None:
      raise TProtocol.TProtocolException(message='Required field data is unset!')
    if self.ID is None:
      raise TProtocol.TProtocolException(message='Required field ID is unset!')
    if self.option is None:
      raise TProtocol.TProtocolException(message='Required field option is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.data)
    value = (value * 31) ^ hash(self.ID)
    value = (value * 31) ^ hash(self.option)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)