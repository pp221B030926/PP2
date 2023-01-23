import json
data = '''{ 
    "squadName": "Super Hero Squad", 
    "homeTown": "Metro City", 
    "formed": 2016, 
    "secretBase": "Super tower", 
    "active": true, 
    "members": [ 
      { 
        "name": "Molecule Man", 
        "age": 29, 
        "secretIdentity": "Dan Jukes", 
        "powers": [ 
          "Radiation resistance", 
          "Turning tiny", 
          "Radiation blast" 
          ] 
      }, 
      { 
        "name": "Madame Uppercut", 
        "age": 39, 
        "secretIdentity": "Jane Wilson", 
        "powers": [ 
          "Million tonne punch", 
          "Damage resistance", 
          "Superhuman reflexes" 
          ] 
      }, 
      { 
        "name": "Eternal Flame", 
        "age": 1000000, 
        "secretIdentity": "Unknown", 
        "powers": [ 
          "Immortality", 
          "Heat Immunity", 
          "Inferno", 
          "Teleportation", 
          "Interdimensional travel" 
          ] 
      } 
    ] 
  } '''

data = json.loads(data)
print('==========', end = '')
print(data['squadName'].upper(), end = '')
print('==========')
print('Hometown:', data["homeTown"], end = ', ')
print(data["secretBase"], end = ' // ')
print('Formed:',data["formed"])
print('')
for i in data["members"]:
    print('___________________________________')
    print(i['name'].upper())
    print('Real name: ', end = '')
    print(i['secretIdentity'])
    print('Age: ', end = '')
    print(i['age'])
    print('Superpowers:')
    for j in i['powers']:
        print('  ',j)