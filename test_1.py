import asyncio
import aiohttp
import json

async def make_requests():
    async with aiohttp.ClientSession() as session:
        # GET запрос
        async with session.get('http://localhost:8080/get') as response:
            print("GET ответ:")
            print(await response.json())
            print("-" * 50)

        # POST запрос
        data = {"username": "student", "score": 100}
        async with session.post('http://localhost:8080/post', json=data) as response:
            print("POST ответ:")
            print(await response.json())
            print("-" * 50)

        # PATCH запрос
        update_data = {"username": "student", "score": 150}
        async with session.patch('http://localhost:8080/patch', json=update_data) as response:
            print("PATCH ответ:")
            print(await response.json())
            print("-" * 50)

        # DELETE запрос
        async with session.delete('http://localhost:8080/delete') as response:
            print("DELETE ответ:")
            print(await response.json())
            print("-" * 50)

async def main():
    await make_requests()

if __name__ == "__main__":
    asyncio.run(main())