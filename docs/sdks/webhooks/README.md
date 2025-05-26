# Webhooks
(*webhooks*)

## Overview

Webhooks allow you to listen for changes to data in Attio, for example when a record is updated.

### Available Operations

* [get_v2_webhooks](#get_v2_webhooks) - List webhooks
* [post_v2_webhooks](#post_v2_webhooks) - Create a webhook
* [get_v2_webhooks_webhook_id_](#get_v2_webhooks_webhook_id_) - Get a webhook
* [patch_v2_webhooks_webhook_id_](#patch_v2_webhooks_webhook_id_) - Update a webhook
* [delete_v2_webhooks_webhook_id_](#delete_v2_webhooks_webhook_id_) - Delete a webhook

## get_v2_webhooks

Get all of the webhooks in your workspace.

Required scopes: `webhook:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.webhooks.get_v2_webhooks(limit=10, offset=5)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 10                                                                  |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | 5                                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2WebhooksResponse](../../models/getv2webhooksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## post_v2_webhooks

Create a webhook and associated subscriptions.

Required scopes: `webhook:read-write`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.webhooks.post_v2_webhooks(data={
        "target_url": "https://example.com/webhook",
        "subscriptions": [],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `data`                                                                        | [models.PostV2WebhooksDataRequest](../../models/postv2webhooksdatarequest.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.PostV2WebhooksResponse](../../models/postv2webhooksresponse.md)**

### Errors

| Error Type                               | Status Code                              | Content Type                             |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| errors.PostV2WebhooksValidationTypeError | 400                                      | application/json                         |
| errors.APIError                          | 4XX, 5XX                                 | \*/\*                                    |

## get_v2_webhooks_webhook_id_

Get a single webhook.

Required scopes: `webhook:read`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.webhooks.get_v2_webhooks_webhook_id_(webhook_id="23e42eaf-323a-41da-b5bb-fd67eebda553")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 23e42eaf-323a-41da-b5bb-fd67eebda553                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetV2WebhooksWebhookIDResponse](../../models/getv2webhookswebhookidresponse.md)**

### Errors

| Error Type                                 | Status Code                                | Content Type                               |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| errors.GetV2WebhooksWebhookIDNotFoundError | 404                                        | application/json                           |
| errors.APIError                            | 4XX, 5XX                                   | \*/\*                                      |

## patch_v2_webhooks_webhook_id_

Update a webhook and associated subscriptions.

Required scopes: `webhook:read-write`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio, models
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.webhooks.patch_v2_webhooks_webhook_id_(webhook_id="23e42eaf-323a-41da-b5bb-fd67eebda553", data={
        "target_url": "https://example.com/webhook",
        "subscriptions": [
            {
                "event_type": models.PatchV2WebhooksWebhookIDEventTypeRequest.NOTE_CREATED,
                "filter_": {
                    "dollar_and": [
                        {
                            "field": "parent_object_id",
                            "operator": models.PatchV2WebhooksWebhookIDDollarAndOperatorEqualsRequest.EQUALS,
                            "value": "97052eb9-e65e-443f-a297-f2d9a4a7f795",
                        },
                    ],
                },
            },
            {
                "event_type": models.PatchV2WebhooksWebhookIDEventTypeRequest.NOTE_CREATED,
                "filter_": {
                    "dollar_and": [
                        {
                            "field": "parent_object_id",
                            "operator": models.PatchV2WebhooksWebhookIDDollarAndOperatorEqualsRequest.EQUALS,
                            "value": "97052eb9-e65e-443f-a297-f2d9a4a7f795",
                        },
                    ],
                },
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `webhook_id`                                                                                      | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               | 23e42eaf-323a-41da-b5bb-fd67eebda553                                                              |
| `data`                                                                                            | [models.PatchV2WebhooksWebhookIDDataRequest](../../models/patchv2webhookswebhookiddatarequest.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |                                                                                                   |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |

### Response

**[models.PatchV2WebhooksWebhookIDResponse](../../models/patchv2webhookswebhookidresponse.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| errors.PatchV2WebhooksWebhookIDNotFoundError | 404                                          | application/json                             |
| errors.APIError                              | 4XX, 5XX                                     | \*/\*                                        |

## delete_v2_webhooks_webhook_id_

Delete a webhook by ID.

Required scopes: `webhook:read-write`.

### Example Usage

```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.webhooks.delete_v2_webhooks_webhook_id_(webhook_id="23e42eaf-323a-41da-b5bb-fd67eebda553")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 23e42eaf-323a-41da-b5bb-fd67eebda553                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteV2WebhooksWebhookIDResponse](../../models/deletev2webhookswebhookidresponse.md)**

### Errors

| Error Type                                    | Status Code                                   | Content Type                                  |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| errors.DeleteV2WebhooksWebhookIDNotFoundError | 404                                           | application/json                              |
| errors.APIError                               | 4XX, 5XX                                      | \*/\*                                         |