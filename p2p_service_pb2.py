# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: p2p_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='p2p_service.proto',
  package='p2pService',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11p2p_service.proto\x12\np2pService\"E\n\x13RegisterFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x1c\n\x14hashed_value_of_file\x18\x02 \x01(\t\"=\n\x14RegisterFileResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x15\n\rentrance_addr\x18\x02 \x01(\t\"%\n\x11LookUpFileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"Y\n\x12LookUpFileResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x1c\n\x14hashed_value_of_file\x18\x02 \x01(\t\x12\x15\n\rentrance_addr\x18\x03 \x01(\t\"/\n\x0f\x44ownloadRequest\x12\x1c\n\x14hashed_value_of_file\x18\x01 \x01(\t\"0\n\x10\x44ownloadResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x0c\n\x04\x66ile\x18\x02 \x01(\t\"#\n\x13\x41\x64\x64\x43hordNodeRequest\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\t\"&\n\x14\x41\x64\x64\x43hordNodeResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\"&\n\x16RemoveChordNodeRequest\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\t\")\n\x17RemoveChordNodeResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32\xc0\x03\n\x03P2P\x12X\n\x11rpc_register_file\x12\x1f.p2pService.RegisterFileRequest\x1a .p2pService.RegisterFileResponse\"\x00\x12S\n\x10rpc_look_up_file\x12\x1d.p2pService.LookUpFileRequest\x1a\x1e.p2pService.LookUpFileResponse\"\x00\x12K\n\x0crpc_download\x12\x1b.p2pService.DownloadRequest\x1a\x1c.p2pService.DownloadResponse\"\x00\x12Y\n\x12rpc_add_chord_node\x12\x1f.p2pService.AddChordNodeRequest\x1a .p2pService.AddChordNodeResponse\"\x00\x12\x62\n\x15rpc_remove_chord_node\x12\".p2pService.RemoveChordNodeRequest\x1a#.p2pService.RemoveChordNodeResponse\"\x00\x62\x06proto3')
)




_REGISTERFILEREQUEST = _descriptor.Descriptor(
  name='RegisterFileRequest',
  full_name='p2pService.RegisterFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='p2pService.RegisterFileRequest.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hashed_value_of_file', full_name='p2pService.RegisterFileRequest.hashed_value_of_file', index=1,
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
  serialized_start=33,
  serialized_end=102,
)


_REGISTERFILERESPONSE = _descriptor.Descriptor(
  name='RegisterFileResponse',
  full_name='p2pService.RegisterFileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='p2pService.RegisterFileResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entrance_addr', full_name='p2pService.RegisterFileResponse.entrance_addr', index=1,
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
  serialized_start=104,
  serialized_end=165,
)


_LOOKUPFILEREQUEST = _descriptor.Descriptor(
  name='LookUpFileRequest',
  full_name='p2pService.LookUpFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='p2pService.LookUpFileRequest.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=167,
  serialized_end=204,
)


_LOOKUPFILERESPONSE = _descriptor.Descriptor(
  name='LookUpFileResponse',
  full_name='p2pService.LookUpFileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='p2pService.LookUpFileResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hashed_value_of_file', full_name='p2pService.LookUpFileResponse.hashed_value_of_file', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entrance_addr', full_name='p2pService.LookUpFileResponse.entrance_addr', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=206,
  serialized_end=295,
)


_DOWNLOADREQUEST = _descriptor.Descriptor(
  name='DownloadRequest',
  full_name='p2pService.DownloadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hashed_value_of_file', full_name='p2pService.DownloadRequest.hashed_value_of_file', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=297,
  serialized_end=344,
)


_DOWNLOADRESPONSE = _descriptor.Descriptor(
  name='DownloadResponse',
  full_name='p2pService.DownloadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='p2pService.DownloadResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='p2pService.DownloadResponse.file', index=1,
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
  serialized_start=346,
  serialized_end=394,
)


_ADDCHORDNODEREQUEST = _descriptor.Descriptor(
  name='AddChordNodeRequest',
  full_name='p2pService.AddChordNodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr', full_name='p2pService.AddChordNodeRequest.addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=396,
  serialized_end=431,
)


_ADDCHORDNODERESPONSE = _descriptor.Descriptor(
  name='AddChordNodeResponse',
  full_name='p2pService.AddChordNodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='p2pService.AddChordNodeResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=433,
  serialized_end=471,
)


_REMOVECHORDNODEREQUEST = _descriptor.Descriptor(
  name='RemoveChordNodeRequest',
  full_name='p2pService.RemoveChordNodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr', full_name='p2pService.RemoveChordNodeRequest.addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=473,
  serialized_end=511,
)


_REMOVECHORDNODERESPONSE = _descriptor.Descriptor(
  name='RemoveChordNodeResponse',
  full_name='p2pService.RemoveChordNodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='p2pService.RemoveChordNodeResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=513,
  serialized_end=554,
)

DESCRIPTOR.message_types_by_name['RegisterFileRequest'] = _REGISTERFILEREQUEST
DESCRIPTOR.message_types_by_name['RegisterFileResponse'] = _REGISTERFILERESPONSE
DESCRIPTOR.message_types_by_name['LookUpFileRequest'] = _LOOKUPFILEREQUEST
DESCRIPTOR.message_types_by_name['LookUpFileResponse'] = _LOOKUPFILERESPONSE
DESCRIPTOR.message_types_by_name['DownloadRequest'] = _DOWNLOADREQUEST
DESCRIPTOR.message_types_by_name['DownloadResponse'] = _DOWNLOADRESPONSE
DESCRIPTOR.message_types_by_name['AddChordNodeRequest'] = _ADDCHORDNODEREQUEST
DESCRIPTOR.message_types_by_name['AddChordNodeResponse'] = _ADDCHORDNODERESPONSE
DESCRIPTOR.message_types_by_name['RemoveChordNodeRequest'] = _REMOVECHORDNODEREQUEST
DESCRIPTOR.message_types_by_name['RemoveChordNodeResponse'] = _REMOVECHORDNODERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterFileRequest = _reflection.GeneratedProtocolMessageType('RegisterFileRequest', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERFILEREQUEST,
  __module__ = 'p2p_service_pb2'
  # @@protoc_insertion_point(class_scope:p2pService.RegisterFileRequest)
  ))
