from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Valores(_message.Message):
    __slots__ = ("valor1", "valor2")
    VALOR1_FIELD_NUMBER: _ClassVar[int]
    VALOR2_FIELD_NUMBER: _ClassVar[int]
    valor1: float
    valor2: float
    def __init__(self, valor1: _Optional[float] = ..., valor2: _Optional[float] = ...) -> None: ...

class Resultado(_message.Message):
    __slots__ = ("resultado",)
    RESULTADO_FIELD_NUMBER: _ClassVar[int]
    resultado: float
    def __init__(self, resultado: _Optional[float] = ...) -> None: ...
