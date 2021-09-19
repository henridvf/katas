import numpy as np

def score(dice):
    # roll = [[x,dice.count(x)] for x in set(dice)]
    # roll = dict((x,dice.count(x)) for x in set(dice))
    roll = np.bincount(np.array(dice))

    pnts_singles = {1: 100, 5: 50}
    pnts_triples = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}

    points = 0
    for i in range(1, len(roll)):
        points += roll[i] * pnts_singles.get(i, 0)
        if roll[i] >= 3:
            points += (pnts_triples.get(i) - (3 * pnts_singles.get(i, 0)))

    return points

# print(score([4, 4, 4, 3, 3]))
# print(score([2, 4, 4, 5, 4]))
print(score([2, 5, 5, 5, 5]))


'''
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
 '''