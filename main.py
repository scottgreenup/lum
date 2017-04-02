#!/usr/bin/env python

import itertools
import logging




def method(ordered, n):
    l = len(ordered)
    y = n

    pool = []
    results = []

    curr = ordered[:n]

    while True:

        results.append(list(curr))

        if not pool or (max(pool) < min(curr)):
            if y >= len(ordered):
                break
            logging.warning("Adding {} to pool".format(ordered[y], pool))
            pool.append(ordered[y])
            y += 1

        pool = sorted(pool)

        index = None
        index_smallest = 0

        while index is None:
            smallest = pool[index_smallest]
            for i in range(len(curr)-1, -1, -1):
                if curr[i] < smallest:
                    index = i
                    break

            if index is None:
                index_smallest += 1

        # index is what we are replacing
        # index_smallest is what we replace it with

        curr_before = list(curr)

        smallest = pool[index_smallest]
        pool.remove(pool[index_smallest])
        pool.append(curr[index])
        pool = sorted(pool)
        curr[index] = smallest
        index -= 1

        logging.warning('-' * 60)
        logging.warning("{} -> {} :: {}".format(curr_before, curr, pool))
        curr_before = list(curr)

        # Now we want to replace everything before index if we can
        # TODO fix bug
        for i in range(0, index+1):
            logging.warning("pool = {}; curr = {}; i = {}".format(pool, curr, i))
            if pool[0] < curr[i]:
                m = int(pool[0])
                pool = pool[1:]
                pool.append(curr[i])
                pool = sorted(pool)
                curr[i] = m

        if curr_before != curr:
            logging.warning("{} -> {} :: {}".format(curr_before, curr, pool))

    return results

results = method(list(range(1, 21)), 4)

hostnames = list(reversed(range(0, 20)))
index = 0
curr = -1
count = 0
for p in itertools.permutations(hostnames, 4):
    p = list(p)
    if sorted(p) == p:
        x = []
        for e in p:
            x.append(20-e)
        x = sorted(x)

        if x[-1] != curr:
            if curr > 0:
                #print("{} for {} times".format(curr, count))
                pass
            curr = x[-1]
            count = 1
        else:
            count += 1

        print("{} == {} : {}".format(x, results[index], x == results[index]))
        index += 1