_sym_db.RegisterMessage(RegisterFileRequest)

RegisterFileResponse = _reflection.GeneratedProtocolMessageType('RegisterFileResponse', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERFILERESPONSE,
  __module__ = 'p2p_service_pb2'
  # @@protoc_insertion_point(class_scope:p2pService.RegisterFileResponse)
  ))
_sym_db.RegisterMessage(RegisterFileResponse)

LookUpFileRequest = _reflection.GeneratedProtocolMessageType('LookUpFileRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOOKUPFILEREQUEST,
  __module__ = 'p2p_service_pb2'
  # @@protoc_insertion_point(class_scope:p2pService.LookUpFileRequest)
  ))
_sym_db.RegisterMessage(LookUpFileRequest)

LookUpFileResponse = _reflection.GeneratedProtocolMessageType('LookUpFileResponse', (_message.Message,), dict(
  DESCRIPTOR = _LOOKUPFILERESPONSE,
  __module__ = 'p2p_service_pb2'
  # @@protoc_insertion_point(class_scope:p2pService.LookUpFileResponse)
  ))
_sym_db.RegisterMessage(LookUpFileResponse)

DownloadRequest = _reflection.GeneratedProtocolMessageType('DownloadRequest', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADREQUEST,
  __module__ = 'p2p_service_pb2'
  # @@protoc_insertion_point(class_scope:p2pService.DownloadRequest)
  ))
_sym_db.RegisterMessage(DownloadRequest)

DownloadResponse = _reflection.GeneratedProtocolMessageType('DownloadResponse', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADRESPONSE,
  __module__ = 'p2p_service_pb2'
  # @@protoc_insertion_point(class_scope:p2pService.DownloadResponse)
  ))
_sym_db.RegisterMessage(DownloadResponse)

AddChordNodeRequest = _reflection.GeneratedProtocolMessageType('AddChordNodeRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDCHORDNODEREQUEST,
  __module__ = 'p2p_service_pb2'
  # @@protoc_insertion_point(class_scope:p2pService.AddChordNodeRequest)
  ))
_sym_db.RegisterMessage(AddChordNodeRequest)

AddChordNodeResponse = _reflection.GeneratedProtocolMessageType('AddChordNodeResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDCHORDNODERESPONSE,
  __module__ = 'p2p_service_pb2'
  # @@protoc_insertion_point(class_scope:p2pService.AddChordNodeResponse)
  ))
_sym_db.RegisterMessage(AddChordNodeResponse)

RemoveChordNodeRequest = _reflection.GeneratedProtocolMessageType('RemoveChordNodeRequest', (_message.Message,), dict(
  DESCRIPTOR = _REMOVECHORDNODEREQUEST,
  __module__ = 'p2p_service_pb2'
  # @@protoc_insertion_point(class_scope:p2pService.RemoveChordNodeRequest)
  ))
_sym_db.RegisterMessage(RemoveChordNodeRequest)

RemoveChordNodeResponse = _reflection.GeneratedProtocolMessageType('RemoveChordNodeResponse', (_message.Message,), dict(
  DESCRIPTOR = _REMOVECHORDNODERESPONSE,
  __module__ = 'p2p_service_pb2'
  # @@protoc_insertion_point(class_scope:p2pService.RemoveChordNodeResponse)
  ))
_sym_db.RegisterMessage(RemoveChordNodeResponse)



_P2P = _descriptor.ServiceDescriptor(
  name='P2P',
  full_name='p2pService.P2P',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=557,
  serialized_end=1005,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpc_register_file',
    full_name='p2pService.P2P.rpc_register_file',
    index=0,
    containing_service=None,
    input_type=_REGISTERFILEREQUEST,
    output_type=_REGISTERFILERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpc_look_up_file',
    full_name='p2pService.P2P.rpc_look_up_file',
    index=1,
    containing_service=None,
    input_type=_LOOKUPFILEREQUEST,
    output_type=_LOOKUPFILERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpc_download',
    full_name='p2pService.P2P.rpc_download',
    index=2,
    containing_service=None,
    input_type=_DOWNLOADREQUEST,
    output_type=_DOWNLOADRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpc_add_chord_node',
    full_name='p2pService.P2P.rpc_add_chord_node',
    index=3,
    containing_service=None,
    input_type=_ADDCHORDNODEREQUEST,
    output_type=_ADDCHORDNODERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpc_remove_chord_node',
    full_name='p2pService.P2P.rpc_remove_chord_node',
    index=4,
    containing_service=None,
    input_type=_REMOVECHORDNODEREQUEST,
    output_type=_REMOVECHORDNODERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_P2P)

DESCRIPTOR.services_by_name['P2P'] = _P2P

# @@protoc_insertion_point(module_scope)