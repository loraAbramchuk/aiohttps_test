import asyncio
import aiohttp
import json

async def get_request(session):
    async with session.get('http://localhost:8080/get') as response:
        result = await response.json()
        print("GET ответ:")
        print(result)
        print("-" * 50)
        return result

async def post_request(session):
    data = {"username": "student", "score": 100}
    async with session.post('http://localhost:8080/post', json=data) as response:
        result = await response.json()
        print("POST ответ:")
        print(result)
        print("-" * 50)
        return result

async def patch_request(session):
    update_data = {"username": "student", "score": 150}
    async with session.patch('http://localhost:8080/patch', json=update_data) as response:
        result = await response.json()
        print("PATCH ответ:")
        print(result)
        print("-" * 50)
        return result

async def delete_request(session):
    async with session.delete('http://localhost:8080/delete') as response:
        result = await response.json()
        print("DELETE ответ:")
        print(result)
        print("-" * 50)
        return result

async def make_parallel_requests():
    async with aiohttp.ClientSession() as session:
        task = [
            get_request(session),
            post_request(session),
            patch_request(session),
            delete_request(session)
        ]
        result = await asyncio.gather(*task)
        return result

async def main():
    result = await make_parallel_requests()
    print("\nВсе результаты получены!")

if __name__ == "__main__":
    asyncio.run(main())

