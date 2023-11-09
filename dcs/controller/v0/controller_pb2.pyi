from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetAlarmStateRequest(_message.Message):
    __slots__ = ["group_name", "unit_name", "alarm_state"]
    class AlarmState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ALARM_STATE_UNSPECIFIED: _ClassVar[SetAlarmStateRequest.AlarmState]
        ALARM_STATE_AUTO: _ClassVar[SetAlarmStateRequest.AlarmState]
        ALARM_STATE_GREEN: _ClassVar[SetAlarmStateRequest.AlarmState]
        ALARM_STATE_RED: _ClassVar[SetAlarmStateRequest.AlarmState]
    ALARM_STATE_UNSPECIFIED: SetAlarmStateRequest.AlarmState
    ALARM_STATE_AUTO: SetAlarmStateRequest.AlarmState
    ALARM_STATE_GREEN: SetAlarmStateRequest.AlarmState
    ALARM_STATE_RED: SetAlarmStateRequest.AlarmState
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    UNIT_NAME_FIELD_NUMBER: _ClassVar[int]
    ALARM_STATE_FIELD_NUMBER: _ClassVar[int]
    group_name: str
    unit_name: str
    alarm_state: SetAlarmStateRequest.AlarmState
    def __init__(self, group_name: _Optional[str] = ..., unit_name: _Optional[str] = ..., alarm_state: _Optional[_Union[SetAlarmStateRequest.AlarmState, str]] = ...) -> None: ...

class SetAlarmStateResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
