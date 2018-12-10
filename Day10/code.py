import re
import time

class Star:
    def __init__(self, x, y, v_x, v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

    def move(self):
        self.x += self.v_x
        self.y += self.v_y


def display_stars(stars, i):
    x_list = list()
    y_list = list()

    for star in stars:
        x_list.append(star.x)
        y_list.append(star.y)

    min_x = min(x_list)
    min_y = min(y_list)
    max_x = max(x_list)
    max_y = max(y_list)

    dy = max_y - min_y
    dx = max_x - min_x

    if dx < 10 or dy < 10:
        points = dict()
        for star in stars:
            point_x = star.x - min_x
            point_y = star.y - min_y
            points[(point_y, point_x)] = '*'

        for y in range(dy+1):
            string = ''
            for x in range(dx+1):
                if (y,x) in points:
                    string = string + '*'
                else:
                    string = string + '.'
            print(string)
        return True

    return False

with open('data') as file_in:
    data = file_in.read()


start = time.time()

data = data.split('\n')
pattern = 'position=<(.*),(.*)> velocity=<(.*),(.*)>'
stars = list()

for row in data:
    matchobj = re.match(pattern, row)
    star_x, star_y, star_v_x, star_v_y = matchobj.groups()
    star = Star(int(star_x), int(star_y), int(star_v_x), int(star_v_y))
    stars.append(star)

i=0
found = False
print('Part1:')

while not found:
    found = display_stars(stars, i)
    for star in stars:
        star.move()
    i+=1

print('Part2:', i)

duration = time.time() - start
print('Duration: {0:.3} seconds'.format(duration))
