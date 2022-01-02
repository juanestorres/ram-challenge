import requests

api_results = 'results'
api_name = "name"
characters_url = 'https://rickandmortyapi.com/api/character'
episodes_url = "https://rickandmortyapi.com/api/episode"
locations_url = 'https://rickandmortyapi.com/api/location'

def fetch_data(url):
    return requests.get(url)

try:
    characters_response = fetch_data(characters_url)
    episodes_response = fetch_data(episodes_url)
    locations_response = fetch_data(locations_url)

    characters_json = characters_response.json()
    episodes_json = episodes_response.json()
    locations_json = locations_response.json()


except Exception as e:
    print("There was an error fetching the information. " + str(e))