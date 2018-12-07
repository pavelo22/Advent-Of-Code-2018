import time


def fully_react(_data, _replacements):
    need_to_repeat = True
    while need_to_repeat:
        need_to_repeat = False
        for replacement in _replacements:
            if replacement in _data:
                _data = _data.replace(replacement, '')

        for replacement in _replacements:
            if replacement in _data:
                need_to_repeat = True
                break
    return _data


def prepare_replacements():
    _replacements = []
    for i in range(ord('a'), ord('z') + 1):
        s1 = chr(i) + chr(i).upper()
        s2 = chr(i).upper() + chr(i)
        _replacements.append(s1)
        _replacements.append(s2)
    return _replacements


with open('data') as file_in:
    data = file_in.read()

start = time.time()
replacements = prepare_replacements()
new_data = fully_react(data, replacements)
print('Part1:', len(new_data))
duration = time.time() - start
print('Duration: {0:.3} seconds'.format(duration))

start = time.time()
min_len = 1000000
for i in range(ord('a'), ord('z') + 1):
    new_data = data.replace(chr(i), '').replace(chr(i).upper(), '')
    new_data = fully_react(new_data, replacements)
    min_len = min(min_len, len(new_data))
print('Part2:', min_len)
duration = time.time() - start
print('Duration: {0:.3} seconds'.format(duration))
