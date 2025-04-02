from aiohttp import web
import json

# Хранилище данных для демонстрации
storage = {
    "student": {"score": 0}
}

async def index(request):
    print("Приветики:)")
    return web.Response(text="Добро пожаловать на сервер!")


async def handle_get(request):
    return web.json_response({"message": "Данные успешно получены", "data": storage})

async def handle_post(request):
    data = await request.json()
    username = data.get("username")
    score = data.get("score")
    
    if username and score is not None:
        storage[username] = {"score": score}
        return web.json_response({
            "message": "Данные успешно добавлены",
            "data": {username: storage[username]}
        })
    return web.json_response({"error": "Неверные данные"}, status=400)

async def handle_patch(request):
    data = await request.json()
    username = data.get("username")
    score = data.get("score")
    
    if username in storage:
        storage[username]["score"] = score
        return web.json_response({
            "message": "Данные успешно обновлены",
            "data": {username: storage[username]}
        })
    return web.json_response({"error": "Пользователь не найден"}, status=404)

async def handle_delete(request):
    storage.clear()
    return web.json_response({"message": "Все данные удалены"})

app = web.Application()
app.router.add_get('/', index)
app.router.add_get('/get', handle_get)
app.router.add_post('/post', handle_post)
app.router.add_patch('/patch', handle_patch)
app.router.add_delete('/delete', handle_delete)

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=8080) 