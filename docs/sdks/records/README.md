# Records
(*records*)

## Overview

Records are individual instances of objects e.g. a specific [person](/docs/standard-objects-people) or [company](/docs/standard-objects-companies). See our [data model guide](/docs/data-model) for more information.

### Available Operations

* [post_v2_objects_object_records_query](#post_v2_objects_object_records_query) - List records
* [post_v2_objects_object_records](#post_v2_objects_object_records) - Create a record
* [put_v2_objects_object_records](#put_v2_objects_object_records) - Assert a record
* [get_v2_objects_object_records_record_id_](#get_v2_objects_object_records_record_id_) - Get a record
* [patch_v2_objects_object_records_record_id_](#patch_v2_objects_object_records_record_id_) - Update a record (append multiselect values)
* [put_v2_objects_object_records_record_id_](#put_v2_objects_object_records_record_id_) - Update a record (overwrite multiselect values)
* [delete_v2_objects_object_records_record_id_](#delete_v2_objects_object_records_record_id_) - Delete a record
* [get_v2_objects_object_records_record_id_attributes_attribute_values](#get_v2_objects_object_records_record_id_attributes_attribute_values) - List record attribute values
* [get_v2_objects_object_records_record_id_entries](#get_v2_objects_object_records_record_id_entries) - List record entries

## post_v2_objects_object_records_query

Lists people, company or other records, with the option to filter and sort results.

Required scopes: `record_permission:read`, `object_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio, models
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.records.post_v2_objects_object_records_query(object="people", filter_={
        "name": "Ada Lovelace",
    }, sorts=[
        {
            "direction": models.PostV2ObjectsObjectRecordsQueryDirection1.ASC,
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
| `object`                                                                                                                                  | *str*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | N/A                                                                                                                                       | people                                                                                                                                    |
| `filter_`                                                                                                                                 | Dict[str, *Any*]                                                                                                                          | :heavy_minus_sign:                                                                                                                        | An object used to filter results to a subset of results. See the [full guide to filtering and sorting here](/docs/filtering-and-sorting). | {<br/>"name": "Ada Lovelace"<br/>}                                                                                                        |
| `sorts`                                                                                                                                   | List[[models.PostV2ObjectsObjectRecordsQuerySortUnion](../../models/postv2objectsobjectrecordsquerysortunion.md)]                         | :heavy_minus_sign:                                                                                                                        | An object used to sort results. See the [full guide to filtering and sorting here](/docs/filtering-and-sorting).                          | [<br/>{<br/>"direction": "asc",<br/>"attribute": "name",<br/>"field": "last_name"<br/>}<br/>]                                             |
| `limit`                                                                                                                                   | *Optional[float]*                                                                                                                         | :heavy_minus_sign:                                                                                                                        | The maximum number of results to return. Defaults to 500. See the [full guide to pagination here](/docs/pagination).                      | 500                                                                                                                                       |
| `offset`                                                                                                                                  | *Optional[float]*                                                                                                                         | :heavy_minus_sign:                                                                                                                        | The number of results to skip over before returning. Defaults to 0. See the [full guide to pagination here](/docs/pagination).            | 0                                                                                                                                         |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.PostV2ObjectsObjectRecordsQueryResponse](../../models/postv2objectsobjectrecordsqueryresponse.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| errors.FilterError                                  | 400                                                 | application/json                                    |
| errors.PostV2ObjectsObjectRecordsQueryNotFoundError | 404                                                 | application/json                                    |
| errors.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## post_v2_objects_object_records

Creates a new person, company or other record. This endpoint will throw on conflicts of unique attributes. If you would prefer to update records on conflicts, please use the [Assert record endpoint](/reference/put_v2-objects-object-records) instead.

Required scopes: `record_permission:read-write`, `object_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.records.post_v2_objects_object_records(object="people", data={
        "values": {
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

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `object`                                                                                              | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   | people                                                                                                |
| `data`                                                                                                | [models.PostV2ObjectsObjectRecordsDataRequest](../../models/postv2objectsobjectrecordsdatarequest.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |                                                                                                       |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |                                                                                                       |

### Response

**[models.PostV2ObjectsObjectRecordsResponse](../../models/postv2objectsobjectrecordsresponse.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| errors.PostV2ObjectsObjectRecordsValueNotFoundError | 400                                                 | application/json                                    |
| errors.PostV2ObjectsObjectRecordsNotFoundError      | 404                                                 | application/json                                    |
| errors.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## put_v2_objects_object_records

Use this endpoint to create or update people, companies and other records. A matching attribute is used to search for existing records. If a record is found with the same value for the matching attribute, that record will be updated. If no record with the same value for the matching attribute is found, a new record will be created instead. If you would like to avoid matching, please use the [Create record endpoint](/reference/post_v2-objects-object-records).

If the matching attribute is a multiselect attribute, new values will be added and existing values will not be deleted. For any other multiselect attribute, all values will be either created or deleted as necessary to match the list of supplied values.

Required scopes: `record_permission:read-write`, `object_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.records.put_v2_objects_object_records(object="people", matching_attribute="41252299-f8c7-4b5e-99c9-4ff8321d2f96", data={
        "values": {
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

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         | Example                                                                                             |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `object`                                                                                            | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 | people                                                                                              |
| `matching_attribute`                                                                                | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 | 41252299-f8c7-4b5e-99c9-4ff8321d2f96                                                                |
| `data`                                                                                              | [models.PutV2ObjectsObjectRecordsDataRequest](../../models/putv2objectsobjectrecordsdatarequest.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |                                                                                                     |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |                                                                                                     |

### Response

**[models.PutV2ObjectsObjectRecordsResponse](../../models/putv2objectsobjectrecordsresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| errors.PutV2ObjectsObjectRecordsValueNotFoundError | 400                                                | application/json                                   |
| errors.PutV2ObjectsObjectRecordsNotFoundError      | 404                                                | application/json                                   |
| errors.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## get_v2_objects_object_records_record_id_

Gets a single person, company or other record by its `record_id`.

Required scopes: `record_permission:read`, `object_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.records.get_v2_objects_object_records_record_id_(object="people", record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `object`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | people                                                              |
| `record_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 891dcbfc-9141-415d-9b2a-2238a6cc012d                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2ObjectsObjectRecordsRecordIDResponse](../../models/getv2objectsobjectrecordsrecordidresponse.md)**

### Errors

| Error Type                                            | Status Code                                           | Content Type                                          |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| errors.GetV2ObjectsObjectRecordsRecordIDNotFoundError | 404                                                   | application/json                                      |
| errors.APIError                                       | 4XX, 5XX                                              | \*/\*                                                 |

## patch_v2_objects_object_records_record_id_

Use this endpoint to update people, companies, and other records by `record_id`. If the update payload includes multiselect attributes, the values supplied will be created and prepended to the list of values that already exist (if any). Use the `PUT` endpoint to overwrite or remove multiselect attribute values.

Required scopes: `record_permission:read-write`, `object_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.records.patch_v2_objects_object_records_record_id_(object="people", record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d", data={
        "values": {
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

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             | Example                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `object`                                                                                                                | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     | people                                                                                                                  |
| `record_id`                                                                                                             | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     | 891dcbfc-9141-415d-9b2a-2238a6cc012d                                                                                    |
| `data`                                                                                                                  | [models.PatchV2ObjectsObjectRecordsRecordIDDataRequest](../../models/patchv2objectsobjectrecordsrecordiddatarequest.md) | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |                                                                                                                         |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |                                                                                                                         |

### Response

**[models.PatchV2ObjectsObjectRecordsRecordIDResponse](../../models/patchv2objectsobjectrecordsrecordidresponse.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| errors.PatchV2ObjectsObjectRecordsRecordIDMissingValueError | 400                                                         | application/json                                            |
| errors.PatchV2ObjectsObjectRecordsRecordIDNotFoundError     | 404                                                         | application/json                                            |
| errors.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## put_v2_objects_object_records_record_id_

Use this endpoint to update people, companies, and other records by `record_id`. If the update payload includes multiselect attributes, the values supplied will overwrite/remove the list of values that already exist (if any). Use the `PATCH` endpoint to append multiselect values without removing those that already exist.

Required scopes: `record_permission:read-write`, `object_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.records.put_v2_objects_object_records_record_id_(object="people", record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d", data={
        "values": {
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

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         | Example                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `object`                                                                                                            | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 | people                                                                                                              |
| `record_id`                                                                                                         | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 | 891dcbfc-9141-415d-9b2a-2238a6cc012d                                                                                |
| `data`                                                                                                              | [models.PutV2ObjectsObjectRecordsRecordIDDataRequest](../../models/putv2objectsobjectrecordsrecordiddatarequest.md) | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |                                                                                                                     |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |                                                                                                                     |

### Response

**[models.PutV2ObjectsObjectRecordsRecordIDResponse](../../models/putv2objectsobjectrecordsrecordidresponse.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| errors.PutV2ObjectsObjectRecordsRecordIDMissingValueError | 400                                                       | application/json                                          |
| errors.PutV2ObjectsObjectRecordsRecordIDNotFoundError     | 404                                                       | application/json                                          |
| errors.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |

## delete_v2_objects_object_records_record_id_

Deletes a single record (e.g. a company or person) by ID.

Required scopes: `object_configuration:read`, `record_permission:read-write`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.records.delete_v2_objects_object_records_record_id_(object="people", record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `object`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | people                                                              |
| `record_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 891dcbfc-9141-415d-9b2a-2238a6cc012d                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteV2ObjectsObjectRecordsRecordIDResponse](../../models/deletev2objectsobjectrecordsrecordidresponse.md)**

### Errors

| Error Type                                               | Status Code                                              | Content Type                                             |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| errors.DeleteV2ObjectsObjectRecordsRecordIDNotFoundError | 404                                                      | application/json                                         |
| errors.APIError                                          | 4XX, 5XX                                                 | \*/\*                                                    |

## get_v2_objects_object_records_record_id_attributes_attribute_values

Gets all values for a given attribute on a record. If the attribute is historic, this endpoint has the ability to return all historic values using the `show_historic` query param.

Required scopes: `record_permission:read`, `object_configuration:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.records.get_v2_objects_object_records_record_id_attributes_attribute_values(object="people", record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d", attribute="41252299-f8c7-4b5e-99c9-4ff8321d2f96", limit=10, offset=5)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `object`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | people                                                              |
| `record_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 891dcbfc-9141-415d-9b2a-2238a6cc012d                                |
| `attribute`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 41252299-f8c7-4b5e-99c9-4ff8321d2f96                                |
| `show_historic`                                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 | true                                                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 10                                                                  |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 5                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2ObjectsObjectRecordsRecordIDAttributesAttributeValuesResponse](../../models/getv2objectsobjectrecordsrecordidattributesattributevaluesresponse.md)**

### Errors

| Error Type                                                                           | Status Code                                                                          | Content Type                                                                         |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| errors.GetV2ObjectsObjectRecordsRecordIDAttributesAttributeValuesValidationTypeError | 400                                                                                  | application/json                                                                     |
| errors.GetV2ObjectsObjectRecordsRecordIDAttributesAttributeValuesNotFoundError       | 404                                                                                  | application/json                                                                     |
| errors.APIError                                                                      | 4XX, 5XX                                                                             | \*/\*                                                                                |

## get_v2_objects_object_records_record_id_entries

List all entries, across all lists, for which this record is the parent.

Required scopes: `record_permission:read`, `object_configuration:read`, `list_entry:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.records.get_v2_objects_object_records_record_id_entries(object="people", record_id="891dcbfc-9141-415d-9b2a-2238a6cc012d", limit=10, offset=5)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `object`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | people                                                              |
| `record_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 891dcbfc-9141-415d-9b2a-2238a6cc012d                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 10                                                                  |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 5                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2ObjectsObjectRecordsRecordIDEntriesResponse](../../models/getv2objectsobjectrecordsrecordidentriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |