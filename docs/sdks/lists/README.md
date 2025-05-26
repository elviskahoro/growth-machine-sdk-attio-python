# Lists
(*lists*)

## Overview

Lists are used to model a particular process. A list contains many records of a single object type, where each record is represented by an entry. Entries contain their own data from attributes defined on the list and also data from their parent record. See our [data model guide](/docs/data-model) for more information.

### Available Operations

* [get_v2_lists](#get_v2_lists) - List all lists
* [post_v2_lists](#post_v2_lists) - Create a list
* [get_v2_lists_list_](#get_v2_lists_list_) - Get a list
* [patch_v2_lists_list_](#patch_v2_lists_list_) - Update a list

## get_v2_lists

List all lists that your access token has access to. lists are returned in the order that they are sorted in the sidebar.

Required scopes: `list_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.lists.get_v2_lists()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetV2ListsResponse](../../models/getv2listsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## post_v2_lists

Creates a new list.

Once you have your list, add attributes to it using the [Create attribute](/reference/post_v2-target-identifier-attributes) API, and add records to it using the [Add records to list](/reference/post_v2-lists-list-entries) API. 

New lists must specify which records can be added with the `parent_object` parameter which accepts either an object slug or an object ID. Permissions for the list are controlled with the `workspace_access` and `workspace_member_access` parameters.

Please note that new lists must have either `workspace_access` set to `"full-access"` or one or more element of `workspace_member_access` with a `"full-access"` level. It is also possible to receive a `403` billing error if your workspace is not on a plan that supports either advanced workspace or workspace member-level access for lists.

Required scopes: `list_configuration:read-write`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio, models
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.lists.post_v2_lists(data={
        "name": "Enterprise Sales",
        "api_slug": "enterprise_sales",
        "parent_object": "people",
        "workspace_access": models.PostV2ListsWorkspaceAccess.READ_AND_WRITE,
        "workspace_member_access": [
            {
                "workspace_member_id": "50cf242c-7fa3-4cad-87d0-75b1af71c57b",
                "level": models.PostV2ListsLevel.READ_AND_WRITE,
            },
            {
                "workspace_member_id": "50cf242c-7fa3-4cad-87d0-75b1af71c57b",
                "level": models.PostV2ListsLevel.READ_AND_WRITE,
            },
            {
                "workspace_member_id": "50cf242c-7fa3-4cad-87d0-75b1af71c57b",
                "level": models.PostV2ListsLevel.READ_AND_WRITE,
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data`                                                              | [models.PostV2ListsData](../../models/postv2listsdata.md)           | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostV2ListsResponse](../../models/postv2listsresponse.md)**

### Errors

| Error Type                           | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.PostV2ListsValueNotFoundError | 400                                  | application/json                     |
| errors.BillingError                  | 403                                  | application/json                     |
| errors.PostV2ListsNotFoundError      | 404                                  | application/json                     |
| errors.APIError                      | 4XX, 5XX                             | \*/\*                                |

## get_v2_lists_list_

Gets a single list in your workspace that your access token has access to.

Required scopes: `list_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.lists.get_v2_lists_list_(list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `list`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 33ebdbe9-e529-47c9-b894-0ba25e9c15c0                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2ListsListResponse](../../models/getv2listslistresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GetV2ListsListNotFoundError | 404                                | application/json                   |
| errors.APIError                    | 4XX, 5XX                           | \*/\*                              |

## patch_v2_lists_list_

Updates an existing list. Permissions for the list are controlled with the `workspace_access` and `workspace_member_access` parameters. Please note that lists must have either `workspace_access` set to `"full-access"` or one or more element of `workspace_member_access` with a `"full-access"` level. It is also possible to receive a `403` billing error if your workspace is not on a plan that supports either advanced workspace or workspace member level access for lists. Changing the parent object of a list is not possible through the API as it can have unintended side-effects that should be considered carefully. If you wish to carry out a parent object change you should do so through the UI.

Required scopes: `list_configuration:read-write`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio, models
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.lists.patch_v2_lists_list_(list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0", data={
        "name": "Enterprise Sales",
        "api_slug": "enterprise_sales",
        "workspace_access": models.PatchV2ListsListWorkspaceAccess.READ_AND_WRITE,
        "workspace_member_access": [
            {
                "workspace_member_id": "50cf242c-7fa3-4cad-87d0-75b1af71c57b",
                "level": models.PatchV2ListsListLevel.READ_AND_WRITE,
            },
            {
                "workspace_member_id": "50cf242c-7fa3-4cad-87d0-75b1af71c57b",
                "level": models.PatchV2ListsListLevel.READ_AND_WRITE,
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `list`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 33ebdbe9-e529-47c9-b894-0ba25e9c15c0                                |
| `data`                                                              | [models.PatchV2ListsListData](../../models/patchv2listslistdata.md) | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PatchV2ListsListResponse](../../models/patchv2listslistresponse.md)**

### Errors

| Error Type                                | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.PatchV2ListsListValueNotFoundError | 400                                       | application/json                          |
| errors.PatchV2ListsListNotFoundError      | 404                                       | application/json                          |
| errors.APIError                           | 4XX, 5XX                                  | \*/\*                                     |