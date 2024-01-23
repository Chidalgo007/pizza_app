from kivy.network.urlrequest import UrlRequest
import json

class HttpClient:
    def get_pizzas(self, on_complete):
        url="https://pizzachris-6eebc6d87850.herokuapp.com/api/GetPizza"

        def data_received(req, result):
            data = json.loads(result)
            pizza_dict = []
            for i in data:
                pizza_dict.append(i['fields']) 
            print('data_received')
            if on_complete:
                on_complete(pizza_dict)

        req = UrlRequest(url, data_received)                