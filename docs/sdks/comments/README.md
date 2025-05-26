# Comments
(*comments*)

## Overview

Comments are messages on a [thread](/reference/get_v2-threads).

### Available Operations

* [post_v2_comments](#post_v2_comments) - Create a comment
* [get_v2_comments_comment_id_](#get_v2_comments_comment_id_) - Get a comment
* [delete_v2_comments_comment_id_](#delete_v2_comments_comment_id_) - Delete a comment

## post_v2_comments

Creates a new comment related to an existing thread, record or entry.

To create comments on records, you will need the `object_configuration:read` and `record_permission:read` scopes.

To create comments on list entries, you will need the `list_configuration:read` and `list_entry:read` scopes.

Required scopes: `comment:read-write`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio, models
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.comments.post_v2_comments(data={
        "format_": models.PostV2CommentsFormat2.PLAINTEXT,
        "content": "If I put the email address of my colleague on Attio in here, e.g. alice@attio.com, they will be notified. Other emails (e.g. person@example.com) will be turned into clickable links.",
        "author": {
            "type": models.TypeWorkspaceMember2.WORKSPACE_MEMBER,
            "id": "50cf242c-7fa3-4cad-87d0-75b1af71c57b",
        },
        "created_at": "2023-01-01T15:00:00.000000000Z",
        "record": {
            "object": "97052eb9-e65e-443f-a297-f2d9a4a7f795",
            "record_id": "bf071e1f-6035-429d-b874-d83ea64ea13b",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `data`                                                                    | [models.PostV2CommentsDataUnion](../../models/postv2commentsdataunion.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.PostV2CommentsResponse](../../models/postv2commentsresponse.md)**

### Errors

| Error Type                              | Status Code                             | Content Type                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| errors.PostV2CommentsValueNotFoundError | 400                                     | application/json                        |
| errors.APIError                         | 4XX, 5XX                                | \*/\*                                   |

## get_v2_comments_comment_id_

Get a single comment by ID.

To view comments on records, you will need the `object_configuration:read` and `record_permission:read` scopes.

To view comments on list entries, you will need the `list_configuration:read` and `list_entry:read` scopes.

Required scopes: `comment:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.comments.get_v2_comments_comment_id_(comment_id="aa1dc1d9-93ac-4c6c-987e-16b6eea9aab2")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `comment_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | aa1dc1d9-93ac-4c6c-987e-16b6eea9aab2                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2CommentsCommentIDResponse](../../models/getv2commentscommentidresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.GetV2CommentsCommentIDNotFoundError | 404                                        | application/json                           |
| errors.APIError                            | 4XX, 5XX                                   | \*/\*                                      |

## delete_v2_comments_comment_id_

Deletes a comment by ID. If deleting a comment at the head of a thread, all messages in the thread are also deleted.

Required scopes: `comment:read-write`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.comments.delete_v2_comments_comment_id_(comment_id="aa1dc1d9-93ac-4c6c-987e-16b6eea9aab2")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `comment_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | aa1dc1d9-93ac-4c6c-987e-16b6eea9aab2                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteV2CommentsCommentIDResponse](../../models/deletev2commentscommentidresponse.md)**

### Errors

| Error Type                                    | Status Code                                   | Content Type                                  |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| errors.DeleteV2CommentsCommentIDNotFoundError | 404                                           | application/json                              |
| errors.APIError                               | 4XX, 5XX                                      | \*/\*                                         |