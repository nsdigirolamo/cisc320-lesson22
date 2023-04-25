import unittest
import answer

class TestProcessLines(unittest.TestCase):

    def test_given_example (self):
        input = [
            "Textbook 4 50\n",
            "HardDrive 10 2\n",
            "DogFood 10 5\n",
            "FavoriteGame 20 60\n",
            "SuperComputer 100 100\n",
        ]
        actual_ouput = answer.process_lines(input)
        expected_ouput = [
            {"name": "Textbook", "weight": 4, "value": 50},
            {"name": "HardDrive", "weight": 10, "value": 2},
            {"name": "DogFood", "weight": 10, "value": 5},
            {"name": "FavoriteGame", "weight": 20, "value": 60},
            {"name": "SuperComputer", "weight": 100, "value": 100},
        ]
        self.assertEqual(actual_ouput, expected_ouput)

    def test_ten_items (self):
        input = [
            "Basketball 10 10\n",
            "Textbook 4 50\n",
            "CatFood 10 0\n",
            "HardDrive 10 2\n",
            "Laptop 15 5\n",
            "DogFood 10 5\n",
            "DogToy 5 50\n",
            "FavoriteGame 20 60\n",
            "TV 50 2\n",
            "SuperComputer 100 100\n",
        ]
        actual_ouput = answer.process_lines(input)
        expected_ouput = [
            {"name": "Basketball", "weight": 10, "value": 10},
            {"name": "Textbook", "weight": 4, "value": 50},
            {"name": "CatFood", "weight": 10, "value": 0},
            {"name": "HardDrive", "weight": 10, "value": 2},
            {"name": "Laptop", "weight": 15, "value": 5},
            {"name": "DogFood", "weight": 10, "value": 5},
            {"name": "DogToy", "weight": 5, "value": 50},
            {"name": "FavoriteGame", "weight": 20, "value": 60},
            {"name": "TV", "weight": 50, "value": 2},
            {"name": "SuperComputer", "weight": 100, "value": 100},
        ]
        self.assertEqual(actual_ouput, expected_ouput)