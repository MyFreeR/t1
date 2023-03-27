import pprint
import json
from requests import get, post, delete, put

ff = open('response.json')
# Response: Говорит Алиса, этот тест просто читает респонс.
pprint.pprint(post('http://127.0.0.1:5000/post', json=json.load(ff)).json()['response']['text'])
# pprint.pprint(post('http://127.0.0.1:5000/post', json=json.load(ff)).json())
ff.close()


print()

ff = open('request.json', encoding='utf8')
# Request: Говорит пользователь, этот тест выдаёт ответ Алисы.
pprint.pprint(post('http://127.0.0.1:5000/post', json=json.load(ff)).json()['response']['text'])
# pprint.pprint(post('http://127.0.0.1:5000/post', json=json.load(ff)).json())
ff.close()
