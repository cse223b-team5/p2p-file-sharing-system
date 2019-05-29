# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chord_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chord_service.proto',
  package='chordService',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x63hord_service.proto\x12\x0c\x63hordService\"3\n\x14\x46indSuccessorRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07pathlen\x18\x02 \x01(\x05\"=\n\x15\x46indSuccessorResponse\x12\x13\n\x0bsuccessorId\x18\x01 \x01(\x05\x12\x0f\n\x07pathlen\x18\x02 \x01(\x05\x32\x64\n\x05\x43hord\x12[\n\x0e\x66ind_successor\x12\".chordService.FindSuccessorRequest\x1a#.chordService.FindSuccessorResponse\"\x00\x62\x06proto3')
)




_FINDSUCCESSORREQUEST = _descriptor.Descriptor(
  name='FindSuccessorRequest',
  full_name='chordService.FindSuccessorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chordService.FindSuccessorRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pathlen', full_name='chordService.FindSuccessorRequest.pathlen', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=37,
  serialized_end=88,
)


_FINDSUCCESSORRESPONSE = _descriptor.Descriptor(
  name='FindSuccessorResponse',
  full_name='chordService.FindSuccessorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='successorId', full_name='chordService.FindSuccessorResponse.successorId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pathlen', full_name='chordService.FindSuccessorResponse.pathlen', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=90,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['FindSuccessorRequest'] = _FINDSUCCESSORREQUEST
DESCRIPTOR.message_types_by_name['FindSuccessorResponse'] = _FINDSUCCESSORRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FindSuccessorRequest = _reflection.GeneratedProtocolMessageType('FindSuccessorRequest', (_message.Message,), dict(
  DESCRIPTOR = _FINDSUCCESSORREQUEST,
  __module__ = 'chord_service_pb2'
  # @@protoc_insertion_point(class_scope:chordService.FindSuccessorRequest)
  ))
_sym_db.RegisterMessage(FindSuccessorRequest)

FindSuccessorResponse = _reflection.GeneratedProtocolMessageType('FindSuccessorResponse', (_message.Message,), dict(
  DESCRIPTOR = _FINDSUCCESSORRESPONSE,
  __module__ = 'chord_service_pb2'
  # @@protoc_insertion_point(class_scope:chordService.FindSuccessorResponse)
  ))
_sym_db.RegisterMessage(FindSuccessorResponse)



_CHORD = _descriptor.ServiceDescriptor(
  name='Chord',
  full_name='chordService.Chord',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=153,
  serialized_end=253,
  methods=[
  _descriptor.MethodDescriptor(
    name='find_successor',
    full_name='chordService.Chord.find_successor',
    index=0,
    containing_service=None,
    input_type=_FINDSUCCESSORREQUEST,
    output_type=_FINDSUCCESSORRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHORD)

DESCRIPTOR.services_by_name['Chord'] = _CHORD

# @@protoc_insertion_point(module_scope)
