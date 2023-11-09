from dcs.common.v0 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUnitsRequest(_message.Message):
    __slots__ = ["group_name", "active"]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    group_name: str
    active: bool
    def __init__(self, group_name: _Optional[str] = ..., active: bool = ...) -> None: ...

class GetUnitsResponse(_message.Message):
    __slots__ = ["units"]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    units: _containers.RepeatedCompositeFieldContainer[_common_pb2.Unit]
    def __init__(self, units: _Optional[_Iterable[_Union[_common_pb2.Unit, _Mapping]]] = ...) -> None: ...
