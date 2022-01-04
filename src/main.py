import requests
import traceback
import json
from datetime import datetime
from char_counter import char_counter
from episode_locations import episode_locations
from concurrent.futures import ThreadPoolExecutor, as_completed

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


def fetch_data_multithread(url:str):

    response = requests.get(url)
    response_json = response.json()
    if not response_json:
        raise "Empty data"
    object_type = url.split('/')[-1]
    base_url = f'https://rickandmortyapi.com/api/{object_type}?page='
    number_pages = int(response_json['info']['pages'])
    pages_url_list = []

    for page in range(2, number_pages + 1):
        new_url = base_url + str(page)
        pages_url_list.append(new_url)

    threads = []
    with ThreadPoolExecutor(max_workers=15) as executor:
        for page_url in pages_url_list:
            threads.append(executor.submit(aux_fetch, page_url))
        for task in as_completed(threads):
            response_json['results'] += task.result()['results']

    return response_json

def aux_fetch(url):
    return requests.get(url).json()





def rick_and_morty_solution():
    try:
        #Start time measurement for first exercise
        start = datetime.now()

        #Get the responses for each list
        #characters_response = fetch_data(characters_url)
        #episodes_response = fetch_data(episodes_url)
        #locations_response = fetch_data(locations_url)

        #Get the json(dict) information from the response
        characters_json = fetch_data_multithread(characters_url)
        episodes_json = fetch_data_multithread(episodes_url)
        locations_json = fetch_data_multithread(locations_url)

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


