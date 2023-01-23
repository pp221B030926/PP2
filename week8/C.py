import json
data = '''{
    "providerName": "ooo Ngrok",
    "updateDate": "18.12.2015",
    "items": [
      {
        "code": "9435001",
        "name": "Депенд белье впитывающее жен L/XL 1*6 (8шт)",
        "manufacturer": "Кимберли Кларк",
        "manufacturerCountry": "Россия",
        "barcode": "5029053543727",
        "quantity": 92,
        "price": 389.1315,
        "multiplicity": 1,
        "ratends": 18,
        "expirationDate": ""
      },
      {
        "code": "1971001",
        "name": "Депенд белье впитывающее жен L/XL 1*6 (10шт)",
        "manufacturer": "Кимберли Кларк",
        "manufacturerCountry": "Россия",
        "barcode": "",
        "quantity": 142,
        "price": 326.0243,
        "multiplicity": 1,
        "ratends": 18,
        "expirationDate": ""
      },
      {
        "code": "9435002",
        "name": "Депенд белье впитывающее муж L/XL 1*6 (8шт)",
        "manufacturer": "Кимберли Кларк",
        "manufacturerCountry": "Россия",
        "barcode": "5029053543734",
        "quantity": 123,
        "price": 389.1315,
        "multiplicity": 1,
        "ratends": 18,
        "expirationDate": ""
      },
      {
        "code": "9435006",
        "name": "Депенд прокладки при недерж жен мини 1*12 (10шт)",
        "manufacturer": "Кимберли Кларк",
        "manufacturerCountry": "Россия",
        "barcode": "5029053543857",
        "quantity": 93,
        "price": 97.2108,
        "multiplicity": 1,
        "ratends": 18,
        "expirationDate": ""
      }
    ]
  }'''
data = json.loads(data)
sum = 0
for i in data['items']:
    sum += i['quantity'] * i['price']
print('Полная оплата составляет',int(sum), 'тг.')