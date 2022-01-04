from datetime import datetime
from datetime import timedelta

def episode_locations(characters_json, episodes_json, start):
    #Final answer json(dictionary)
    second_answer = {
        "exercise_name": "Episode locations",
        "time": "",
        "in_time": False,
    }
    episodes_list=episodes_json["results"]
    characters_list = characters_json["results"]
    results = []
    for episode in episodes_list:
        locations= []
        locations_size = 0
        characters_in_episode = episode["characters"]
        print("---------")
        for character in characters_in_episode:
            character_id = int(character.split('/')[-1]) - 1
            if character_id > len(characters_list) - 1:
                break
            print(character_id + 1)
            character_data = characters_list[character_id]
            character_origin = character_data["origin"]["name"]
            if character_origin not in locations:
                locations.append(character_origin)
                locations_size+= 1
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



