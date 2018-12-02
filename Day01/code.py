import time


def part1(data):
    new_elements = [int(x) for x in data]
    suma = sum(new_elements)
    print('Part1:', suma, end='')
    return new_elements


def part2(new_elements):
    suma = 0
    idx = 0
    elements = len(new_elements)
    sums = dict()

    while True:
        suma += new_elements[idx % elements]
        if suma not in sums:
            sums[suma] = 0
        else:
            print('Part2:', suma, end='')
            break
        idx += 1


with open('data', 'r') as file_in:
    data = file_in.read().split()

start = time.time()
data1 = part1(data)
duration = time.time() - start
print('\t\tDuration: {0:.3} seconds'.format(duration))

start = time.time()
part2(data1)
duration = time.time() - start
print('\t\tDuration: {0:.3} seconds'.format(duration))
