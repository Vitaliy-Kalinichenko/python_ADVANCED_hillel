import aiohttp
from aiohttp import web

apis = {
    'api_1': {
        'url': "https://numbersapi.p.rapidapi.com/6/21/date",
        'querystring': {"fragment": "true", "json": "true"},
        'headers': {
            'x-rapidapi-key': "f7a97a4b1cmsheca736213eec59fp10fda2jsn486833907246",
            'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }
    },
    'api_2': {
        'url': "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total",
        'querystring': {"country": "Canada"},
        'headers': {
            'x-rapidapi-key': "f7a97a4b1cmsheca736213eec59fp10fda2jsn486833907246",
            'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
        }
    }
}


async def handler(request):
    async with aiohttp.ClientSession() as session:  # создаем сессию для запроса на сервера
        web_data = []
        for api in apis.values():  # проходим в цикле по apis, делаем get запросы на url, с заголовками и параметрами
            async with session.get(api['url'], headers=api['headers'], params=api['querystring']) as responce:
                data = await responce.json()  # получаем ответ - json данные
                web_data.append(data)
        return web.json_response(web_data)


app = web.Application()
app.add_routes([web.get('/collect_info', handler)])

if __name__ == '__main__':
    web.run_app(app)
