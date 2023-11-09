# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dcs/unit/v0/unit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dcs.common.v0 import common_pb2 as dcs_dot_common_dot_v0_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x64\x63s/unit/v0/unit.proto\x12\x0b\x64\x63s.unit.v0\x1a\x1a\x64\x63s/common/v0/common.proto\"\x1f\n\x0fGetRadarRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"I\n\x10GetRadarResponse\x12\x0e\n\x06\x61\x63tive\x18\x01 \x01(\x08\x12%\n\x06target\x18\x02 \x01(\x0b\x32\x15.dcs.common.v0.Target\"\"\n\x12GetPositionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"@\n\x13GetPositionResponse\x12)\n\x08position\x18\x01 \x01(\x0b\x32\x17.dcs.common.v0.Position\"#\n\x13GetTransformRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xa8\x01\n\x0bOrientation\x12&\n\x07\x66orward\x18\x01 \x01(\x0b\x32\x15.dcs.common.v0.Vector\x12$\n\x05right\x18\x02 \x01(\x0b\x32\x15.dcs.common.v0.Vector\x12!\n\x02up\x18\x03 \x01(\x0b\x32\x15.dcs.common.v0.Vector\x12\x0b\n\x03yaw\x18\x04 \x01(\x01\x12\r\n\x05pitch\x18\x05 \x01(\x01\x12\x0c\n\x04roll\x18\x06 \x01(\x01\"\xce\x01\n\x14GetTransformResponse\x12)\n\x08position\x18\x01 \x01(\x0b\x32\x17.dcs.common.v0.Position\x12\t\n\x01u\x18\x02 \x01(\x01\x12\t\n\x01v\x18\x03 \x01(\x01\x12\x0f\n\x07heading\x18\x04 \x01(\x01\x12-\n\x0borientation\x18\x05 \x01(\x0b\x32\x18.dcs.unit.v0.Orientation\x12\'\n\x08velocity\x18\x06 \x01(\x0b\x32\x15.dcs.common.v0.Vector\x12\x0c\n\x04time\x18\x07 \x01(\x01\"$\n\x14GetPlayerNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"A\n\x15GetPlayerNameResponse\x12\x18\n\x0bplayer_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_player_name\"$\n\x14GetDescriptorRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"+\n\x15GetDescriptorResponse\x12\x12\n\nattributes\x18\x01 \x03(\t\"4\n\x12SetEmissionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x65mitting\x18\x02 \x01(\x08\"\x15\n\x13SetEmissionResponse\"\x1a\n\nGetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"0\n\x0bGetResponse\x12!\n\x04unit\x18\x01 \x01(\x0b\x32\x13.dcs.common.v0.Unit2\xc7\x04\n\x0bUnitService\x12I\n\x08GetRadar\x12\x1c.dcs.unit.v0.GetRadarRequest\x1a\x1d.dcs.unit.v0.GetRadarResponse\"\x00\x12R\n\x0bGetPosition\x12\x1f.dcs.unit.v0.GetPositionRequest\x1a .dcs.unit.v0.GetPositionResponse\"\x00\x12X\n\rGetPlayerName\x12!.dcs.unit.v0.GetPlayerNameRequest\x1a\".dcs.unit.v0.GetPlayerNameResponse\"\x00\x12X\n\rGetDescriptor\x12!.dcs.unit.v0.GetDescriptorRequest\x1a\".dcs.unit.v0.GetDescriptorResponse\"\x00\x12R\n\x0bSetEmission\x12\x1f.dcs.unit.v0.SetEmissionRequest\x1a .dcs.unit.v0.SetEmissionResponse\"\x00\x12:\n\x03Get\x12\x17.dcs.unit.v0.GetRequest\x1a\x18.dcs.unit.v0.GetResponse\"\x00\x12U\n\x0cGetTransform\x12 .dcs.unit.v0.GetTransformRequest\x1a!.dcs.unit.v0.GetTransformResponse\"\x00\x42MZ+github.com/DCS-gRPC/go-bindings/dcs/v0/unit\xaa\x02\x1dRurouniJones.Dcs.Grpc.V0.Unitb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dcs.unit.v0.unit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/DCS-gRPC/go-bindings/dcs/v0/unit\252\002\035RurouniJones.Dcs.Grpc.V0.Unit'
  _globals['_GETRADARREQUEST']._serialized_start=67
  _globals['_GETRADARREQUEST']._serialized_end=98
  _globals['_GETRADARRESPONSE']._serialized_start=100
  _globals['_GETRADARRESPONSE']._serialized_end=173
  _globals['_GETPOSITIONREQUEST']._serialized_start=175
  _globals['_GETPOSITIONREQUEST']._serialized_end=209
  _globals['_GETPOSITIONRESPONSE']._serialized_start=211
  _globals['_GETPOSITIONRESPONSE']._serialized_end=275
  _globals['_GETTRANSFORMREQUEST']._serialized_start=277
  _globals['_GETTRANSFORMREQUEST']._serialized_end=312
  _globals['_ORIENTATION']._serialized_start=315
  _globals['_ORIENTATION']._serialized_end=483
  _globals['_GETTRANSFORMRESPONSE']._serialized_start=486
  _globals['_GETTRANSFORMRESPONSE']._serialized_end=692
  _globals['_GETPLAYERNAMEREQUEST']._serialized_start=694
  _globals['_GETPLAYERNAMEREQUEST']._serialized_end=730
  _globals['_GETPLAYERNAMERESPONSE']._serialized_start=732
  _globals['_GETPLAYERNAMERESPONSE']._serialized_end=797
  _globals['_GETDESCRIPTORREQUEST']._serialized_start=799
  _globals['_GETDESCRIPTORREQUEST']._serialized_end=835
  _globals['_GETDESCRIPTORRESPONSE']._serialized_start=837
  _globals['_GETDESCRIPTORRESPONSE']._serialized_end=880
  _globals['_SETEMISSIONREQUEST']._serialized_start=882
  _globals['_SETEMISSIONREQUEST']._serialized_end=934
  _globals['_SETEMISSIONRESPONSE']._serialized_start=936
  _globals['_SETEMISSIONRESPONSE']._serialized_end=957
  _globals['_GETREQUEST']._serialized_start=959
  _globals['_GETREQUEST']._serialized_end=985
  _globals['_GETRESPONSE']._serialized_start=987
  _globals['_GETRESPONSE']._serialized_end=1035
  _globals['_UNITSERVICE']._serialized_start=1038
  _globals['_UNITSERVICE']._serialized_end=1621
# @@protoc_insertion_point(module_scope)