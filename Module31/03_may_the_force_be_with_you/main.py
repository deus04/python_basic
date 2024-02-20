import requests
import json


my_req = requests.get('https://swapi.dev/api/starships/12/')

data = json.loads(my_req.text)
print(data)

xwing_info = dict()
xwing_info['name'] = data['name']
xwing_info['max_atmosphering_speed'] = data['max_atmosphering_speed']
xwing_info['starship_class'] = data['starship_class']
xwing_info['pilots'] = list()
for i_pilot in data['pilots']:
    i_pilot_req = requests.get(i_pilot)
    i_pilot_data = json.loads(i_pilot_req.text)
    print(i_pilot_data)
    pilots_parametrs = dict()

    pilots_parametrs['name'] = i_pilot_data['name']
    pilots_parametrs['height'] = i_pilot_data['height']
    pilots_parametrs['mass'] = i_pilot_data['mass']

    pilot_homeworld_name_req = requests.get(i_pilot_data['homeworld'])
    pilot_homeworld_name = json.loads(pilot_homeworld_name_req.text)
    pilots_parametrs['homeworld'] = pilot_homeworld_name['name']

    pilots_parametrs['homeworld_url'] = i_pilot_data['homeworld']
    xwing_info['pilots'].append(pilots_parametrs)

print(xwing_info)

with open('my_data.json', 'w') as file:
    json.dump(xwing_info, file, indent=4)

