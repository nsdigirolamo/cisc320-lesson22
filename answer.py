"""
Nicholas DiGirolamo
CISC320 Lesson 22 - Devouring Doggos
April 21, 2023
"""

def process_items(lines: list[str]) -> list[dict]:
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

    count = lines.pop(0).strip()
    capacity = lines.pop(0).strip()
    items = process_lines(lines)
    
        