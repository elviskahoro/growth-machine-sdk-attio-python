# growth-machine-sdk-attio-python

Developer-friendly & type-safe Python SDK specifically catered to leverage *growth-machine-sdk-attio-python* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=growth-machine-sdk-attio-python&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/chalk-ai/chalk-ai). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [growth-machine-sdk-attio-python](#growth-machine-sdk-attio-python)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from growth-machine-sdk-attio-python python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "growth-machine-sdk-attio-python",
# ]
# ///

from growth_machine_sdk_attio_python import Attio

sdk = Attio(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.objects.get_v2_objects()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from growth_machine_sdk_attio_python import Attio
import os

async def main():

    async with Attio(
        oauth2=os.getenv("ATTIO_OAUTH2", ""),
    ) as attio:

        res = await attio.objects.get_v2_objects_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name     | Type   | Scheme       | Environment Variable |
| -------- | ------ | ------------ | -------------------- |
| `oauth2` | oauth2 | OAuth2 token | `ATTIO_OAUTH2`       |

To authenticate with the API the `oauth2` parameter must be set when initializing the SDK client instance. For example:
```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.objects.get_v2_objects()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>


### [attributes](docs/sdks/attributes/README.md)

* [get_v2_target_identifier_attributes](docs/sdks/attributes/README.md#get_v2_target_identifier_attributes) - List attributes
* [post_v2_target_identifier_attributes](docs/sdks/attributes/README.md#post_v2_target_identifier_attributes) - Create an attribute
* [get_v2_target_identifier_attributes_attribute_](docs/sdks/attributes/README.md#get_v2_target_identifier_attributes_attribute_) - Get an attribute
* [patch_v2_target_identifier_attributes_attribute_](docs/sdks/attributes/README.md#patch_v2_target_identifier_attributes_attribute_) - Update an attribute
* [get_v2_target_identifier_attributes_attribute_options](docs/sdks/attributes/README.md#get_v2_target_identifier_attributes_attribute_options) - List select options
* [post_v2_target_identifier_attributes_attribute_options](docs/sdks/attributes/README.md#post_v2_target_identifier_attributes_attribute_options) - Create a select option
* [patch_v2_target_identifier_attributes_attribute_options_option_](docs/sdks/attributes/README.md#patch_v2_target_identifier_attributes_attribute_options_option_) - Update a select option
* [get_v2_target_identifier_attributes_attribute_statuses](docs/sdks/attributes/README.md#get_v2_target_identifier_attributes_attribute_statuses) - List statuses
* [post_v2_target_identifier_attributes_attribute_statuses](docs/sdks/attributes/README.md#post_v2_target_identifier_attributes_attribute_statuses) - Create a status
* [patch_v2_target_identifier_attributes_attribute_statuses_status_](docs/sdks/attributes/README.md#patch_v2_target_identifier_attributes_attribute_statuses_status_) - Update a status

### [comments](docs/sdks/comments/README.md)

* [post_v2_comments](docs/sdks/comments/README.md#post_v2_comments) - Create a comment
* [get_v2_comments_comment_id_](docs/sdks/comments/README.md#get_v2_comments_comment_id_) - Get a comment
* [delete_v2_comments_comment_id_](docs/sdks/comments/README.md#delete_v2_comments_comment_id_) - Delete a comment

### [entries](docs/sdks/entries/README.md)

* [post_v2_lists_list_entries_query](docs/sdks/entries/README.md#post_v2_lists_list_entries_query) - List entries
* [post_v2_lists_list_entries](docs/sdks/entries/README.md#post_v2_lists_list_entries) - Create an entry (add record to list)
* [put_v2_lists_list_entries](docs/sdks/entries/README.md#put_v2_lists_list_entries) - Assert a list entry by parent
* [get_v2_lists_list_entries_entry_id_](docs/sdks/entries/README.md#get_v2_lists_list_entries_entry_id_) - Get a list entry
* [patch_v2_lists_list_entries_entry_id_](docs/sdks/entries/README.md#patch_v2_lists_list_entries_entry_id_) - Update a list entry (append multiselect values)
* [put_v2_lists_list_entries_entry_id_](docs/sdks/entries/README.md#put_v2_lists_list_entries_entry_id_) - Update a list entry (overwrite multiselect values)
* [delete_v2_lists_list_entries_entry_id_](docs/sdks/entries/README.md#delete_v2_lists_list_entries_entry_id_) - Delete a list entry
* [get_v2_lists_list_entries_entry_id_attributes_attribute_values](docs/sdks/entries/README.md#get_v2_lists_list_entries_entry_id_attributes_attribute_values) - List attribute values for a list entry

### [lists](docs/sdks/lists/README.md)

* [get_v2_lists](docs/sdks/lists/README.md#get_v2_lists) - List all lists
* [post_v2_lists](docs/sdks/lists/README.md#post_v2_lists) - Create a list
* [get_v2_lists_list_](docs/sdks/lists/README.md#get_v2_lists_list_) - Get a list
* [patch_v2_lists_list_](docs/sdks/lists/README.md#patch_v2_lists_list_) - Update a list

### [meta](docs/sdks/meta/README.md)

* [get_v2_self](docs/sdks/meta/README.md#get_v2_self) - Identify

### [notes](docs/sdks/notes/README.md)

* [get_v2_notes](docs/sdks/notes/README.md#get_v2_notes) - List notes
* [post_v2_notes](docs/sdks/notes/README.md#post_v2_notes) - Create a note
* [get_v2_notes_note_id_](docs/sdks/notes/README.md#get_v2_notes_note_id_) - Get a note
* [delete_v2_notes_note_id_](docs/sdks/notes/README.md#delete_v2_notes_note_id_) - Delete a note

### [objects](docs/sdks/objects/README.md)

* [get_v2_objects](docs/sdks/objects/README.md#get_v2_objects) - List objects
* [post_v2_objects](docs/sdks/objects/README.md#post_v2_objects) - Create an object
* [get_v2_objects_object_](docs/sdks/objects/README.md#get_v2_objects_object_) - Get an object
* [patch_v2_objects_object_](docs/sdks/objects/README.md#patch_v2_objects_object_) - Update an object

### [records](docs/sdks/records/README.md)

* [post_v2_objects_object_records_query](docs/sdks/records/README.md#post_v2_objects_object_records_query) - List records
* [post_v2_objects_object_records](docs/sdks/records/README.md#post_v2_objects_object_records) - Create a record
* [put_v2_objects_object_records](docs/sdks/records/README.md#put_v2_objects_object_records) - Assert a record
* [get_v2_objects_object_records_record_id_](docs/sdks/records/README.md#get_v2_objects_object_records_record_id_) - Get a record
* [patch_v2_objects_object_records_record_id_](docs/sdks/records/README.md#patch_v2_objects_object_records_record_id_) - Update a record (append multiselect values)
* [put_v2_objects_object_records_record_id_](docs/sdks/records/README.md#put_v2_objects_object_records_record_id_) - Update a record (overwrite multiselect values)
* [delete_v2_objects_object_records_record_id_](docs/sdks/records/README.md#delete_v2_objects_object_records_record_id_) - Delete a record
* [get_v2_objects_object_records_record_id_attributes_attribute_values](docs/sdks/records/README.md#get_v2_objects_object_records_record_id_attributes_attribute_values) - List record attribute values
* [get_v2_objects_object_records_record_id_entries](docs/sdks/records/README.md#get_v2_objects_object_records_record_id_entries) - List record entries

### [tasks](docs/sdks/tasks/README.md)

* [get_v2_tasks](docs/sdks/tasks/README.md#get_v2_tasks) - List tasks
* [post_v2_tasks](docs/sdks/tasks/README.md#post_v2_tasks) - Create a task
* [get_v2_tasks_task_id_](docs/sdks/tasks/README.md#get_v2_tasks_task_id_) - Get a task
* [patch_v2_tasks_task_id_](docs/sdks/tasks/README.md#patch_v2_tasks_task_id_) - Update a task
* [delete_v2_tasks_task_id_](docs/sdks/tasks/README.md#delete_v2_tasks_task_id_) - Delete a task

### [threads](docs/sdks/threads/README.md)

* [get_v2_threads](docs/sdks/threads/README.md#get_v2_threads) - List threads
* [get_v2_threads_thread_id_](docs/sdks/threads/README.md#get_v2_threads_thread_id_) - Get a thread

### [webhooks](docs/sdks/webhooks/README.md)

* [get_v2_webhooks](docs/sdks/webhooks/README.md#get_v2_webhooks) - List webhooks
* [post_v2_webhooks](docs/sdks/webhooks/README.md#post_v2_webhooks) - Create a webhook
* [get_v2_webhooks_webhook_id_](docs/sdks/webhooks/README.md#get_v2_webhooks_webhook_id_) - Get a webhook
* [patch_v2_webhooks_webhook_id_](docs/sdks/webhooks/README.md#patch_v2_webhooks_webhook_id_) - Update a webhook
* [delete_v2_webhooks_webhook_id_](docs/sdks/webhooks/README.md#delete_v2_webhooks_webhook_id_) - Delete a webhook

### [workspace_members](docs/sdks/workspacemembers/README.md)

* [get_v2_workspace_members](docs/sdks/workspacemembers/README.md#get_v2_workspace_members) - List workspace members
* [get_v2_workspace_members_workspace_member_id_](docs/sdks/workspacemembers/README.md#get_v2_workspace_members_workspace_member_id_) - Get a workspace member

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from growth_machine_sdk_attio_python import Attio
from growth_machine_sdk_attio_python.utils import BackoffStrategy, RetryConfig
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.objects.get_v2_objects(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from growth_machine_sdk_attio_python import Attio
from growth_machine_sdk_attio_python.utils import BackoffStrategy, RetryConfig
import os


with Attio(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.objects.get_v2_objects()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `post_v2_objects_async` method may raise the following exceptions:

| Error Type                            | Status Code | Content Type     |
| ------------------------------------- | ----------- | ---------------- |
| errors.PostV2ObjectsSlugConflictError | 409         | application/json |
| errors.APIError                       | 4XX, 5XX    | \*/\*            |

### Example

```python
from growth_machine_sdk_attio_python import Attio, errors
import os


with Attio(
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:
    res = None
    try:

        res = attio.objects.post_v2_objects(data={
            "api_slug": "people",
            "singular_noun": "Person",
            "plural_noun": "People",
        })

        # Handle response
        print(res)

    except errors.PostV2ObjectsSlugConflictError as e:
        # handle e.data: errors.PostV2ObjectsSlugConflictErrorData
        raise(e)
    except errors.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from growth_machine_sdk_attio_python import Attio
import os


with Attio(
    server_url="https://api.attio.com",
    oauth2=os.getenv("ATTIO_OAUTH2", ""),
) as attio:

    res = attio.objects.get_v2_objects()

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from growth_machine_sdk_attio_python import Attio
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Attio(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from growth_machine_sdk_attio_python import Attio
from growth_machine_sdk_attio_python.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Attio(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Attio` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from growth_machine_sdk_attio_python import Attio
import os
def main():

    with Attio(
        oauth2=os.getenv("ATTIO_OAUTH2", ""),
    ) as attio:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Attio(
        oauth2=os.getenv("ATTIO_OAUTH2", ""),
    ) as attio:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from growth_machine_sdk_attio_python import Attio
import logging

logging.basicConfig(level=logging.DEBUG)
s = Attio(debug_logger=logging.getLogger("growth_machine_sdk_attio_python"))
```

You can also enable a default debug logger by setting an environment variable `ATTIO_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=growth-machine-sdk-attio-python&utm_campaign=python)
