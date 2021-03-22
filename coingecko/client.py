import aiohttp

from aiohttp import ContentTypeError
from exceptions import FailedDecodeJson, BadMethod


class HTTPClient:

    async def request(self, method: str, url: str, *args, **kwargs) -> dict:
        async with aiohttp.ClientSession() as session:
            if method.upper() == 'GET':
                async with session.get(url, **kwargs) as resp:
                    return await self.validate_json(resp, *args)
            elif method.upper() == 'POST':
                async with session.post(url, **kwargs) as resp:
                    return await self.validate_json(resp, *args)
            else:
                raise BadMethod('Accept only GET/POST')

    @staticmethod
    async def validate_json(resp: aiohttp.ClientResponse, content_type: str = 'application/json') -> dict:
        try:
            return await resp.json(content_type=content_type)
        except ContentTypeError as e:
            bad_url = str(str(e).split(",")[2]).split("'")[1]
            raise FailedDecodeJson(f"Check args, URL is invalid\nURL- {bad_url}")
