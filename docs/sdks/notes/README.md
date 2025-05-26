# Notes
(*notes*)

## Overview

Notes are rich text documents that reference a single parent record.

### Available Operations

* [get_v2_notes](#get_v2_notes) - List notes
* [post_v2_notes](#post_v2_notes) - Create a note
* [get_v2_notes_note_id_](#get_v2_notes_note_id_) - Get a note
* [delete_v2_notes_note_id_](#delete_v2_notes_note_id_) - Delete a note

## get_v2_notes

List notes for all records or for a specific record.

Required scopes: `note:read`, `object_configuration:read`, `record_permission:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.notes.get_v2_notes(limit=10, offset=5, parent_object="people", parent_record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 10                                                                  |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 5                                                                   |
| `parent_object`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | people                                                              |
| `parent_record_id`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 891dcbfc-9141-415d-9b2a-2238a6cc012d                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2NotesResponse](../../models/getv2notesresponse.md)**

### Errors

| Error Type                     | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.GetV2NotesNotFoundError | 404                            | application/json               |
| errors.APIError                | 4XX, 5XX                       | \*/\*                          |

## post_v2_notes

Creates a new note for a given record.

Required scopes: `note:read-write`, `object_configuration:read`, `record_permission:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio, models
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.notes.post_v2_notes(data={
        "parent_object": "people",
        "parent_record_id": "891dcbfc-9141-415d-9b2a-2238a6cc012d",
        "title": "Initial Prospecting Call Summary",
        "format_": models.PostV2NotesFormat.PLAINTEXT,
        "content": ("Introduction\n"
        "Date and time of the call\n"
        "Participants\n"
        "Purpose of the call\n"
        "Customer Background\n"
        "Company overview (industry, size, location)\n"
        "Key business challenges\n"
        "Current software solutions (if any) and pain points"),
        "created_at": "2023-01-01T15:00:00.000000000Z",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data`                                                              | [models.PostV2NotesData](../../models/postv2notesdata.md)           | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostV2NotesResponse](../../models/postv2notesresponse.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.PostV2NotesNotFoundError | 404                             | application/json                |
| errors.APIError                 | 4XX, 5XX                        | \*/\*                           |

## get_v2_notes_note_id_

Get a single note by ID.

Required scopes: `note:read`, `object_configuration:read`, `record_permission:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.notes.get_v2_notes_note_id_(note_id="ff3f3bd4-40f4-4f80-8187-cd02385af424")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `note_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | ff3f3bd4-40f4-4f80-8187-cd02385af424                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2NotesNoteIDResponse](../../models/getv2notesnoteidresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GetV2NotesNoteIDNotFoundError | 404                                  | application/json                     |
| errors.APIError                      | 4XX, 5XX                             | \*/\*                                |

## delete_v2_notes_note_id_

Delete a single note by ID.

Required scopes: `note:read-write`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.notes.delete_v2_notes_note_id_(note_id="ff3f3bd4-40f4-4f80-8187-cd02385af424")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `note_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | ff3f3bd4-40f4-4f80-8187-cd02385af424                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteV2NotesNoteIDResponse](../../models/deletev2notesnoteidresponse.md)**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.DeleteV2NotesNoteIDNotFoundError | 404                                     | application/json                        |
| errors.APIError                         | 4XX, 5XX                                | \*/\*                                   |