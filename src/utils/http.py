import httpx

async def httpxGetAsync(url):
    async with httpx.AsyncClient() as client:
        return await client.get(url)
    
async def httpxDeleteAsync(url):
    async with httpx.AsyncClient() as client:
        return await client.delete(url)

async def httpxPutAsync(url, data):
    async with httpx.AsyncClient() as client:
        return await client.put(url, json=data)

async def httpxPatchAsync(url, data):
    async with httpx.AsyncClient() as client:
        return await client.patch(url, json=data)