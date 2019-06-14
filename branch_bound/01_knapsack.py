# weight, value
items = [(2,40), (3.14,50), (1.98, 100), (5,95), (3,30)]
capacity = 10


def greedy(items,capacity):
    length = len(items)
    weight_est = 0
    value_est = 0
    # fraction of value to weight
    vw = []
    # taken hash
    taken = {}
    # fill in vw
    for i in range(length):
        # value/weight, value, weight
        vw.append((items[i][1]/items[i][0], items[i][1], items[i][0]))
    # sort by highest v/w ratio
    vw.sort(key=lambda x: x[0], reverse=True)
    print(vw)

    for ratio in vw:
        taken[ratio[1]] = 0
        if weight_est + ratio[2] <= capacity:
            value_est += ratio[1]
            weight_est += ratio[2]
            taken[ratio[1]] = 1
    return value_est, taken, weight_est
#print(greedy(items, capacity))
