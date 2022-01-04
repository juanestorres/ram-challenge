import unittest
from episode_locations import episode_locations
import json
from datetime import datetime
import os

TESTDATA_1_FILENAME = os.path.join(os.path.dirname(__file__), 'episode1-characters.json')
TESTDATA_2_FILENAME = os.path.join(os.path.dirname(__file__), 'episode-test.json')

class TestCountCharacter(unittest.TestCase):
    def test_character(self):
        with open(TESTDATA_1_FILENAME, 'r', encoding="utf-8") as f:
            characters_json = json.loads(f.read())
            f.close()
        with open(TESTDATA_2_FILENAME, 'r', encoding="utf-8") as f:
            episodes_json = json.loads(f.read())
            f.close()
        start = datetime.now()
        response = episode_locations(characters_json, episodes_json, start)
        result = response["results"][0]["locations"]

        solution = [
        "Earth (C-137)",
        "unknown",
        "Bepis 9",
        "Gromflom Prime",
        "Girvonesk"
        ]
        self.assertEqual(set(result), set(solution), "Should be 5 locations.")

if __name__ == '__main__':

    unittest.main()