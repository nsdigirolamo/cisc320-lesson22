"""
Nicholas DiGirolamo
CISC320 Lesson 22 - Devouring Doggos
April 21, 2023
"""

def process_lines(lines: list[str]) -> list[dict]:
    items = []
    for line in lines:
        info = line.split()
        items.append({
            "name": info[0].strip(),
            "weight": int(info[1]),
            "value": int(info[2]),
        })
    return items

if __name__ == "__main__":

    # filename = input()
    filename = "input.txt"
    with open(filename) as f: lines = f.readlines()

    count = int(lines.pop(0).strip())
    max_capacity = int(lines.pop(0).strip())
    items = process_lines(lines)

    row_count = count
    col_count = max_capacity + 1

    value_table = [[0 for i in range(max_capacity + 1)] for j in range(count)]

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

    for i in range(0, count):
        print(f"{'Name: ' + items[i]['name']:<20} {'Weight: ' + str(items[i]['weight']):<15} {'Value: ' + str(items[i]['value']):<15} {value_table[i]}")

    selected_items = []

    row = row_count - 1
    col = col_count - 1
    value = value_table[row][col]

    while value != 0:
        if value != value_table[row - 1][col] or row == 0:
            selected = items[row]
            selected_items.append(selected)
            value = value - selected["value"]
            col = col - selected["value"]
        row = row - 1

    for item in selected_items:
        print(f"{item['name']}")

