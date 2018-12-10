import collections
import time

def play_player(the_circle, designated, players, player, position):
    if designated % 23 == 0:
        llen = len(the_circle)
        idx = (position - 6) % llen
        the_circle.rotate(-idx)
        players[player] += the_circle.popleft() + designated
        the_circle.rotate(idx)
        idx = (idx - 1) % llen
    else:
        idx = (position + 2) % len(the_circle)
        the_circle.rotate(-idx-1)
        the_circle.appendleft(designated)
        the_circle.rotate(idx+1)

    return the_circle, idx

def run_the_game(cycles):
    no_players = 404
    players = {i: 0 for i in range(1, no_players + 1)}

    the_circle = collections.deque()
    the_circle.append(0)
    designated = 0
    player = 1
    position = 0

    for k in range(cycles):
        designated += 1
        the_circle, position = play_player(the_circle, designated, players, player, position)
        player = player + 1
        if player == no_players + 1:
            player = 1

    max_val = max(players.values())
    response = 0
    for key in players.keys():
        if players[key] == max_val:
            response = max_val

    return response

start = time.time()
print('Part1:', run_the_game(71852))
duration = time.time() - start
print('Duration: {0:.3} seconds'.format(duration))

start = time.time()
print('Part2:', run_the_game(7185200))
duration = time.time() - start
print('Duration: {0:.3} seconds'.format(duration))
