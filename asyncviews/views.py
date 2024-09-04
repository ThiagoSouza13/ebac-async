import asyncio
import httpx
from django.http import JsonResponse


async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(f"Request {num}")
        
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/posts/1")
        print(f"Response {num}: {response.status_code}")
        
async def async_views(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return JsonResponse({"Non-blocking": "Response"}) 