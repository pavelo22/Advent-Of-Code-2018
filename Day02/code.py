import time


def part1(data):
    twos = 0
    threes = 0
    for row in data:
        letters = set(row)
        ddict = {i: row.count(i) for i in letters}

        if 2 in ddict.values():
            twos += 1
        if 3 in ddict.values():
            threes += 1

    suma = twos * threes
    print('Part1:', suma, end='')


def compare_labels(label1, label2):
    commons = ''
    for i in range(len(label1)):
        if label1[i] == label2[i]:
            commons += label2[i]

    return len(commons) == len(label2) - 1, commons


def part2(fabric_boxes):
    num_fabric_boxes = len(fabric_boxes)

    for id1 in range(num_fabric_boxes - 1):
        for id2 in range(id1 + 1, num_fabric_boxes):
            result, commons = compare_labels(fabric_boxes[id1], fabric_boxes[id2])
            if result:
                print('Part2:', commons, end='')
                break

    return 0


with open('data', 'r') as file_in:
    data = file_in.read().split()

start = time.time()
part1(data)
duration = time.time() - start
print('\t\tDuration: {0:.3} seconds'.format(duration))

start = time.time()
part2(data)
duration = time.time() - start
print('\t\tDuration: {0:.3} seconds'.format(duration))
