"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .task import Task, TaskTypedDict
from enum import Enum
from growth_machine_sdk_attio_python.types import BaseModel
from growth_machine_sdk_attio_python.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class GetV2TasksTaskIDRequestTypedDict(TypedDict):
    task_id: str


class GetV2TasksTaskIDRequest(BaseModel):
    task_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetV2TasksTaskIDType(str, Enum):
    INVALID_REQUEST_ERROR = "invalid_request_error"


class GetV2TasksTaskIDCode(str, Enum):
    NOT_FOUND = "not_found"


class GetV2TasksTaskIDResponseTypedDict(TypedDict):
    r"""Success"""

    data: TaskTypedDict


class GetV2TasksTaskIDResponse(BaseModel):
    r"""Success"""

    data: Task
