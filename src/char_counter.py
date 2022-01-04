from datetime import datetime
from datetime import timedelta

#Key names from the API. Just in case they may change in the future.
api_results = 'results'
api_name = "name"

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
        counter += current_name.lower().count(char)
    #return the total count
    return counter

def char_counter(characters_json, episodes_json, locations_json, start):
    """Function that solves the first exercise.

    Args:
        characters_json ([dict]): The json(dict) data for the characters.
        episodes_json ([dict]): The json(dict) data for the episodes.
        locations_json ([dict]): The json(dict) data for the locations.
        start ([datetime]): datetime of the start of the solution.

    Returns:
        [dict]: Json (dict) containing the expected answer for the first exercise.
    """
    #Final answer json(dictionary)
    first_answer = {
        "exercise_name": "Char counter",
            "time": "",
            "in_time": False,
            "results": [
                {
                    "char": "l",
                    "count": 0,
                    "resource": "location"
                },
                {
                    "char": "e",
                    "count": 0,
                    "resource": "episode"
                },
                {
                    "char": "c",
                    "count": 0,
                    "resource": "character"
                }
            ]
    }

    #Call the auxiliary function to count the occurrences depending on which  "list" of data is
    characters_counter = count_character(characters_json,'c')
    episodes_counter =  count_character(episodes_json, 'e')
    location_counter =  count_character(locations_json, 'l')

    #print(f"Finished fetching the data. Results c: {characters_counter}, e: {episodes_counter}, l: {location_counter}")

    #Calculate time and check if the process was on time
    time_used = datetime.now() - start
    seconds_used_str = str(time_used.seconds)
    milliseconds_used_str = str(round(time_used.microseconds / 1000, 3))
    time_used_str = seconds_used_str + "s " + milliseconds_used_str + "ms"
    in_time = time_used < timedelta(seconds=3)

    #Add values to json
    first_answer["time"] = time_used_str
    first_answer["in_time"] = in_time
    first_answer["results"][0]["count"] = location_counter
    first_answer["results"][1]["count"] = episodes_counter
    first_answer["results"][2]["count"] = characters_counter

    #print(str(first_answer))
    return first_answer

