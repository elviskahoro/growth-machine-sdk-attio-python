<!-- Start SDK Example Usage [usage] -->
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