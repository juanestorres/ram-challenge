import requests
import traceback
import json
from datetime import datetime
from char_counter import char_counter
from episode_locations import episode_locations


#API's urls. Just in case they may change in the future.
characters_url = 'https://rickandmortyapi.com/api/character'
episodes_url = "https://rickandmortyapi.com/api/episode"
locations_url = 'https://rickandmortyapi.com/api/location'

def fetch_data(url):
    """Fetches the API data using requests module.

    Args:
        url (string): The API's url where the data comes from.

    Returns:
        [Response]: Returns the response object.
    """
    response = requests.get(url)
    response_json = response.json()
    next_page_url = response_json["info"]["next"]


    while next_page_url:
        new_response = requests.get(next_page_url)
        new_response_json = new_response.json()
        response_json['results'] += new_response_json['results']
        next_page_url = new_response_json["info"]["next"]
    return  response_json







def rick_and_morty_solution():
    try:
        #Start time measurement for first exercise
        start = datetime.now()

        #Get the responses for each list
        #characters_response = fetch_data(characters_url)
        #episodes_response = fetch_data(episodes_url)
        #locations_response = fetch_data(locations_url)

        #Get the json(dict) information from the response
        characters_json = fetch_data(characters_url)
        episodes_json = fetch_data(episodes_url)
        locations_json = fetch_data(locations_url)

        char_counter_json = char_counter(characters_json, episodes_json, locations_json, start)

        #Start time measurement for second exercise
        start = datetime.now()

        episode_locations_json = episode_locations(characters_json, episodes_json, start)

        answers = [char_counter_json, episode_locations_json]
        with open('results.json', 'w') as file:
            file.write(json.dumps(answers))
            file.close()

    except Exception as e:
        print("There was an error fetching the information. " + str(traceback.format_exc()))



rick_and_morty_solution()


