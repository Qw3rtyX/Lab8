import requests

def get_pokemon_info(pokemon_name):

    pokemon_name = pokemon_name.strip().lower()
    if pokemon_name in (None, ''):
        return
    
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
    resp_msg = requests.get(url)

    if resp_msg.status_code == 200:
        return resp_msg.json()
    else:
        print('failed to get Pokemon info.')
        print('Response code:', resp_msg.status_code)
        print(resp_msg.txt)