"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from growth_machine_sdk_attio_python import models, utils
from growth_machine_sdk_attio_python._hooks import SDKHooks
from growth_machine_sdk_attio_python.types import OptionalNullable, UNSET
import httpx
import importlib
from typing import Any, Callable, Dict, Optional, TYPE_CHECKING, Union, cast
import weakref

if TYPE_CHECKING:
    from growth_machine_sdk_attio_python.attributes import Attributes
    from growth_machine_sdk_attio_python.comments import Comments
    from growth_machine_sdk_attio_python.entries import Entries
    from growth_machine_sdk_attio_python.lists import Lists
    from growth_machine_sdk_attio_python.meta import Meta
    from growth_machine_sdk_attio_python.notes import Notes
    from growth_machine_sdk_attio_python.objects import Objects
    from growth_machine_sdk_attio_python.records import Records
    from growth_machine_sdk_attio_python.tasks import Tasks
    from growth_machine_sdk_attio_python.threads import Threads
    from growth_machine_sdk_attio_python.webhooks import Webhooks
    from growth_machine_sdk_attio_python.workspace_members import WorkspaceMembers


class Attio(BaseSDK):
    objects: "Objects"
    r"""Objects are the core data models inside of Attio. They contain standard objects, such as [people](/docs/standard-objects-people), [companies](/docs/standard-objects-companies) or [deals](/docs/standard-objects-deals), and custom objects that are specific to your use-case. See our [data model guide](/docs/data-model) for more information."""
    attributes: "Attributes"
    r"""Attributes model properties of objects and lists. Some attributes, such as the `name` attribute on a person, are system-defined, while others are user-defined. Attributes are one of [many types](/docs/attribute-types) such as text, location or select. See our [data model guide](/docs/data-model) for more information."""
    records: "Records"
    r"""Records are individual instances of objects e.g. a specific [person](/docs/standard-objects-people) or [company](/docs/standard-objects-companies). See our [data model guide](/docs/data-model) for more information."""
    lists: "Lists"
    r"""Lists are used to model a particular process. A list contains many records of a single object type, where each record is represented by an entry. Entries contain their own data from attributes defined on the list and also data from their parent record. See our [data model guide](/docs/data-model) for more information."""
    entries: "Entries"
    r"""Entries are elements in a list that reference a single parent record. Entries contain their own data from attributes defined on the list and also data from their parent record. See our [data model guide](/docs/data-model) for more information."""
    workspace_members: "WorkspaceMembers"
    r"""Workspace members represent a user with access to a workspace. Workspace members are assigned roles that determine what they can do within the workspace."""
    notes: "Notes"
    r"""Notes are rich text documents that reference a single parent record."""
    tasks: "Tasks"
    r"""A task is a defined, actionable item with references to linked records and assigned workspace members."""
    threads: "Threads"
    r"""Threads are groups of [comments](/reference/get_v2-comments-comment-id) on either a record or entry."""
    comments: "Comments"
    r"""Comments are messages on a [thread](/reference/get_v2-threads)."""
    webhooks: "Webhooks"
    r"""Webhooks allow you to listen for changes to data in Attio, for example when a record is updated."""
    meta: "Meta"
    r"""Meta endpoints are used to get information about the API token."""
    _sub_sdk_map = {
        "objects": ("growth_machine_sdk_attio_python.objects", "Objects"),
        "attributes": ("growth_machine_sdk_attio_python.attributes", "Attributes"),
        "records": ("growth_machine_sdk_attio_python.records", "Records"),
        "lists": ("growth_machine_sdk_attio_python.lists", "Lists"),
        "entries": ("growth_machine_sdk_attio_python.entries", "Entries"),
        "workspace_members": (
            "growth_machine_sdk_attio_python.workspace_members",
            "WorkspaceMembers",
        ),
        "notes": ("growth_machine_sdk_attio_python.notes", "Notes"),
        "tasks": ("growth_machine_sdk_attio_python.tasks", "Tasks"),
        "threads": ("growth_machine_sdk_attio_python.threads", "Threads"),
        "comments": ("growth_machine_sdk_attio_python.comments", "Comments"),
        "webhooks": ("growth_machine_sdk_attio_python.webhooks", "Webhooks"),
        "meta": ("growth_machine_sdk_attio_python.meta", "Meta"),
    }

    def __init__(
        self,
        oauth2: Optional[Union[Optional[str], Callable[[], Optional[str]]]] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param oauth2: The oauth2 required for authentication
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        client_supplied = True
        if client is None:
            client = httpx.Client()
            client_supplied = False

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        async_client_supplied = True
        if async_client is None:
            async_client = httpx.AsyncClient()
            async_client_supplied = False

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        security: Any = None
        if callable(oauth2):
            # pylint: disable=unnecessary-lambda-assignment
            security = lambda: models.Security(oauth2=oauth2())
        else:
            security = models.Security(oauth2=oauth2)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                client_supplied=client_supplied,
                async_client=async_client,
                async_client_supplied=async_client_supplied,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        weakref.finalize(
            self,
            close_clients,
            cast(ClientOwner, self.sdk_configuration),
            self.sdk_configuration.client,
            self.sdk_configuration.client_supplied,
            self.sdk_configuration.async_client,
            self.sdk_configuration.async_client_supplied,
        )

    def __getattr__(self, name: str):
        if name in self._sub_sdk_map:
            module_path, class_name = self._sub_sdk_map[name]
            try:
                module = importlib.import_module(module_path)
                klass = getattr(module, class_name)
                instance = klass(self.sdk_configuration)
                setattr(self, name, instance)
                return instance
            except ImportError as e:
                raise AttributeError(
                    f"Failed to import module {module_path} for attribute {name}: {e}"
                ) from e
            except AttributeError as e:
                raise AttributeError(
                    f"Failed to find class {class_name} in module {module_path} for attribute {name}: {e}"
                ) from e

        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{name}'"
        )

    def __dir__(self):
        default_attrs = list(super().__dir__())
        lazy_attrs = list(self._sub_sdk_map.keys())
        return sorted(list(set(default_attrs + lazy_attrs)))

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.client is not None
            and not self.sdk_configuration.client_supplied
        ):
            self.sdk_configuration.client.close()
        self.sdk_configuration.client = None

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.async_client is not None
            and not self.sdk_configuration.async_client_supplied
        ):
            await self.sdk_configuration.async_client.aclose()
        self.sdk_configuration.async_client = None
