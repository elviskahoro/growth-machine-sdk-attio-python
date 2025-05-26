# Tasks
(*tasks*)

## Overview

A task is a defined, actionable item with references to linked records and assigned workspace members.

### Available Operations

* [get_v2_tasks](#get_v2_tasks) - List tasks
* [post_v2_tasks](#post_v2_tasks) - Create a task
* [get_v2_tasks_task_id_](#get_v2_tasks_task_id_) - Get a task
* [patch_v2_tasks_task_id_](#patch_v2_tasks_task_id_) - Update a task
* [delete_v2_tasks_task_id_](#delete_v2_tasks_task_id_) - Delete a task

## get_v2_tasks

List all tasks. Results are sorted by creation date, from oldest to newest.

Required scopes: `task:read`, `object_configuration:read`, `record_permission:read`, `user_management:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio, models
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.tasks.get_v2_tasks(limit=10, offset=5, sort=models.GetV2TasksSort.CREATED_AT_DESC, linked_object="people", linked_record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d", assignee="50cf242c-7fa3-4cad-87d0-75b1af71c57b", is_completed=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          | Example                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                   | N/A                                                                                                                                                                                                  | 10                                                                                                                                                                                                   |
| `offset`                                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                   | N/A                                                                                                                                                                                                  | 5                                                                                                                                                                                                    |
| `sort`                                                                                                                                                                                               | [Optional[models.GetV2TasksSort]](../../models/getv2taskssort.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                   | Optionally sort the results. "created_at:asc" returns oldest results first, "created_at:desc" returns the newest results first. If unspecified, defaults to "created_at:asc" (oldest results first). | created_at:desc                                                                                                                                                                                      |
| `linked_object`                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                   | N/A                                                                                                                                                                                                  | people                                                                                                                                                                                               |
| `linked_record_id`                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                   | N/A                                                                                                                                                                                                  | 891dcbfc-9141-415d-9b2a-2238a6cc012d                                                                                                                                                                 |
| `assignee`                                                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                   | N/A                                                                                                                                                                                                  | 50cf242c-7fa3-4cad-87d0-75b1af71c57b                                                                                                                                                                 |
| `is_completed`                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                   | N/A                                                                                                                                                                                                  | true                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                  |                                                                                                                                                                                                      |

### Response

**[models.GetV2TasksResponse](../../models/getv2tasksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## post_v2_tasks

Creates a new task.

At present, tasks can only be created from plaintext without record reference formatting.

Required scopes: `task:read-write`, `object_configuration:read`, `record_permission:read`, `user_management:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio, models
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.tasks.post_v2_tasks(data={
        "content": "Follow up on current software solutions",
        "format_": models.PostV2TasksFormat.PLAINTEXT,
        "deadline_at": "2023-01-01T15:00:00.000000000Z",
        "is_completed": False,
        "linked_records": [
            {
                "target_object": "people",
                "target_record_id": "891dcbfc-9141-415d-9b2a-2238a6cc012d",
            },
        ],
        "assignees": [],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data`                                                              | [models.PostV2TasksData](../../models/postv2tasksdata.md)           | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostV2TasksResponse](../../models/postv2tasksresponse.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.PostV2TasksValidationTypeError | 400                                   | application/json                      |
| errors.PostV2TasksNotFoundError       | 404                                   | application/json                      |
| errors.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## get_v2_tasks_task_id_

Get a single task by ID.

Required scopes: `task:read`, `object_configuration:read`, `record_permission:read`, `user_management:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.tasks.get_v2_tasks_task_id_(task_id="649e34f4-c39a-4f4d-99ef-48a36bef8f04")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 649e34f4-c39a-4f4d-99ef-48a36bef8f04                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2TasksTaskIDResponse](../../models/getv2taskstaskidresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GetV2TasksTaskIDNotFoundError | 404                                  | application/json                     |
| errors.APIError                      | 4XX, 5XX                             | \*/\*                                |

## patch_v2_tasks_task_id_

Updates an existing task by `task_id`. At present, only the `deadline_at`, `is_completed`, `linked_records`, and `assignees` fields can be updated.

Required scopes: `task:read-write`, `object_configuration:read`, `record_permission:read`, `user_management:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio, models
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.tasks.patch_v2_tasks_task_id_(task_id="649e34f4-c39a-4f4d-99ef-48a36bef8f04", data={
        "deadline_at": "2023-01-01T15:00:00.000000000Z",
        "is_completed": False,
        "linked_records": [
            {
                "target_object": "people",
                "target_record_id": "891dcbfc-9141-415d-9b2a-2238a6cc012d",
            },
            {
                "target_object": "people",
                "slug_or_id_of_matching_attribute": [
                    {
                        "domain": "app.attio.com",
                    },
                ],
            },
        ],
        "assignees": [
            {
                "referenced_actor_type": models.PatchV2TasksTaskIDReferencedActorType.WORKSPACE_MEMBER,
                "referenced_actor_id": "50cf242c-7fa3-4cad-87d0-75b1af71c57b",
            },
            {
                "referenced_actor_type": models.PatchV2TasksTaskIDReferencedActorType.WORKSPACE_MEMBER,
                "referenced_actor_id": "50cf242c-7fa3-4cad-87d0-75b1af71c57b",
            },
            {
                "referenced_actor_type": models.PatchV2TasksTaskIDReferencedActorType.WORKSPACE_MEMBER,
                "referenced_actor_id": "50cf242c-7fa3-4cad-87d0-75b1af71c57b",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `task_id`                                                               | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     | 649e34f4-c39a-4f4d-99ef-48a36bef8f04                                    |
| `data`                                                                  | [models.PatchV2TasksTaskIDData](../../models/patchv2taskstaskiddata.md) | :heavy_check_mark:                                                      | N/A                                                                     |                                                                         |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |                                                                         |

### Response

**[models.PatchV2TasksTaskIDResponse](../../models/patchv2taskstaskidresponse.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| errors.PatchV2TasksTaskIDValidationTypeError | 400                                          | application/json                             |
| errors.PatchV2TasksTaskIDNotFoundError       | 404                                          | application/json                             |
| errors.APIError                              | 4XX, 5XX                                     | \*/\*                                        |

## delete_v2_tasks_task_id_

Delete a task by ID.

Required scopes: `task:read-write`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.tasks.delete_v2_tasks_task_id_(task_id="649e34f4-c39a-4f4d-99ef-48a36bef8f04")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `task_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 649e34f4-c39a-4f4d-99ef-48a36bef8f04                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteV2TasksTaskIDResponse](../../models/deletev2taskstaskidresponse.md)**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.DeleteV2TasksTaskIDNotFoundError | 404                                     | application/json                        |
| errors.APIError                         | 4XX, 5XX                                | \*/\*                                   |