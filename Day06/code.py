import time

with open('data') as file_in:
    data = file_in.read().split('\n')

start = time.time()

new_data = dict()
max_x = 0
max_y = 0

for idx, element in enumerate(data):
    x, y = element.split(', ')
    max_x = max(max_x, int(x))
    max_y = max(max_y, int(y))
    new_data['A' + str(idx).zfill(3)] = (int(x), int(y))

field = list()
for row in range(max_y + 2):
    new_row = list()
    for element in range(max_x + 2):
        new_row.append(dict())
    field.append(new_row)

for point in new_data:
    point_x = new_data[point][0]
    point_y = new_data[point][1]

    for y in range(max_y + 2):
        for x in range(max_x + 2):
            if isinstance(field[y][x], str):
                continue
            distance = abs(x - point_x) + abs(y - point_y)
            field[y][x][point] = distance

all_results = list()
for y in range(max_y + 2):
    row = ''
    for x in range(max_x + 2):
        if isinstance(field[y][x], str):
            row += field[y][x]
            continue
        min_val = min(list(field[y][x].values()))

        if list(field[y][x].values()).count(min_val) > 1:
            row += '.'
            continue
        for key in field[y][x].keys():
            if field[y][x][key] == min_val:
                row += key.lower()
                break
    all_results.append(row)

borders = all_results[0] + '-' + all_results[-1]
for i in range(1, len(all_results) - 1):
    borders += all_results[i][0:4] + all_results[i][-4:]

rectangle = "\n".join(all_results)
for character in new_data.keys():
    if character.lower() in borders:
        rectangle = rectangle.replace(character.lower(), '')
        rectangle = rectangle.replace(character, '')

max_char = ''
max_val = -1
for candidate in new_data.keys():
    c_lower = candidate.lower()
    if rectangle.lower().count(c_lower) > max_val:
        max_char = c_lower
        max_val = rectangle.lower().count(c_lower)

print('Part1:', max_val)

counter = 0
for row in field:
    for column in row:
        suma = sum(column.values())
        if suma < 10000:
            counter += 1

print('Part2:', counter)

duration = time.time() - start
print('Duration: {0:.3} seconds'.format(duration))
