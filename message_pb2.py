# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='message',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rmessage.proto\x12\x07message\"i\n\x0b\x41gentOutput\x12\x19\n\rpolicy_logits\x18\x01 \x03(\x02\x42\x02\x10\x01\x12\x12\n\x06values\x18\x02 \x03(\x02\x42\x02\x10\x01\x12\x12\n\x06\x61\x63tion\x18\x03 \x03(\x05\x42\x02\x10\x01\x12\x17\n\x0b\x61gent_state\x18\x04 \x03(\x02\x42\x02\x10\x01\"\x91\x01\n\nTransition\x12\x14\n\x08timestep\x18\x01 \x03(\x05\x42\x02\x10\x01\x12\x12\n\x06reward\x18\x02 \x03(\x02\x42\x02\x10\x01\x12\x14\n\x08\x64iscount\x18\x03 \x03(\x02\x42\x02\x10\x01\x12\x17\n\x0bobservation\x18\x04 \x03(\x02\x42\x02\x10\x01\x12*\n\x0c\x61gent_output\x18\x05 \x01(\x0b\x32\x14.message.AgentOutput\"-\n\x17InsertTrajectoryRequest\x12\x12\n\ntrajectory\x18\x01 \x01(\t\"(\n\x15InsertTrajectoryReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x12\n\x10GetParamsRequest\"5\n\x0eGetParamsReply\x12\x13\n\x0b\x66rame_count\x18\x01 \x01(\x05\x12\x0e\n\x06params\x18\x02 \x01(\t2\xa8\x01\n\x0bInformation\x12V\n\x10InsertTrajectory\x12 .message.InsertTrajectoryRequest\x1a\x1e.message.InsertTrajectoryReply\"\x00\x12\x41\n\tGetParams\x12\x19.message.GetParamsRequest\x1a\x17.message.GetParamsReply\"\x00\x62\x06proto3'
)




_AGENTOUTPUT = _descriptor.Descriptor(
  name='AgentOutput',
  full_name='message.AgentOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy_logits', full_name='message.AgentOutput.policy_logits', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='message.AgentOutput.values', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='message.AgentOutput.action', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent_state', full_name='message.AgentOutput.agent_state', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
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
  serialized_start=26,
  serialized_end=131,
)


_TRANSITION = _descriptor.Descriptor(
  name='Transition',
  full_name='message.Transition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestep', full_name='message.Transition.timestep', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='message.Transition.reward', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discount', full_name='message.Transition.discount', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observation', full_name='message.Transition.observation', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent_output', full_name='message.Transition.agent_output', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=134,
  serialized_end=279,
)


_INSERTTRAJECTORYREQUEST = _descriptor.Descriptor(
  name='InsertTrajectoryRequest',
  full_name='message.InsertTrajectoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trajectory', full_name='message.InsertTrajectoryRequest.trajectory', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=281,
  serialized_end=326,
)


_INSERTTRAJECTORYREPLY = _descriptor.Descriptor(
  name='InsertTrajectoryReply',
  full_name='message.InsertTrajectoryReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='message.InsertTrajectoryReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=328,
  serialized_end=368,
)


_GETPARAMSREQUEST = _descriptor.Descriptor(
  name='GetParamsRequest',
  full_name='message.GetParamsRequest',
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
  serialized_start=370,
  serialized_end=388,
)


_GETPARAMSREPLY = _descriptor.Descriptor(
  name='GetParamsReply',
  full_name='message.GetParamsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_count', full_name='message.GetParamsReply.frame_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='message.GetParamsReply.params', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=390,
  serialized_end=443,
)

_TRANSITION.fields_by_name['agent_output'].message_type = _AGENTOUTPUT
DESCRIPTOR.message_types_by_name['AgentOutput'] = _AGENTOUTPUT
DESCRIPTOR.message_types_by_name['Transition'] = _TRANSITION
DESCRIPTOR.message_types_by_name['InsertTrajectoryRequest'] = _INSERTTRAJECTORYREQUEST
DESCRIPTOR.message_types_by_name['InsertTrajectoryReply'] = _INSERTTRAJECTORYREPLY
DESCRIPTOR.message_types_by_name['GetParamsRequest'] = _GETPARAMSREQUEST
DESCRIPTOR.message_types_by_name['GetParamsReply'] = _GETPARAMSREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AgentOutput = _reflection.GeneratedProtocolMessageType('AgentOutput', (_message.Message,), {
  'DESCRIPTOR' : _AGENTOUTPUT,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.AgentOutput)
  })
_sym_db.RegisterMessage(AgentOutput)

Transition = _reflection.GeneratedProtocolMessageType('Transition', (_message.Message,), {
  'DESCRIPTOR' : _TRANSITION,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.Transition)
  })
_sym_db.RegisterMessage(Transition)

InsertTrajectoryRequest = _reflection.GeneratedProtocolMessageType('InsertTrajectoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _INSERTTRAJECTORYREQUEST,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.InsertTrajectoryRequest)
  })
_sym_db.RegisterMessage(InsertTrajectoryRequest)

InsertTrajectoryReply = _reflection.GeneratedProtocolMessageType('InsertTrajectoryReply', (_message.Message,), {
  'DESCRIPTOR' : _INSERTTRAJECTORYREPLY,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.InsertTrajectoryReply)
  })
_sym_db.RegisterMessage(InsertTrajectoryReply)

GetParamsRequest = _reflection.GeneratedProtocolMessageType('GetParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPARAMSREQUEST,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.GetParamsRequest)
  })
_sym_db.RegisterMessage(GetParamsRequest)

GetParamsReply = _reflection.GeneratedProtocolMessageType('GetParamsReply', (_message.Message,), {
  'DESCRIPTOR' : _GETPARAMSREPLY,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.GetParamsReply)
  })
_sym_db.RegisterMessage(GetParamsReply)


_AGENTOUTPUT.fields_by_name['policy_logits']._options = None
_AGENTOUTPUT.fields_by_name['values']._options = None
_AGENTOUTPUT.fields_by_name['action']._options = None
_AGENTOUTPUT.fields_by_name['agent_state']._options = None
_TRANSITION.fields_by_name['timestep']._options = None
_TRANSITION.fields_by_name['reward']._options = None
_TRANSITION.fields_by_name['discount']._options = None
_TRANSITION.fields_by_name['observation']._options = None

_INFORMATION = _descriptor.ServiceDescriptor(
  name='Information',
  full_name='message.Information',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=446,
  serialized_end=614,
  methods=[
  _descriptor.MethodDescriptor(
    name='InsertTrajectory',
    full_name='message.Information.InsertTrajectory',
    index=0,
    containing_service=None,
    input_type=_INSERTTRAJECTORYREQUEST,
    output_type=_INSERTTRAJECTORYREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetParams',
    full_name='message.Information.GetParams',
    index=1,
    containing_service=None,
    input_type=_GETPARAMSREQUEST,
    output_type=_GETPARAMSREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INFORMATION)

DESCRIPTOR.services_by_name['Information'] = _INFORMATION

# @@protoc_insertion_point(module_scope)
