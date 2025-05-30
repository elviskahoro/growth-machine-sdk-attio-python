"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from growth_machine_sdk_attio_python import utils
from growth_machine_sdk_attio_python.models import (
    delete_v2_lists_list_entries_entry_id_op as models_delete_v2_lists_list_entries_entry_id_op,
)
from growth_machine_sdk_attio_python.types import BaseModel


class DeleteV2ListsListEntriesEntryIDNotFoundErrorData(BaseModel):
    status_code: float

    type: models_delete_v2_lists_list_entries_entry_id_op.DeleteV2ListsListEntriesEntryIDType

    code: models_delete_v2_lists_list_entries_entry_id_op.DeleteV2ListsListEntriesEntryIDCode

    message: str


class DeleteV2ListsListEntriesEntryIDNotFoundError(Exception):
    r"""Not Found"""

    data: DeleteV2ListsListEntriesEntryIDNotFoundErrorData

    def __init__(self, data: DeleteV2ListsListEntriesEntryIDNotFoundErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, DeleteV2ListsListEntriesEntryIDNotFoundErrorData
        )
