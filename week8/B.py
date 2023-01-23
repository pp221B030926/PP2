import json
data = '''{
    "Subscriptions": [{
        "name": "Three month subscription",
        "price": "39900",
        "discount": "50"
    },
    {
        "name": "One month subscription",
        "price": "19900",
        "discount": "30"
    },
    {
        "name": "Premium free trial",
        "price": "40000",
        "discount": "10"
    }]
}'''
data = json.loads(data)
min = 1000000
name = ''
for i in data['Subscriptions']:
    sum = int(i['price']) * (100 - int(i['discount'])) / 100
    if sum < min:
        name = i['name']
        min = sum
print('Name:', name)
print('Price:', int(min))