"""
Nicholas DiGirolamo
CISC320 Lesson 22 - Devouring Doggos
April 21, 2023
"""

def process_lines (lines: list[str]) -> list[dict]:
    items = []
    for line in lines:
        info = line.split()
        items.append({
            "name": info[0].strip(),
            "weight": int(info[1]),
            "value": int(info[2]),
        })
    return items

def generate_value_table (items: list[dict], row_count: int, col_count: int) -> list[int]:

    value_table = [[0 for i in range(col_count)] for j in range(row_count)]

    for row in range(0, row_count):
        for col in range(0, col_count):
            item = items[row]
            capacity = col
            if row == 0:
                if capacity < item["weight"]:
                    value_table[row][col] = 0
                else:
                    value_table[row][col] = item["value"]
            else:
                prev_value = value_table[row - 1][col]
                if capacity < item["weight"]:
                    value_table[row][col] = prev_value
                else:
                    current_value = value_table[row - 1][col - item["weight"]] + item["value"]
                    value_table[row][col] = max(prev_value, current_value)

    return value_table

def select_items (items: list[dict], table: list[int]) -> list[dict]:

    selected_items = []

    row = len(table) - 1
    col = len(table[row]) - 1
    value = value_table[row][col]

    while value != 0:
        if value != value_table[row - 1][col] or row == 0:
            selected = items[row]
            selected_items.append(selected)
            value = value - selected["value"]
            col = col - selected["value"]
        row = row - 1

    return selected_items

def print_table (items: list[dict], table: list[int]) -> None:
    for i in range(0, len(items)):
        prefix = f"{'Name: ' + items[i]['name']:<25}"
        prefix += f"{'Weight: ' + str(items[i]['weight']):<15}"
        prefix += f"{'Value: ' + str(items[i]['value']):<15} "
        print(prefix + f"{value_table[i]}")

if __name__ == "__main__":

    # filename = input()
    filename = "input.txt"
    with open(filename) as f: lines = f.readlines()

    count = int(lines.pop(0).strip())
    max_capacity = int(lines.pop(0).strip())
    items = process_lines(lines)

    row_count = count
    col_count = max_capacity + 1
    value_table = generate_value_table(items, row_count, col_count)

    print_table(items, value_table)

    selected_items = select_items(items, value_table)

    for item in selected_items:
        print(f"{item['name']}")

