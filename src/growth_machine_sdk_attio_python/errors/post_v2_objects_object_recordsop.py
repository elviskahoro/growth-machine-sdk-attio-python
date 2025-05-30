"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from growth_machine_sdk_attio_python import utils
from growth_machine_sdk_attio_python.models import (
    post_v2_objects_object_recordsop as models_post_v2_objects_object_recordsop,
)
from growth_machine_sdk_attio_python.types import BaseModel


class PostV2ObjectsObjectRecordsNotFoundErrorData(BaseModel):
    status_code: float

    type: models_post_v2_objects_object_recordsop.PostV2ObjectsObjectRecordsNotFoundType

    code: models_post_v2_objects_object_recordsop.PostV2ObjectsObjectRecordsNotFoundCode

    message: str


class PostV2ObjectsObjectRecordsNotFoundError(Exception):
    r"""Not Found"""

    data: PostV2ObjectsObjectRecordsNotFoundErrorData

    def __init__(self, data: PostV2ObjectsObjectRecordsNotFoundErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, PostV2ObjectsObjectRecordsNotFoundErrorData
        )


class PostV2ObjectsObjectRecordsValueNotFoundErrorData(BaseModel):
    status_code: float

    type: (
        models_post_v2_objects_object_recordsop.PostV2ObjectsObjectRecordsBadRequestType
    )

    code: models_post_v2_objects_object_recordsop.PostV2ObjectsObjectRecordsCodeValueNotFound

    message: str


class PostV2ObjectsObjectRecordsValueNotFoundError(Exception):
    r"""Bad Request"""

    data: PostV2ObjectsObjectRecordsValueNotFoundErrorData

    def __init__(self, data: PostV2ObjectsObjectRecordsValueNotFoundErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, PostV2ObjectsObjectRecordsValueNotFoundErrorData
        )
