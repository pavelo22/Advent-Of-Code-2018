import re
import time

with open('data') as file_in:
    data = file_in.read().split('\n')

start = time.time()

begin2end = dict()
end2begin = dict()
pattern = 'Step (.) must be finished before step (.) can begin.'

for element in data:
    matchobj = re.match(pattern=pattern, string=element)
    parent, child = matchobj.groups()
    if parent not in begin2end:
        begin2end[parent] = list()
    begin2end[parent].append(child)

    if child not in end2begin:
        end2begin[child] = list()
    end2begin[child].append(parent)

for element in begin2end:
    begin2end[element] = sorted(set(begin2end[element]))
for element in end2begin:
    end2begin[element] = sorted(set(end2begin[element]))

children = list(end2begin.keys())
parents = list(begin2end.keys())

for child in children:
    if child in parents:
        parents.remove(child)

all_nodes_len = len(set(children + parents))

the_path = ''
next_steps = list(parents)

while len(the_path) < all_nodes_len:
    next_steps = sorted(set(next_steps))
    for candidate in next_steps:
        if candidate not in end2begin:
            the_path += candidate
            next_steps.remove(candidate)
            next_steps.extend(begin2end[candidate])
            break

        the_result = True
        for pp in end2begin[candidate]:
            if the_path.count(pp) == 0:
                the_result = False

        if not the_result:
            continue

        the_path += candidate
        next_steps.remove(candidate)
        if candidate in begin2end:
            next_steps.extend(begin2end[candidate])
        break

print('Part1:', the_path)

duration = time.time() - start
print('Duration: {0:.3} seconds'.format(duration))
start = time.time()

workers = [''] * 5

for idx, parent in enumerate(parents):
    workers[idx] = parent * (ord(parent) - ord('A') + 61)
    the_path = the_path.replace(parent, '')

second = 0
done = ''

while the_path !=''  or "".join(workers) !='':
    for idx, worker in enumerate(workers):
        if len(worker) == 1:
            done += worker[0]
            workers[idx] = ''
        else:
            workers[idx] = worker[1:]

    for idx, worker in enumerate(workers):
        if worker == '':

            for candidate in the_path:
                result = True
                for parent in end2begin[candidate]:
                    if parent not in done:
                        result = False

                if result:
                    workers[idx] = candidate * (ord(candidate) - ord('A') + 61)
                    the_path = the_path.replace(candidate, '')
                    break

    second += 1

print('Part2:', second)
duration = time.time() - start
print('Duration: {0:.3} seconds'.format(duration))
