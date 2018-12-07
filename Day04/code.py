import time


def get_next_day(_dates, day):
    my_precious = 0
    for idx, element in enumerate(_dates):
        if element == day:
            my_precious = idx
            break

    return _dates[my_precious + 1]


with open('data') as file_in:
    data = file_in.read().split('\n')

start = time.time()
data = sorted(data)

dates = list()
for element in data:
    row = element.split('] ')
    day = row[0].replace('[', '').split(' ')
    dates.append(day[0])

dates = sorted(set(dates))

all_records = list()
for element in data:
    genuine = str(element)
    row = element.split(']')
    day, hour = row[0].replace('[', '').split(' ')
    if hour.startswith('23'):
        day = get_next_day(dates, day)
        hour = '00:00'
    creme = element.find(']')
    new_string = '[%s %s]%s' % (day, hour, element[creme + 1:])
    all_records.append(new_string)

data = all_records
guard_id = ''
start_hour = ''
stop_hour = ''
start_hour2 = 0
stop_hour2 = 0

new_new = list()

i = 0
while i < len(data):
    words = data[i].split(' ')
    if data[i].find('Guard') > 0:
        guard_id = words[-3].replace('#', '')
    elif data[i].find('falls') > 0:
        start_hour = words[1].replace(']', '')
        start_hour2 = int(start_hour.replace('00:', ''))
    elif data[i].find('wakes') > 0:
        if start_hour == '':
            print('problem1_' * 10)
        stop_hour = words[1].replace(']', '')
        stop_hour2 = int(stop_hour.replace('00:', ''))
        date = words[0].replace('[', '')
        new_new.append((date, guard_id, start_hour2, stop_hour2))
        start_hour = ''
        start_hour2 = 0
    else:
        print(data[i])
        print('problem2_' * 10)

    i += 1

big_dict = dict()
for element in new_new:
    date = element[0]

    if date not in big_dict:
        big_dict[date] = dict()
        big_dict[date]['id'] = element[1]
        big_dict[date]['minutes'] = ['.'] * 60

    for i in range(element[2], element[3]):
        big_dict[date]['minutes'][i] = '#'

sums = dict()
for record in big_dict:
    hashes = big_dict[record]['minutes'].count('#')
    if big_dict[record]['id'] not in sums:
        sums[big_dict[record]['id']] = 0

    sums[big_dict[record]['id']] += hashes

max_x = 0
max_id = ''
for record in sorted(sums):
    if sums[record] > max_x:
        max_x = sums[record]
        max_id = record

sums = [0] * 60
for key in big_dict:
    if big_dict[key]['id'] == max_id:
        for minute in range(0, 60):
            if big_dict[key]['minutes'][minute] == '#':
                sums[minute] += 1

max_position = sums.index(max(sums))
print("{} * {} = {}".format(max_id, max_position, int(max_id) * max_position))

guard_ids = set([big_dict[key]['id'] for key in big_dict.keys()])
guards = dict()
for key in guard_ids:
    guards[key] = [0] * 60

for element in big_dict:
    for day in range(0, 60):
        if big_dict[element]['minutes'][day] == "#":
            guards[big_dict[element]['id']][day] += 1

max_id = 0
max_val = 0
for guard_id in guards.keys():
    if max_val < max(guards[guard_id]):
        max_val = max(guards[guard_id])
        max_id = guard_id

for element in range(0, 60):
    if guards[max_id][element] == max_val:
        print("{} * {} = {}".format(max_id, element, int(max_id) * element))
        break

duration = time.time() - start
print('Duration: {0:.3} seconds'.format(duration))
