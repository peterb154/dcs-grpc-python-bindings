from dcs.common.v0 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAirbasesRequest(_message.Message):
    __slots__ = ["coalition"]
    COALITION_FIELD_NUMBER: _ClassVar[int]
    coalition: _common_pb2.Coalition
    def __init__(self, coalition: _Optional[_Union[_common_pb2.Coalition, str]] = ...) -> None: ...

class GetAirbasesResponse(_message.Message):
    __slots__ = ["airbases"]
    AIRBASES_FIELD_NUMBER: _ClassVar[int]
    airbases: _containers.RepeatedCompositeFieldContainer[_common_pb2.Airbase]
    def __init__(self, airbases: _Optional[_Iterable[_Union[_common_pb2.Airbase, _Mapping]]] = ...) -> None: ...

class GetMarkPanelsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetMarkPanelsResponse(_message.Message):
    __slots__ = ["mark_panels"]
    MARK_PANELS_FIELD_NUMBER: _ClassVar[int]
    mark_panels: _containers.RepeatedCompositeFieldContainer[_common_pb2.MarkPanel]
    def __init__(self, mark_panels: _Optional[_Iterable[_Union[_common_pb2.MarkPanel, _Mapping]]] = ...) -> None: ...

class GetTheatreRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetTheatreResponse(_message.Message):
    __slots__ = ["theatre"]
    THEATRE_FIELD_NUMBER: _ClassVar[int]
    theatre: str
    def __init__(self, theatre: _Optional[str] = ...) -> None: ...
