import requests
from datetime import datetime, timedelta
from char_counter import char_counter


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
    return requests.get(url)



def rick_and_morty_solution():
    try:
        #Start time measurement for first exercise
        start = datetime.now()

        #Get the responses for each list
        characters_response = fetch_data(characters_url)
        episodes_response = fetch_data(episodes_url)
        locations_response = fetch_data(locations_url)

        #Get the json(dict) information from the response
        characters_json = characters_response.json()
        episodes_json = episodes_response.json()
        locations_json = locations_response.json()

        char_counter_json = char_counter(characters_json, episodes_json, locations_json, start)
        print(char_counter_json)

        #Start time measurement for second exercise
        start = datetime.now()



    except Exception as e:
        print("There was an error fetching the information. " + str(e))



rick_and_morty_solution()


