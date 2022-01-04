from datetime import datetime
from datetime import timedelta

def episode_locations(characters_json, episodes_json, start):

    #Final answer json(dictionary)
    second_answer = {
        "exercise_name": "Episode locations",
        "time": "",
        "in_time": False,
    }

    #Extract the episodes and characters (ordered) list and create an empty list to append the results
    episodes_list=episodes_json["results"]
    characters_list = characters_json["results"]
    results = []


    for episode in episodes_list:
        #Set a new array of locations and its size. Besides, getting the chracters that appeared in that episode
        locations= []
        locations_size = 0
        characters_in_episode = episode["characters"]
        
        for character in characters_in_episode:
            #Get the character id and access its information from the list (which is ordered).
            character_id = int(character.split('/')[-1]) - 1
            character_data = characters_list[character_id]
            character_origin = character_data["origin"]["name"]
            #Check if that location is not already in the list. if so then add it.
            if character_origin not in locations:
                locations.append(character_origin)
                locations_size+= 1
        
        #Create the json structure and append the result
        result = {
                "name": episode["name"],
                "episode": episode["episode"],
                "locations": locations
            }
        results.append(result)

    #Calculate time and check if the process was on time
    time_used = datetime.now() - start
    seconds_used_str = str(time_used.seconds)
    milliseconds_used_str = str(round(time_used.microseconds / 1000, 3))
    time_used_str = seconds_used_str + "s " + milliseconds_used_str + "ms"
    in_time = time_used < timedelta(seconds=3)

    #Add values to json
    second_answer["time"] = time_used_str
    second_answer["in_time"] = in_time
    second_answer["results"] =  results

    return second_answer



