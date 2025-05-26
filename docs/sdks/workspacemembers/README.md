# WorkspaceMembers
(*workspace_members*)

## Overview

Workspace members represent a user with access to a workspace. Workspace members are assigned roles that determine what they can do within the workspace.

### Available Operations

* [get_v2_workspace_members](#get_v2_workspace_members) - List workspace members
* [get_v2_workspace_members_workspace_member_id_](#get_v2_workspace_members_workspace_member_id_) - Get a workspace member

## get_v2_workspace_members

Lists all workspace members in the workspace.

Required scopes: `user_management:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.workspace_members.get_v2_workspace_members()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetV2WorkspaceMembersResponse](../../models/getv2workspacemembersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_v2_workspace_members_workspace_member_id_

Gets a single workspace member by ID.

Required scopes: `user_management:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.workspace_members.get_v2_workspace_members_workspace_member_id_(workspace_member_id="50cf242c-7fa3-4cad-87d0-75b1af71c57b")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workspace_member_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 50cf242c-7fa3-4cad-87d0-75b1af71c57b                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2WorkspaceMembersWorkspaceMemberIDResponse](../../models/getv2workspacemembersworkspacememberidresponse.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| errors.GetV2WorkspaceMembersWorkspaceMemberIDNotFoundError | 404                                                        | application/json                                           |
| errors.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |