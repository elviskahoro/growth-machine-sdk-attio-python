"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .select_option import SelectOption, SelectOptionTypedDict
from enum import Enum
from growth_machine_sdk_attio_python.types import BaseModel
from growth_machine_sdk_attio_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
)
from typing_extensions import Annotated, TypedDict


class PostV2TargetIdentifierAttributesAttributeOptionsTarget(str, Enum):
    r"""Whether the attribute is on an object or a list."""

    OBJECTS = "objects"
    LISTS = "lists"


class PostV2TargetIdentifierAttributesAttributeOptionsDataTypedDict(TypedDict):
    title: str
    r"""The Title of the select option"""


class PostV2TargetIdentifierAttributesAttributeOptionsData(BaseModel):
    title: str
    r"""The Title of the select option"""


class PostV2TargetIdentifierAttributesAttributeOptionsRequestBodyTypedDict(TypedDict):
    data: PostV2TargetIdentifierAttributesAttributeOptionsDataTypedDict


class PostV2TargetIdentifierAttributesAttributeOptionsRequestBody(BaseModel):
    data: PostV2TargetIdentifierAttributesAttributeOptionsData


class PostV2TargetIdentifierAttributesAttributeOptionsRequestTypedDict(TypedDict):
    target: PostV2TargetIdentifierAttributesAttributeOptionsTarget
    r"""Whether the attribute is on an object or a list."""
    identifier: str
    attribute: str
    request_body: PostV2TargetIdentifierAttributesAttributeOptionsRequestBodyTypedDict


class PostV2TargetIdentifierAttributesAttributeOptionsRequest(BaseModel):
    target: Annotated[
        PostV2TargetIdentifierAttributesAttributeOptionsTarget,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Whether the attribute is on an object or a list."""

    identifier: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    attribute: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        PostV2TargetIdentifierAttributesAttributeOptionsRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class PostV2TargetIdentifierAttributesAttributeOptionsConflictType(str, Enum):
    INVALID_REQUEST_ERROR = "invalid_request_error"


class PostV2TargetIdentifierAttributesAttributeOptionsConflictCode(str, Enum):
    SLUG_CONFLICT = "slug_conflict"


class PostV2TargetIdentifierAttributesAttributeOptionsNotFoundType(str, Enum):
    INVALID_REQUEST_ERROR = "invalid_request_error"


class PostV2TargetIdentifierAttributesAttributeOptionsNotFoundCode(str, Enum):
    NOT_FOUND = "not_found"


class PostV2TargetIdentifierAttributesAttributeOptionsBadRequestType(str, Enum):
    INVALID_REQUEST_ERROR = "invalid_request_error"


class PostV2TargetIdentifierAttributesAttributeOptionsCodeValidationType(str, Enum):
    VALIDATION_TYPE = "validation_type"


class PostV2TargetIdentifierAttributesAttributeOptionsResponseTypedDict(TypedDict):
    r"""Success"""

    data: SelectOptionTypedDict


class PostV2TargetIdentifierAttributesAttributeOptionsResponse(BaseModel):
    r"""Success"""

    data: SelectOption
