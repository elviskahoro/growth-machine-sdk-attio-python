# Entries
(*entries*)

## Overview

Entries are elements in a list that reference a single parent record. Entries contain their own data from attributes defined on the list and also data from their parent record. See our [data model guide](/docs/data-model) for more information.

### Available Operations

* [post_v2_lists_list_entries_query](#post_v2_lists_list_entries_query) - List entries
* [post_v2_lists_list_entries](#post_v2_lists_list_entries) - Create an entry (add record to list)
* [put_v2_lists_list_entries](#put_v2_lists_list_entries) - Assert a list entry by parent
* [get_v2_lists_list_entries_entry_id_](#get_v2_lists_list_entries_entry_id_) - Get a list entry
* [patch_v2_lists_list_entries_entry_id_](#patch_v2_lists_list_entries_entry_id_) - Update a list entry (append multiselect values)
* [put_v2_lists_list_entries_entry_id_](#put_v2_lists_list_entries_entry_id_) - Update a list entry (overwrite multiselect values)
* [delete_v2_lists_list_entries_entry_id_](#delete_v2_lists_list_entries_entry_id_) - Delete a list entry
* [get_v2_lists_list_entries_entry_id_attributes_attribute_values](#get_v2_lists_list_entries_entry_id_attributes_attribute_values) - List attribute values for a list entry

## post_v2_lists_list_entries_query

Lists entries in a given list, with the option to filter and sort results.

Required scopes: `list_entry:read`, `list_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio, models
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.entries.post_v2_lists_list_entries_query(list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0", filter_={
        "name": "Ada Lovelace",
    }, sorts=[
        {
            "direction": models.PostV2ListsListEntriesQueryDirection1.ASC,
            "attribute": "name",
            "field": "last_name",
        },
    ], limit=500, offset=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `list`                                                                                                                                    | *str*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | N/A                                                                                                                                       | 33ebdbe9-e529-47c9-b894-0ba25e9c15c0                                                                                                      |
| `filter_`                                                                                                                                 | Dict[str, *Any*]                                                                                                                          | :heavy_minus_sign:                                                                                                                        | An object used to filter results to a subset of results. See the [full guide to filtering and sorting here](/docs/filtering-and-sorting). | {<br/>"name": "Ada Lovelace"<br/>}                                                                                                        |
| `sorts`                                                                                                                                   | List[[models.PostV2ListsListEntriesQuerySortUnion](../../models/postv2listslistentriesquerysortunion.md)]                                 | :heavy_minus_sign:                                                                                                                        | An object used to sort results. See the [full guide to filtering and sorting here](/docs/filtering-and-sorting).                          | [<br/>{<br/>"direction": "asc",<br/>"attribute": "name",<br/>"field": "last_name"<br/>}<br/>]                                             |
| `limit`                                                                                                                                   | *Optional[float]*                                                                                                                         | :heavy_minus_sign:                                                                                                                        | The maximum number of results to return. Defaults to 500. See the [full guide to pagination here](/docs/pagination).                      | 500                                                                                                                                       |
| `offset`                                                                                                                                  | *Optional[float]*                                                                                                                         | :heavy_minus_sign:                                                                                                                        | The number of results to skip over before returning. Defaults to 0. See the [full guide to pagination here](/docs/pagination).            | 0                                                                                                                                         |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.PostV2ListsListEntriesQueryResponse](../../models/postv2listslistentriesqueryresponse.md)**

### Errors

| Error Type                                      | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| errors.PostV2ListsListEntriesQueryNotFoundError | 404                                             | application/json                                |
| errors.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |

## post_v2_lists_list_entries

Adds a record to a list as a new list entry. This endpoint will throw on conflicts of unique attributes. Multiple list entries are allowed for the same parent record

Required scopes: `list_entry:read-write`, `list_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.entries.post_v2_lists_list_entries(list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0", data={
        "parent_record_id": "891dcbfc-9141-415d-9b2a-2238a6cc012d",
        "parent_object": "people",
        "entry_values": {
            "41252299-f8c7-4b5e-99c9-4ff8321d2f96": [
                "Text value",
            ],
            "multiselect_attribute": [
                "Select option 1",
                "Select option 2",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `list`                                                                                        | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           | 33ebdbe9-e529-47c9-b894-0ba25e9c15c0                                                          |
| `data`                                                                                        | [models.PostV2ListsListEntriesDataRequest](../../models/postv2listslistentriesdatarequest.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |                                                                                               |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[models.PostV2ListsListEntriesResponse](../../models/postv2listslistentriesresponse.md)**

### Errors

| Error Type                                      | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| errors.PostV2ListsListEntriesValueNotFoundError | 400                                             | application/json                                |
| errors.PostV2ListsListEntriesNotFoundError      | 404                                             | application/json                                |
| errors.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |

## put_v2_lists_list_entries

Use this endpoint to create or update a list entry for a given parent record. If an entry with the specified parent record is found, that entry will be updated. If no such entry is found, a new entry will be created instead. If there are multiple entries with the same parent record, this endpoint with return the "MULTIPLE_MATCH_RESULTS" error. When writing to multi-select attributes, all values will be either created or deleted as necessary to match the list of values supplied in the request body.

Required scopes: `list_entry:read-write`, `list_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.entries.put_v2_lists_list_entries(list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0", data={
        "parent_record_id": "891dcbfc-9141-415d-9b2a-2238a6cc012d",
        "parent_object": "people",
        "entry_values": {
            "41252299-f8c7-4b5e-99c9-4ff8321d2f96": [
                "Text value",
            ],
            "multiselect_attribute": [
                "Select option 1",
                "Select option 2",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 | Example                                                                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `list`                                                                                      | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         | 33ebdbe9-e529-47c9-b894-0ba25e9c15c0                                                        |
| `data`                                                                                      | [models.PutV2ListsListEntriesDataRequest](../../models/putv2listslistentriesdatarequest.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |                                                                                             |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |                                                                                             |

### Response

**[models.PutV2ListsListEntriesResponse](../../models/putv2listslistentriesresponse.md)**

### Errors

| Error Type                                | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.MultipleMatchResultsError          | 400                                       | application/json                          |
| errors.PutV2ListsListEntriesNotFoundError | 404                                       | application/json                          |
| errors.APIError                           | 4XX, 5XX                                  | \*/\*                                     |

## get_v2_lists_list_entries_entry_id_

Gets a single list entry by its `entry_id`.

Required scopes: `list_entry:read`, `list_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.entries.get_v2_lists_list_entries_entry_id_(list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0", entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `list`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 33ebdbe9-e529-47c9-b894-0ba25e9c15c0                                |
| `entry_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2e6e29ea-c4e0-4f44-842d-78a891f8c156                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2ListsListEntriesEntryIDResponse](../../models/getv2listslistentriesentryidresponse.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| errors.GetV2ListsListEntriesEntryIDNotFoundError | 404                                              | application/json                                 |
| errors.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |

## patch_v2_lists_list_entries_entry_id_

Use this endpoint to update list entries by `entry_id`. If the update payload includes multiselect attributes, the values supplied will be created and prepended to the list of values that already exist (if any). Use the `PUT` endpoint to overwrite or remove multiselect attribute values.

Required scopes: `list_entry:read-write`, `list_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.entries.patch_v2_lists_list_entries_entry_id_(list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0", entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156", data={
        "entry_values": {
            "41252299-f8c7-4b5e-99c9-4ff8321d2f96": [
                "Text value",
            ],
            "multiselect_attribute": [
                "Select option 1",
                "Select option 2",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   | Example                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `list`                                                                                                        | *str*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           | 33ebdbe9-e529-47c9-b894-0ba25e9c15c0                                                                          |
| `entry_id`                                                                                                    | *str*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           | 2e6e29ea-c4e0-4f44-842d-78a891f8c156                                                                          |
| `data`                                                                                                        | [models.PatchV2ListsListEntriesEntryIDDataRequest](../../models/patchv2listslistentriesentryiddatarequest.md) | :heavy_check_mark:                                                                                            | N/A                                                                                                           |                                                                                                               |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |                                                                                                               |

### Response

**[models.PatchV2ListsListEntriesEntryIDResponse](../../models/patchv2listslistentriesentryidresponse.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| errors.PatchV2ListsListEntriesEntryIDImmutableValueError | 400                                                      | application/json                                         |
| errors.PatchV2ListsListEntriesEntryIDNotFoundError       | 404                                                      | application/json                                         |
| errors.APIError                                          | 4XX, 5XX                                                 | \*/\*                                                    |

## put_v2_lists_list_entries_entry_id_

Use this endpoint to update list entries by `entry_id`. If the update payload includes multiselect attributes, the values supplied will overwrite/remove the list of values that already exist (if any). Use the `PATCH` endpoint to add multiselect attribute values without removing those value that already exist.

Required scopes: `list_entry:read-write`, `list_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.entries.put_v2_lists_list_entries_entry_id_(list="33ebdbe9-e529-47c9-b894-0ba25e9c15c0", entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156", data={
        "entry_values": {
            "41252299-f8c7-4b5e-99c9-4ff8321d2f96": [
                "Text value",
            ],
            "multiselect_attribute": [
                "Select option 1",
                "Select option 2",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `list`                                                                                                    | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       | 33ebdbe9-e529-47c9-b894-0ba25e9c15c0                                                                      |
| `entry_id`                                                                                                | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       | 2e6e29ea-c4e0-4f44-842d-78a891f8c156                                                                      |
| `data`                                                                                                    | [models.PutV2ListsListEntriesEntryIDDataRequest](../../models/putv2listslistentriesentryiddatarequest.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |                                                                                                           |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |

### Response

**[models.PutV2ListsListEntriesEntryIDResponse](../../models/putv2listslistentriesentryidresponse.md)**

### Errors

| Error Type                                             | Status Code                                            | Content Type                                           |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| errors.PutV2ListsListEntriesEntryIDImmutableValueError | 400                                                    | application/json                                       |
| errors.PutV2ListsListEntriesEntryIDNotFoundError       | 404                                                    | application/json                                       |
| errors.APIError                                        | 4XX, 5XX                                               | \*/\*                                                  |

## delete_v2_lists_list_entries_entry_id_

Deletes a single list entry by its `entry_id`.

Required scopes: `list_entry:read-write`, `list_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.entries.delete_v2_lists_list_entries_entry_id_(list="enterprise_sales", entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `list`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | enterprise_sales                                                    |
| `entry_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2e6e29ea-c4e0-4f44-842d-78a891f8c156                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteV2ListsListEntriesEntryIDResponse](../../models/deletev2listslistentriesentryidresponse.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| errors.DeleteV2ListsListEntriesEntryIDNotFoundError | 404                                                 | application/json                                    |
| errors.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## get_v2_lists_list_entries_entry_id_attributes_attribute_values

Gets all values for a given attribute on a list entry. If the attribute is historic, this endpoint has the ability to return all historic values using the `show_historic` query param.

Required scopes: `list_entry:read`, `list_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.entries.get_v2_lists_list_entries_entry_id_attributes_attribute_values(list="enterprise_sales", entry_id="2e6e29ea-c4e0-4f44-842d-78a891f8c156", attribute="41252299-f8c7-4b5e-99c9-4ff8321d2f96", limit=10, offset=5)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `list`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | enterprise_sales                                                    |
| `entry_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2e6e29ea-c4e0-4f44-842d-78a891f8c156                                |
| `attribute`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 41252299-f8c7-4b5e-99c9-4ff8321d2f96                                |
| `show_historic`                                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 | true                                                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 10                                                                  |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 5                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2ListsListEntriesEntryIDAttributesAttributeValuesResponse](../../models/getv2listslistentriesentryidattributesattributevaluesresponse.md)**

### Errors

| Error Type                                                                      | Status Code                                                                     | Content Type                                                                    |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| errors.GetV2ListsListEntriesEntryIDAttributesAttributeValuesValidationTypeError | 400                                                                             | application/json                                                                |
| errors.GetV2ListsListEntriesEntryIDAttributesAttributeValuesNotFoundError       | 404                                                                             | application/json                                                                |
| errors.APIError                                                                 | 4XX, 5XX                                                                        | \*/\*                                                                           |