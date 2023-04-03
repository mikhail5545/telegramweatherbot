"""
Получает ip адрес пользователя для дальнейшего получения координат
"""
import aiohttp


async def _get_ip() -> dict:
    url = 'http://ipinfo.io/json'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            ip_data = await response.json()
    
    return ip_data
