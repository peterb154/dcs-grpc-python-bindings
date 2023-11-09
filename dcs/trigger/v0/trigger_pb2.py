# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dcs/trigger/v0/trigger.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dcs.common.v0 import common_pb2 as dcs_dot_common_dot_v0_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x64\x63s/trigger/v0/trigger.proto\x12\x0e\x64\x63s.trigger.v0\x1a\x1a\x64\x63s/common/v0/common.proto\"H\n\x0eOutTextRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_time\x18\x02 \x01(\x05\x12\x12\n\nclear_view\x18\x03 \x01(\x08\"\x11\n\x0fOutTextResponse\"\x81\x01\n\x1aOutTextForCoalitionRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_time\x18\x02 \x01(\x05\x12\x12\n\nclear_view\x18\x03 \x01(\x08\x12+\n\tcoalition\x18\x04 \x01(\x0e\x32\x18.dcs.common.v0.Coalition\"\x1d\n\x1bOutTextForCoalitionResponse\"b\n\x16OutTextForGroupRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_time\x18\x02 \x01(\x05\x12\x12\n\nclear_view\x18\x03 \x01(\x08\x12\x10\n\x08group_id\x18\x04 \x01(\r\"\x19\n\x17OutTextForGroupResponse\"`\n\x15OutTextForUnitRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_time\x18\x02 \x01(\x05\x12\x12\n\nclear_view\x18\x03 \x01(\x08\x12\x0f\n\x07unit_id\x18\x04 \x01(\r\"\x18\n\x16OutTextForUnitResponse\"\"\n\x12GetUserFlagRequest\x12\x0c\n\x04\x66lag\x18\x01 \x01(\t\"$\n\x13GetUserFlagResponse\x12\r\n\x05value\x18\x01 \x01(\r\"1\n\x12SetUserFlagRequest\x12\x0c\n\x04\x66lag\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r\"\x15\n\x13SetUserFlagResponse\"o\n\x10MarkToAllRequest\x12\x0c\n\x04text\x18\x02 \x01(\t\x12)\n\x08position\x18\x03 \x01(\x0b\x32\x17.dcs.common.v0.Position\x12\x11\n\tread_only\x18\x04 \x01(\x08\x12\x0f\n\x07message\x18\x05 \x01(\t\"\x1f\n\x11MarkToAllResponse\x12\n\n\x02id\x18\x01 \x01(\r\"\xae\x01\n\x16MarkToCoalitionRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04text\x18\x02 \x01(\t\x12)\n\x08position\x18\x03 \x01(\x0b\x32\x17.dcs.common.v0.Position\x12+\n\tcoalition\x18\x04 \x01(\x0e\x32\x18.dcs.common.v0.Coalition\x12\x11\n\tread_only\x18\x05 \x01(\x08\x12\x0f\n\x07message\x18\x06 \x01(\t\"%\n\x17MarkToCoalitionResponse\x12\n\n\x02id\x18\x01 \x01(\r\"\x8f\x01\n\x12MarkToGroupRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04text\x18\x02 \x01(\t\x12)\n\x08position\x18\x03 \x01(\x0b\x32\x17.dcs.common.v0.Position\x12\x10\n\x08group_id\x18\x04 \x01(\r\x12\x11\n\tread_only\x18\x05 \x01(\x08\x12\x0f\n\x07message\x18\x06 \x01(\t\"!\n\x13MarkToGroupResponse\x12\n\n\x02id\x18\x01 \x01(\r\"\x1f\n\x11RemoveMarkRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x14\n\x12RemoveMarkResponse\"L\n\x10\x45xplosionRequest\x12)\n\x08position\x18\x01 \x01(\x0b\x32\x17.dcs.common.v0.Position\x12\r\n\x05power\x18\x02 \x01(\r\"\x13\n\x11\x45xplosionResponse\"\x8e\x02\n\x0cSmokeRequest\x12)\n\x08position\x18\x01 \x01(\x0b\x32\x17.dcs.common.v0.Position\x12\x36\n\x05\x63olor\x18\x02 \x01(\x0e\x32\'.dcs.trigger.v0.SmokeRequest.SmokeColor\"\x9a\x01\n\nSmokeColor\x12\x1b\n\x17SMOKE_COLOR_UNSPECIFIED\x10\x00\x12\x15\n\x11SMOKE_COLOR_GREEN\x10\x01\x12\x13\n\x0fSMOKE_COLOR_RED\x10\x02\x12\x15\n\x11SMOKE_COLOR_WHITE\x10\x03\x12\x16\n\x12SMOKE_COLOR_ORANGE\x10\x04\x12\x14\n\x10SMOKE_COLOR_BLUE\x10\x05\"\x0f\n\rSmokeResponse\"S\n\x17IlluminationBombRequest\x12)\n\x08position\x18\x01 \x01(\x0b\x32\x17.dcs.common.v0.Position\x12\r\n\x05power\x18\x02 \x01(\r\"\x1a\n\x18IlluminationBombResponse\"\x95\x02\n\x12SignalFlareRequest\x12)\n\x08position\x18\x01 \x01(\x0b\x32\x17.dcs.common.v0.Position\x12<\n\x05\x63olor\x18\x02 \x01(\x0e\x32-.dcs.trigger.v0.SignalFlareRequest.FlareColor\x12\x0f\n\x07\x61zimuth\x18\x03 \x01(\r\"\x84\x01\n\nFlareColor\x12\x1b\n\x17\x46LARE_COLOR_UNSPECIFIED\x10\x00\x12\x15\n\x11\x46LARE_COLOR_GREEN\x10\x01\x12\x13\n\x0f\x46LARE_COLOR_RED\x10\x02\x12\x15\n\x11\x46LARE_COLOR_WHITE\x10\x03\x12\x16\n\x12\x46LARE_COLOR_YELLOW\x10\x04\"\x15\n\x13SignalFlareResponse\"@\n\x05\x43olor\x12\x0b\n\x03red\x18\x01 \x01(\x01\x12\r\n\x05green\x18\x02 \x01(\x01\x12\x0c\n\x04\x62lue\x18\x03 \x01(\x01\x12\r\n\x05\x61lpha\x18\x04 \x01(\x01\"\x8c\x02\n\x12MarkupToAllRequest\x12$\n\x05shape\x18\x01 \x01(\x0e\x32\x15.dcs.trigger.v0.Shape\x12\'\n\x06points\x18\x02 \x03(\x0b\x32\x17.dcs.common.v0.Position\x12+\n\x0c\x62order_color\x18\x03 \x01(\x0b\x32\x15.dcs.trigger.v0.Color\x12)\n\nfill_color\x18\x04 \x01(\x0b\x32\x15.dcs.trigger.v0.Color\x12+\n\tline_type\x18\x05 \x01(\x0e\x32\x18.dcs.trigger.v0.LineType\x12\x11\n\tread_only\x18\x06 \x01(\x08\x12\x0f\n\x07message\x18\x07 \x01(\t\"!\n\x13MarkupToAllResponse\x12\n\n\x02id\x18\x01 \x01(\r\"\xbf\x02\n\x18MarkupToCoalitionRequest\x12$\n\x05shape\x18\x01 \x01(\x0e\x32\x15.dcs.trigger.v0.Shape\x12+\n\tcoalition\x18\x02 \x01(\x0e\x32\x18.dcs.common.v0.Coalition\x12\'\n\x06points\x18\x03 \x03(\x0b\x32\x17.dcs.common.v0.Position\x12+\n\x0c\x62order_color\x18\x04 \x01(\x0b\x32\x15.dcs.trigger.v0.Color\x12)\n\nfill_color\x18\x05 \x01(\x0b\x32\x15.dcs.trigger.v0.Color\x12+\n\tline_type\x18\x06 \x01(\x0e\x32\x18.dcs.trigger.v0.LineType\x12\x11\n\tread_only\x18\x07 \x01(\x08\x12\x0f\n\x07message\x18\x08 \x01(\t\"\'\n\x19MarkupToCoalitionResponse\x12\n\n\x02id\x18\x01 \x01(\r*\xab\x01\n\x08LineType\x12\x15\n\x11LINE_TYPE_NO_LINE\x10\x00\x12\x13\n\x0fLINE_TYPE_SOLID\x10\x01\x12\x14\n\x10LINE_TYPE_DASHED\x10\x02\x12\x14\n\x10LINE_TYPE_DOTTED\x10\x03\x12\x16\n\x12LINE_TYPE_DOT_DASH\x10\x04\x12\x17\n\x13LINE_TYPE_LONG_DASH\x10\x05\x12\x16\n\x12LINE_TYPE_TWO_DASH\x10\x06*\x95\x01\n\x05Shape\x12\x15\n\x11SHAPE_UNSPECIFIED\x10\x00\x12\x0e\n\nSHAPE_LINE\x10\x01\x12\x10\n\x0cSHAPE_CIRCLE\x10\x02\x12\x0e\n\nSHAPE_RECT\x10\x03\x12\x0f\n\x0bSHAPE_ARROW\x10\x04\x12\x0e\n\nSHAPE_TEXT\x10\x05\x12\x0e\n\nSHAPE_QUAD\x10\x06\x12\x12\n\x0eSHAPE_FREEFORM\x10\x07\x32\xdd\x0b\n\x0eTriggerService\x12L\n\x07OutText\x12\x1e.dcs.trigger.v0.OutTextRequest\x1a\x1f.dcs.trigger.v0.OutTextResponse\"\x00\x12p\n\x13OutTextForCoalition\x12*.dcs.trigger.v0.OutTextForCoalitionRequest\x1a+.dcs.trigger.v0.OutTextForCoalitionResponse\"\x00\x12\x64\n\x0fOutTextForGroup\x12&.dcs.trigger.v0.OutTextForGroupRequest\x1a\'.dcs.trigger.v0.OutTextForGroupResponse\"\x00\x12\x61\n\x0eOutTextForUnit\x12%.dcs.trigger.v0.OutTextForUnitRequest\x1a&.dcs.trigger.v0.OutTextForUnitResponse\"\x00\x12X\n\x0bGetUserFlag\x12\".dcs.trigger.v0.GetUserFlagRequest\x1a#.dcs.trigger.v0.GetUserFlagResponse\"\x00\x12X\n\x0bSetUserFlag\x12\".dcs.trigger.v0.SetUserFlagRequest\x1a#.dcs.trigger.v0.SetUserFlagResponse\"\x00\x12R\n\tMarkToAll\x12 .dcs.trigger.v0.MarkToAllRequest\x1a!.dcs.trigger.v0.MarkToAllResponse\"\x00\x12\x64\n\x0fMarkToCoalition\x12&.dcs.trigger.v0.MarkToCoalitionRequest\x1a\'.dcs.trigger.v0.MarkToCoalitionResponse\"\x00\x12X\n\x0bMarkToGroup\x12\".dcs.trigger.v0.MarkToGroupRequest\x1a#.dcs.trigger.v0.MarkToGroupResponse\"\x00\x12X\n\x0bMarkupToAll\x12\".dcs.trigger.v0.MarkupToAllRequest\x1a#.dcs.trigger.v0.MarkupToAllResponse\"\x00\x12j\n\x11MarkupToCoalition\x12(.dcs.trigger.v0.MarkupToCoalitionRequest\x1a).dcs.trigger.v0.MarkupToCoalitionResponse\"\x00\x12U\n\nRemoveMark\x12!.dcs.trigger.v0.RemoveMarkRequest\x1a\".dcs.trigger.v0.RemoveMarkResponse\"\x00\x12R\n\tExplosion\x12 .dcs.trigger.v0.ExplosionRequest\x1a!.dcs.trigger.v0.ExplosionResponse\"\x00\x12\x46\n\x05Smoke\x12\x1c.dcs.trigger.v0.SmokeRequest\x1a\x1d.dcs.trigger.v0.SmokeResponse\"\x00\x12g\n\x10IlluminationBomb\x12\'.dcs.trigger.v0.IlluminationBombRequest\x1a(.dcs.trigger.v0.IlluminationBombResponse\"\x00\x12X\n\x0bSignalFlare\x12\".dcs.trigger.v0.SignalFlareRequest\x1a#.dcs.trigger.v0.SignalFlareResponse\"\x00\x42SZ.github.com/DCS-gRPC/go-bindings/dcs/v0/trigger\xaa\x02 RurouniJones.Dcs.Grpc.V0.Triggerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dcs.trigger.v0.trigger_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z.github.com/DCS-gRPC/go-bindings/dcs/v0/trigger\252\002 RurouniJones.Dcs.Grpc.V0.Trigger'
  _globals['_LINETYPE']._serialized_start=2870
  _globals['_LINETYPE']._serialized_end=3041
  _globals['_SHAPE']._serialized_start=3044
  _globals['_SHAPE']._serialized_end=3193
  _globals['_OUTTEXTREQUEST']._serialized_start=76
  _globals['_OUTTEXTREQUEST']._serialized_end=148
  _globals['_OUTTEXTRESPONSE']._serialized_start=150
  _globals['_OUTTEXTRESPONSE']._serialized_end=167
  _globals['_OUTTEXTFORCOALITIONREQUEST']._serialized_start=170
  _globals['_OUTTEXTFORCOALITIONREQUEST']._serialized_end=299
  _globals['_OUTTEXTFORCOALITIONRESPONSE']._serialized_start=301
  _globals['_OUTTEXTFORCOALITIONRESPONSE']._serialized_end=330
  _globals['_OUTTEXTFORGROUPREQUEST']._serialized_start=332
  _globals['_OUTTEXTFORGROUPREQUEST']._serialized_end=430
  _globals['_OUTTEXTFORGROUPRESPONSE']._serialized_start=432
  _globals['_OUTTEXTFORGROUPRESPONSE']._serialized_end=457
  _globals['_OUTTEXTFORUNITREQUEST']._serialized_start=459
  _globals['_OUTTEXTFORUNITREQUEST']._serialized_end=555
  _globals['_OUTTEXTFORUNITRESPONSE']._serialized_start=557
  _globals['_OUTTEXTFORUNITRESPONSE']._serialized_end=581
  _globals['_GETUSERFLAGREQUEST']._serialized_start=583
  _globals['_GETUSERFLAGREQUEST']._serialized_end=617
  _globals['_GETUSERFLAGRESPONSE']._serialized_start=619
  _globals['_GETUSERFLAGRESPONSE']._serialized_end=655
  _globals['_SETUSERFLAGREQUEST']._serialized_start=657
  _globals['_SETUSERFLAGREQUEST']._serialized_end=706
  _globals['_SETUSERFLAGRESPONSE']._serialized_start=708
  _globals['_SETUSERFLAGRESPONSE']._serialized_end=729
  _globals['_MARKTOALLREQUEST']._serialized_start=731
  _globals['_MARKTOALLREQUEST']._serialized_end=842
  _globals['_MARKTOALLRESPONSE']._serialized_start=844
  _globals['_MARKTOALLRESPONSE']._serialized_end=875
  _globals['_MARKTOCOALITIONREQUEST']._serialized_start=878
  _globals['_MARKTOCOALITIONREQUEST']._serialized_end=1052
  _globals['_MARKTOCOALITIONRESPONSE']._serialized_start=1054
  _globals['_MARKTOCOALITIONRESPONSE']._serialized_end=1091
  _globals['_MARKTOGROUPREQUEST']._serialized_start=1094
  _globals['_MARKTOGROUPREQUEST']._serialized_end=1237
  _globals['_MARKTOGROUPRESPONSE']._serialized_start=1239
  _globals['_MARKTOGROUPRESPONSE']._serialized_end=1272
  _globals['_REMOVEMARKREQUEST']._serialized_start=1274
  _globals['_REMOVEMARKREQUEST']._serialized_end=1305
  _globals['_REMOVEMARKRESPONSE']._serialized_start=1307
  _globals['_REMOVEMARKRESPONSE']._serialized_end=1327
  _globals['_EXPLOSIONREQUEST']._serialized_start=1329
  _globals['_EXPLOSIONREQUEST']._serialized_end=1405
  _globals['_EXPLOSIONRESPONSE']._serialized_start=1407
  _globals['_EXPLOSIONRESPONSE']._serialized_end=1426
  _globals['_SMOKEREQUEST']._serialized_start=1429
  _globals['_SMOKEREQUEST']._serialized_end=1699
  _globals['_SMOKEREQUEST_SMOKECOLOR']._serialized_start=1545
  _globals['_SMOKEREQUEST_SMOKECOLOR']._serialized_end=1699
  _globals['_SMOKERESPONSE']._serialized_start=1701
  _globals['_SMOKERESPONSE']._serialized_end=1716
  _globals['_ILLUMINATIONBOMBREQUEST']._serialized_start=1718
  _globals['_ILLUMINATIONBOMBREQUEST']._serialized_end=1801
  _globals['_ILLUMINATIONBOMBRESPONSE']._serialized_start=1803
  _globals['_ILLUMINATIONBOMBRESPONSE']._serialized_end=1829
  _globals['_SIGNALFLAREREQUEST']._serialized_start=1832
  _globals['_SIGNALFLAREREQUEST']._serialized_end=2109
  _globals['_SIGNALFLAREREQUEST_FLARECOLOR']._serialized_start=1977
  _globals['_SIGNALFLAREREQUEST_FLARECOLOR']._serialized_end=2109
  _globals['_SIGNALFLARERESPONSE']._serialized_start=2111
  _globals['_SIGNALFLARERESPONSE']._serialized_end=2132
  _globals['_COLOR']._serialized_start=2134
  _globals['_COLOR']._serialized_end=2198
  _globals['_MARKUPTOALLREQUEST']._serialized_start=2201
  _globals['_MARKUPTOALLREQUEST']._serialized_end=2469
  _globals['_MARKUPTOALLRESPONSE']._serialized_start=2471
  _globals['_MARKUPTOALLRESPONSE']._serialized_end=2504
  _globals['_MARKUPTOCOALITIONREQUEST']._serialized_start=2507
  _globals['_MARKUPTOCOALITIONREQUEST']._serialized_end=2826
  _globals['_MARKUPTOCOALITIONRESPONSE']._serialized_start=2828
  _globals['_MARKUPTOCOALITIONRESPONSE']._serialized_end=2867
  _globals['_TRIGGERSERVICE']._serialized_start=3196
  _globals['_TRIGGERSERVICE']._serialized_end=4697
# @@protoc_insertion_point(module_scope)