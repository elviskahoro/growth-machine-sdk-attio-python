"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .workspace_member import WorkspaceMember, WorkspaceMemberTypedDict
from growth_machine_sdk_attio_python.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class GetV2WorkspaceMembersResponseTypedDict(TypedDict):
    r"""Success"""

    data: List[WorkspaceMemberTypedDict]


class GetV2WorkspaceMembersResponse(BaseModel):
    r"""Success"""

    data: List[WorkspaceMember]
