"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from growth_machine_sdk_attio_python import utils
from growth_machine_sdk_attio_python.models import (
    post_v2_listsop as models_post_v2_listsop,
)
from growth_machine_sdk_attio_python.types import BaseModel


class PostV2ListsNotFoundErrorData(BaseModel):
    status_code: float

    type: models_post_v2_listsop.PostV2ListsNotFoundType

    code: models_post_v2_listsop.PostV2ListsNotFoundCode

    message: str


class PostV2ListsNotFoundError(Exception):
    r"""Not Found"""

    data: PostV2ListsNotFoundErrorData

    def __init__(self, data: PostV2ListsNotFoundErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, PostV2ListsNotFoundErrorData)


class BillingErrorData(BaseModel):
    status_code: float

    type: models_post_v2_listsop.ForbiddenType

    code: models_post_v2_listsop.ForbiddenCode

    message: str


class BillingError(Exception):
    r"""Forbidden"""

    data: BillingErrorData

    def __init__(self, data: BillingErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, BillingErrorData)


class PostV2ListsValueNotFoundErrorData(BaseModel):
    status_code: float

    type: models_post_v2_listsop.PostV2ListsBadRequestType

    code: models_post_v2_listsop.PostV2ListsCodeValueNotFound

    message: str


class PostV2ListsValueNotFoundError(Exception):
    r"""Bad Request"""

    data: PostV2ListsValueNotFoundErrorData

    def __init__(self, data: PostV2ListsValueNotFoundErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, PostV2ListsValueNotFoundErrorData)
