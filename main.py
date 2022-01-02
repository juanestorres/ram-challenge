import requests

#Key names from the API. Just in case they may change in the future.
api_results = 'results'
api_name = "name"

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

def count_character(json_data, char):
    """[summary]

    Args:
        json_data ([type]): [description]
        char ([type]): [description]

    Returns:
        [type]: [description]
    """    
    #Extract the results from the API response's JSON.
    results = json_data[api_results]

    #Auxiliary variables to store the current name and a counter to keep record of how many times the char has appeared
    current_name = str()
    counter = 0

    #For loop over each result
    for result in results:
        current_name = result[api_name]
        #Use str method to count the occurrences
        counter += current_name.count(char)
    #return the total count
    return counter

try:
    #Get the responses for each list
    characters_response = fetch_data(characters_url)
    episodes_response = fetch_data(episodes_url)
    locations_response = fetch_data(locations_url)

    #Get the json(dict) information from the response
    characters_json = characters_response.json()
    episodes_json = episodes_response.json()
    locations_json = locations_response.json()

    #Call the auxiliary function to count the occurrences depending on which  "list" of data is
    characters_counter = count_character(characters_json,'c')
    episodes_counter =  count_character(episodes_json, 'e')
    location_counter =  count_character(locations_json, 'l')

    print(f"Finished fetching the data. Results c: {characters_counter}, e: {episodes_counter}, l: {location_counter}")

except Exception as e:
    print("There was an error fetching the information. " + str(e))