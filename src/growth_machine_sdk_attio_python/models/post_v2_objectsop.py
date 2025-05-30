"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .object import Object, ObjectTypedDict
from enum import Enum
from growth_machine_sdk_attio_python.types import BaseModel
from typing_extensions import TypedDict


class PostV2ObjectsDataTypedDict(TypedDict):
    api_slug: str
    r"""A unique, human-readable slug to access the object through URLs and API calls. Should be formatted in snake case."""
    singular_noun: str
    r"""The singular form of the object's name."""
    plural_noun: str
    r"""The plural form of the object's name."""


class PostV2ObjectsData(BaseModel):
    api_slug: str
    r"""A unique, human-readable slug to access the object through URLs and API calls. Should be formatted in snake case."""

    singular_noun: str
    r"""The singular form of the object's name."""

    plural_noun: str
    r"""The plural form of the object's name."""


class PostV2ObjectsRequestTypedDict(TypedDict):
    data: PostV2ObjectsDataTypedDict


class PostV2ObjectsRequest(BaseModel):
    data: PostV2ObjectsData


class PostV2ObjectsType(str, Enum):
    INVALID_REQUEST_ERROR = "invalid_request_error"


class PostV2ObjectsCode(str, Enum):
    SLUG_CONFLICT = "slug_conflict"


class PostV2ObjectsResponseTypedDict(TypedDict):
    r"""Success"""

    data: ObjectTypedDict


class PostV2ObjectsResponse(BaseModel):
    r"""Success"""

    data: Object
