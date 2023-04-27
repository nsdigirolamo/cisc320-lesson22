import unittest
import answer

class TestProcessLines(unittest.TestCase):

    def test_single_item (self):
        input = [
            "Pencil 1 5\n",
        ]
        actual_output = answer.process_lines(input)
        expected_output = [
            {"name": "Pencil", "weight": 1, "value": 5},
        ]
        self.assertEqual(actual_output, expected_output)

    def test_given_example (self):
        input = [
            "Textbook 4 50\n",
            "HardDrive 10 2\n",
            "DogFood 10 5\n",
            "FavoriteGame 20 60\n",
            "SuperComputer 100 100\n",
        ]
        actual_output = answer.process_lines(input)
        expected_output = [
            {"name": "Textbook", "weight": 4, "value": 50},
            {"name": "HardDrive", "weight": 10, "value": 2},
            {"name": "DogFood", "weight": 10, "value": 5},
            {"name": "FavoriteGame", "weight": 20, "value": 60},
            {"name": "SuperComputer", "weight": 100, "value": 100},
        ]
        self.assertEqual(actual_output, expected_output)

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
        actual_output = answer.process_lines(input)
        expected_output = [
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
        self.assertEqual(actual_output, expected_output)
    
class TestGenerateValueTable(unittest.TestCase):

    def test_single_item (self):
        items = [
            {"name": "Pencil", "weight": 1, "value": 5},
        ]
        row_count = 1
        col_count = 6 # max_capacity is 5
        actual_output = answer.generate_value_table(items, row_count, col_count)
        expected_output = [
            [0, 5, 5, 5, 5, 5]
        ]
        self.assertEqual(actual_output, expected_output)

    def test_overweight_item (self):
        items = [
            {"name": "Anvil", "weight": 100, "value": 1},
        ]
        row_count = 1
        col_count = 6 # max_capacity is 5
        actual_output = answer.generate_value_table(items, row_count, col_count)
        expected_output = [
            [0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(actual_output, expected_output)

    def test_two_items_different_weight_and_value (self):
        items = [
            {"name": "Pencil", "weight": 1, "value": 5},
            {"name": "Notebook", "weight": 4, "value": 10},
        ]
        row_count = 2
        col_count = 6 # max_capacity is 5
        actual_output = answer.generate_value_table(items, row_count, col_count)
        expected_output = [
            [0, 5, 5, 5, 5, 5],
            [0, 5, 5, 5, 10, 15],
        ]
        self.assertEqual(actual_output, expected_output)

    def test_two_items_same_weight_and_value (self):
        items = [
            {"name": "Pencil", "weight": 1, "value": 5},
            {"name": "Pen", "weight": 1, "value": 5},
        ]
        row_count = 2
        col_count = 6 # max_capacity is 5
        actual_output = answer.generate_value_table(items, row_count, col_count)
        expected_output = [
            [0, 5, 5, 5, 5, 5],
            [0, 5, 10, 10, 10, 10],
        ]
        self.assertEqual(actual_output, expected_output)

    def test_two_items_one_exceeds_max (self):
        items = [
            {"name": "Pencil", "weight": 1, "value": 5},
            {"name": "Anvil", "weight": 100, "value": 15},
        ]
        row_count = 2
        col_count = 6 # max_capacity is 5
        actual_output = answer.generate_value_table(items, row_count, col_count)
        expected_output = [
            [0, 5, 5, 5, 5, 5],
            [0, 5, 5, 5, 5, 5],
        ]
        self.assertEqual(actual_output, expected_output)

    def test_three_items_one_much_better_value (self):
        items = [
            {"name": "Notebook", "weight": 5, "value": 5},
            {"name": "PencilCase", "weight": 15, "value": 10},
            {"name": "WaterBottle", "weight": 5, "value": 30},
        ]
        row_count = 3
        col_count = 16 # max_capacity is 15
        actual_output = answer.generate_value_table(items, row_count, col_count)
        expected_output = [
            [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10],
            [0, 0, 0, 0, 0, 30, 30, 30, 30, 30, 35, 35, 35, 35, 35, 35],
        ]
        self.assertEqual(actual_output, expected_output)

    def test_given_example (self):
        items = [
            {"name": "Textbook", "weight": 4, "value": 50},
            {"name": "HardDrive", "weight": 10, "value": 2},
            {"name": "DogFood", "weight": 10, "value": 5},
            {"name": "FavoriteGame", "weight": 20, "value": 60},
            {"name": "SuperComputer", "weight": 100, "value": 100},
        ]
        row_count = 5
        col_count = 16 # max_capacity is 15
        actual_output = answer.generate_value_table(items, row_count, col_count)
        expected_output = [
            [0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
            [0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 52, 52],
            [0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 55, 55],
            [0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 55, 55],
            [0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 55, 55],
        ]
        self.assertEqual(actual_output, expected_output)

class TestSelectItems(unittest.TestCase):

    def test_single_item (self):
        items = [
            {"name": "Pencil", "weight": 1, "value": 5},
        ]
        table = [
            [0, 5, 5, 5, 5, 5]
        ]
        actual_output = answer.select_items(items, table)
        expected_output = [
            {"name": "Pencil", "weight": 1, "value": 5},
        ]
        self.assertEqual(actual_output, expected_output)

    def test_overweight_item (self):
        items = [
            {"name": "Anvil", "weight": 100, "value": 1},
        ]
        table = [
            [0, 0, 0, 0, 0, 0]
        ]
        actual_output = answer.select_items(items, table)
        expected_output = [

        ]
        self.assertEqual(actual_output, expected_output)

    def test_two_items_different_weight_and_value (self):
        items = [
            {"name": "Pencil", "weight": 1, "value": 5},
            {"name": "Notebook", "weight": 4, "value": 10},
        ]
        table = [
            [0, 5, 5, 5, 5, 5],
            [0, 5, 5, 5, 10, 15],
        ]
        actual_output = answer.select_items(items, table)
        expected_output = [
            {"name": "Pencil", "weight": 1, "value": 5},
            {"name": "Notebook", "weight": 4, "value": 10},
        ]
        self.assertEqual(actual_output, expected_output)

    def test_three_items_one_much_better_value (self):
        items = [
            {"name": "Notebook", "weight": 5, "value": 5},
            {"name": "PencilCase", "weight": 15, "value": 10},
            {"name": "WaterBottle", "weight": 5, "value": 30},
        ]
        table = [
            [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10],
            [0, 0, 0, 0, 0, 30, 30, 30, 30, 30, 35, 35, 35, 35, 35, 35],
        ]
        actual_output = answer.select_items(items, table)
        expected_output = [
            {"name": "Notebook", "weight": 5, "value": 5},
            {"name": "WaterBottle", "weight": 5, "value": 30},
        ]
        self.assertEqual(actual_output, expected_output)

    def test_given_example (self):
        items = [
            {"name": "Textbook", "weight": 4, "value": 50},
            {"name": "HardDrive", "weight": 10, "value": 2},
            {"name": "DogFood", "weight": 10, "value": 5},
            {"name": "FavoriteGame", "weight": 20, "value": 60},
            {"name": "SuperComputer", "weight": 100, "value": 100},
        ]
        table = [
            [0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
            [0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 52, 52],
            [0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 55, 55],
            [0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 55, 55],
            [0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 55, 55],
        ]
        actual_output = answer.select_items(items, table)
        expected_output = [
            {"name": "Textbook", "weight": 4, "value": 50},
            {"name": "DogFood", "weight": 10, "value": 5},
        ]
        self.assertEqual(actual_output, expected_output)