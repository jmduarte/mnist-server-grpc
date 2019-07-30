# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server-tools.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='server-tools.proto',
  package='helloworld',
  syntax='proto3',
  serialized_options=_b('\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'),
  serialized_pb=_b('\n\x12server-tools.proto\x12\nhelloworld\"\x0b\n\tNullParam\"D\n\x0b\x44\x61taMessage\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x0e\n\x06images\x18\x02 \x01(\x0c\x12\x12\n\nbatch_size\x18\x03 \x01(\x05\"\\\n\x11PredictionMessage\x12\x10\n\x08\x63omplete\x18\x01 \x01(\x08\x12\x12\n\nprediction\x18\x02 \x01(\x0c\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x12\n\ninfer_time\x18\x04 \x01(\x02\"*\n\tIDMessage\x12\x0e\n\x06new_id\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t2\xa2\x02\n\x0bMnistServer\x12H\n\x0cStartJobWait\x12\x17.helloworld.DataMessage\x1a\x1d.helloworld.PredictionMessage\"\x00\x12\x42\n\x0eStartJobNoWait\x12\x17.helloworld.DataMessage\x1a\x15.helloworld.IDMessage\"\x00\x12\x42\n\x08ProbeJob\x12\x15.helloworld.IDMessage\x1a\x1d.helloworld.PredictionMessage\"\x00\x12\x41\n\x0fRequestClientID\x12\x15.helloworld.NullParam\x1a\x15.helloworld.IDMessage\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)




_NULLPARAM = _descriptor.Descriptor(
  name='NullParam',
  full_name='helloworld.NullParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=45,
)


_DATAMESSAGE = _descriptor.Descriptor(
  name='DataMessage',
  full_name='helloworld.DataMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='helloworld.DataMessage.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='images', full_name='helloworld.DataMessage.images', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='helloworld.DataMessage.batch_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=115,
)


_PREDICTIONMESSAGE = _descriptor.Descriptor(
  name='PredictionMessage',
  full_name='helloworld.PredictionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='complete', full_name='helloworld.PredictionMessage.complete', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prediction', full_name='helloworld.PredictionMessage.prediction', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='helloworld.PredictionMessage.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='infer_time', full_name='helloworld.PredictionMessage.infer_time', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=209,
)


_IDMESSAGE = _descriptor.Descriptor(
  name='IDMessage',
  full_name='helloworld.IDMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_id', full_name='helloworld.IDMessage.new_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='helloworld.IDMessage.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=253,
)

DESCRIPTOR.message_types_by_name['NullParam'] = _NULLPARAM
DESCRIPTOR.message_types_by_name['DataMessage'] = _DATAMESSAGE
DESCRIPTOR.message_types_by_name['PredictionMessage'] = _PREDICTIONMESSAGE
DESCRIPTOR.message_types_by_name['IDMessage'] = _IDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NullParam = _reflection.GeneratedProtocolMessageType('NullParam', (_message.Message,), {
  'DESCRIPTOR' : _NULLPARAM,
  '__module__' : 'server_tools_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.NullParam)
  })
_sym_db.RegisterMessage(NullParam)

DataMessage = _reflection.GeneratedProtocolMessageType('DataMessage', (_message.Message,), {
  'DESCRIPTOR' : _DATAMESSAGE,
  '__module__' : 'server_tools_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.DataMessage)
  })
_sym_db.RegisterMessage(DataMessage)

PredictionMessage = _reflection.GeneratedProtocolMessageType('PredictionMessage', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONMESSAGE,
  '__module__' : 'server_tools_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.PredictionMessage)
  })
_sym_db.RegisterMessage(PredictionMessage)

IDMessage = _reflection.GeneratedProtocolMessageType('IDMessage', (_message.Message,), {
  'DESCRIPTOR' : _IDMESSAGE,
  '__module__' : 'server_tools_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.IDMessage)
  })
_sym_db.RegisterMessage(IDMessage)


DESCRIPTOR._options = None

_MNISTSERVER = _descriptor.ServiceDescriptor(
  name='MnistServer',
  full_name='helloworld.MnistServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=256,
  serialized_end=546,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartJobWait',
    full_name='helloworld.MnistServer.StartJobWait',
    index=0,
    containing_service=None,
    input_type=_DATAMESSAGE,
    output_type=_PREDICTIONMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartJobNoWait',
    full_name='helloworld.MnistServer.StartJobNoWait',
    index=1,
    containing_service=None,
    input_type=_DATAMESSAGE,
    output_type=_IDMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ProbeJob',
    full_name='helloworld.MnistServer.ProbeJob',
    index=2,
    containing_service=None,
    input_type=_IDMESSAGE,
    output_type=_PREDICTIONMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RequestClientID',
    full_name='helloworld.MnistServer.RequestClientID',
    index=3,
    containing_service=None,
    input_type=_NULLPARAM,
    output_type=_IDMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MNISTSERVER)

DESCRIPTOR.services_by_name['MnistServer'] = _MNISTSERVER

# @@protoc_insertion_point(module_scope)
