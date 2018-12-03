import re
import time


def pre_process_data(_data):
    pattern = '#(.*) @ (.*),(.*): (.*)x(.*)'
    _parcels = list()
    x_egdes = list()
    y_egdes = list()

    for a in _data:
        matchobj = re.match(pattern, a)
        properties = [int(x) for x in matchobj.groups()]
        _parcels.append(properties)

        x_egdes.append(properties[1] + properties[3])
        y_egdes.append(properties[2] + properties[4])

    return _parcels, max(x_egdes), max(y_egdes)


def prepare_field(_max_y, _max_x):
    ids_field = list()

    for idx_y in range(_max_y + 1):
        ids_row = [[] for _ in range(_max_x + 1)]
        ids_field.append(ids_row)
    return ids_field


def main_processing(_data):
    parcels, max_x, max_y = pre_process_data(_data)
    ids_field = prepare_field(max_y, max_x)

    for parcel in parcels:
        for y in range(parcel[2], parcel[2] + parcel[4]):
            for x in range(parcel[1], parcel[1] + parcel[3]):
                ids_field[y][x].append(parcel[0])

    counter = 0
    ids = {parcel[0]: True for parcel in parcels}
    for row in ids_field:
        for element in row:
            if len(element) > 1:
                counter += 1
                for parcel_id in element:
                    ids[parcel_id] = False

    print('Part1:', counter)
    for element in ids:
        if ids[element]:
            print('Part2:', element)
            break


with open('data') as file_in:
    data = file_in.read().split('\n')

start = time.time()
main_processing(data)
duration = time.time() - start
print('Duration: {0:.3} seconds'.format(duration))
