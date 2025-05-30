"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from growth_machine_sdk_attio_python import utils
from growth_machine_sdk_attio_python.models import (
    put_v2_objects_object_recordsop as models_put_v2_objects_object_recordsop,
)
from growth_machine_sdk_attio_python.types import BaseModel


class PutV2ObjectsObjectRecordsNotFoundErrorData(BaseModel):
    status_code: float

    type: models_put_v2_objects_object_recordsop.PutV2ObjectsObjectRecordsNotFoundType

    code: models_put_v2_objects_object_recordsop.PutV2ObjectsObjectRecordsNotFoundCode

    message: str


class PutV2ObjectsObjectRecordsNotFoundError(Exception):
    r"""Not Found"""

    data: PutV2ObjectsObjectRecordsNotFoundErrorData

    def __init__(self, data: PutV2ObjectsObjectRecordsNotFoundErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, PutV2ObjectsObjectRecordsNotFoundErrorData)


class PutV2ObjectsObjectRecordsValueNotFoundErrorData(BaseModel):
    status_code: float

    type: models_put_v2_objects_object_recordsop.PutV2ObjectsObjectRecordsBadRequestType

    code: models_put_v2_objects_object_recordsop.PutV2ObjectsObjectRecordsCodeValueNotFound

    message: str


class PutV2ObjectsObjectRecordsValueNotFoundError(Exception):
    r"""Bad Request"""

    data: PutV2ObjectsObjectRecordsValueNotFoundErrorData

    def __init__(self, data: PutV2ObjectsObjectRecordsValueNotFoundErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, PutV2ObjectsObjectRecordsValueNotFoundErrorData
        )
