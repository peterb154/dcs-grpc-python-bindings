# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dcs/world/v0/world.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dcs.common.v0 import common_pb2 as dcs_dot_common_dot_v0_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x64\x63s/world/v0/world.proto\x12\x0c\x64\x63s.world.v0\x1a\x1a\x64\x63s/common/v0/common.proto\"A\n\x12GetAirbasesRequest\x12+\n\tcoalition\x18\x01 \x01(\x0e\x32\x18.dcs.common.v0.Coalition\"?\n\x13GetAirbasesResponse\x12(\n\x08\x61irbases\x18\x01 \x03(\x0b\x32\x16.dcs.common.v0.Airbase\"\x16\n\x14GetMarkPanelsRequest\"F\n\x15GetMarkPanelsResponse\x12-\n\x0bmark_panels\x18\x01 \x03(\x0b\x32\x18.dcs.common.v0.MarkPanel\"\x13\n\x11GetTheatreRequest\"%\n\x12GetTheatreResponse\x12\x0f\n\x07theatre\x18\x01 \x01(\t2\x93\x02\n\x0cWorldService\x12T\n\x0bGetAirbases\x12 .dcs.world.v0.GetAirbasesRequest\x1a!.dcs.world.v0.GetAirbasesResponse\"\x00\x12Z\n\rGetMarkPanels\x12\".dcs.world.v0.GetMarkPanelsRequest\x1a#.dcs.world.v0.GetMarkPanelsResponse\"\x00\x12Q\n\nGetTheatre\x12\x1f.dcs.world.v0.GetTheatreRequest\x1a .dcs.world.v0.GetTheatreResponse\"\x00\x42OZ,github.com/DCS-gRPC/go-bindings/dcs/v0/world\xaa\x02\x1eRurouniJones.Dcs.Grpc.V0.Worldb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dcs.world.v0.world_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/DCS-gRPC/go-bindings/dcs/v0/world\252\002\036RurouniJones.Dcs.Grpc.V0.World'
  _globals['_GETAIRBASESREQUEST']._serialized_start=70
  _globals['_GETAIRBASESREQUEST']._serialized_end=135
  _globals['_GETAIRBASESRESPONSE']._serialized_start=137
  _globals['_GETAIRBASESRESPONSE']._serialized_end=200
  _globals['_GETMARKPANELSREQUEST']._serialized_start=202
  _globals['_GETMARKPANELSREQUEST']._serialized_end=224
  _globals['_GETMARKPANELSRESPONSE']._serialized_start=226
  _globals['_GETMARKPANELSRESPONSE']._serialized_end=296
  _globals['_GETTHEATREREQUEST']._serialized_start=298
  _globals['_GETTHEATREREQUEST']._serialized_end=317
  _globals['_GETTHEATRERESPONSE']._serialized_start=319
  _globals['_GETTHEATRERESPONSE']._serialized_end=356
  _globals['_WORLDSERVICE']._serialized_start=359
  _globals['_WORLDSERVICE']._serialized_end=634
# @@protoc_insertion_point(module_scope)
