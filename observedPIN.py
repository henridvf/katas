import itertools as it 

def get_pins(observed):
    # map to 'adjacent' digits
    pin_map = {
        0: [8],
        1: [2,4],
        2: [1,3,5],
        3: [2,6],
        4: [1,5,7],
        5: [2,4,6,8],
        6: [3,5,9],
        7: [4,8],
        8: [0,5,7,9],
        9: [6,8]
    }
    # take input digit and map to adjacent digits
    # for i in observed:
    #     observed.extend(pin_map.get(i))
    start = '1124'
    # poss += start

    # run permutation
    pins = []
    # perm = [''.join(p) for p in it.product('11', start, repeat=1)]
    # perm = [''.join(p) for p in it.permutations(observed + start, 2)]
    perm = [''.join(p) for p in it.combinations_with_replacement(start, len(observed))]

    pins.append(set(perm))
    print(pins)

get_pins('11')

'''
["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"]
'''
