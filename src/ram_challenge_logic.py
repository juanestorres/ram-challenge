import requests
import traceback
import json
from datetime import datetime
from .char_counter import char_counter
from .episode_locations import episode_locations
from concurrent.futures import ThreadPoolExecutor, as_completed

#API's urls. Just in case they may change in the future.
characters_url = 'https://rickandmortyapi.com/api/character'
episodes_url = "https://rickandmortyapi.com/api/episode"
locations_url = 'https://rickandmortyapi.com/api/location'

def fetch_data(url):
    """Fetches the API data using requests module in a sequential way.

    Args:
        url (string): The API's url where the data comes from.

    Returns:
        [Dict]: Returns the response content in json (dict) format.
    """

    #Get first response
    response = requests.get(url)
    response_json = response.json()
    #Get the next page url
    next_page_url = response_json["info"]["next"]

    #Check if that url is not empty.
    while next_page_url: 
        #Get the new response and append the results to thee first one.
        new_response = requests.get(next_page_url)
        new_response_json = new_response.json()
        response_json['results'] += new_response_json['results']
        next_page_url = new_response_json["info"]["next"]
    return  response_json


def fetch_data_multithread(url:str):
    """Fetches the API data using requests module in a multithreaded way.

    Args:
        url (string): The API's url where the data comes from.

    Returns:
        [Dict]: Returns the response content in json (dict) format.
    """
    #Get the first response
    response = requests.get(url)
    response_json = response.json()

    #Check if the response is not empty.
    if not response_json:
        raise "Empty data"
    #Check if the url is either for episodes, locations or character
    object_type = url.split('/')[-1]
    #Create the base url based on the type
    base_url = f'https://rickandmortyapi.com/api/{object_type}?page='

    #Create a list with all the urls (for all the pages)
    number_pages = int(response_json['info']['pages'])
    pages_url_list = []
    for page in range(2, number_pages + 1):
        new_url = base_url + str(page)
        pages_url_list.append(new_url)

    print(str(number_pages) + " ---- " + pages_url_list[-1])

    #Create a Thread Pool for executing all the API's calls and then merge all the results
    threads = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        for page_url in pages_url_list:
            threads.append(executor.submit(aux_fetch, page_url))
        for task in as_completed(threads):
            response_json['results'] += task.result()['results']

    #Sort the results since they are no longer ordered
    response_json['results'] = sorted(response_json['results'], key=lambda d: d['id'])
    print("Size: " + str(len(response_json["results"])) + ". " + str(response_json["results"][-1]["id"]))

    return response_json

def aux_fetch(url):
    """Aux function that Fetches the API data using requests module

    Args:
        url (string): The API's url where the data comes from.

    Returns:
        Returns the response content in json (dict) format.
    """
    return requests.get(url).json()





def rick_and_morty_solution(local):
    """Main function responsable for getting the API data and delegating each exercise to it's own module.

    Args:
        local (Bool): Determine if the function will run in a local environment or in production. 

    Returns:
        [Dict]: Json (dict) with the answers of each exercise.
    """
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

        #Get json answer for char counter exercise.
        char_counter_json = char_counter(characters_json, episodes_json, locations_json, start)

        #Start time measurement for second exercise
        start = datetime.now()

        #Get json answer for the episode locations exercise.
        episode_locations_json = episode_locations(characters_json, episodes_json, start)

        #Create Json file
        answers = [char_counter_json, episode_locations_json]
        #print(answers)
        json_file = answers
        if local:
            with open('results.json', 'w') as file:
                file.write(json_file)
                file.close()
        else:
            return json_file

    except Exception:
        print("There was an error fetching the information. " + str(traceback.format_exc()))



