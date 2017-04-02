#!/usr/bin/env python

import itertools
import logging
import time

def method(ordered, n, choices):
    l = len(ordered)
    y = n

    pool = []
    results = []

    curr = ordered[:n]

    while True:

        results.append(list(curr))
        if len(results) >= choices:
            return results

        if not pool or (max(pool) < min(curr)):
            if y >= len(ordered):
                break
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

        logging.debug('-' * 60)
        logging.debug("{} -> {} :: {}".format(curr_before, curr, pool))
        curr_before = list(curr)

        # Now we want to replace everything before index if we can
        for i in range(0, index+1):
            if pool[0] < curr[i]:
                m = int(pool[0])
                pool = pool[1:]
                pool.append(curr[i])
                pool = sorted(pool)
                curr[i] = m

        if curr_before != curr:
            logging.debug("{} -> {} :: {}".format(curr_before, curr, pool))

    return results

def method2(hostnames, n, choices):
    curr = -1
    count = 0
    results = []
    for p in itertools.permutations(hostnames, n):
        p = list(p)
        if sorted(p) == p:
            x = []
            for e in p:
                x.append(len(hostnames)-1-e)
            x = sorted(x)

            if x[-1] != curr:
                curr = x[-1]
                count = 1
            else:
                count += 1
            results.append(x)

            if len(results) >= choices:
                return results

    return results




MAGIC_NUMBER = 200

sA = time.time()
results = method(list(range(0, MAGIC_NUMBER)), 4, 100)
tA = time.time()

logging.warning("Fast Method = {}".format(tA - sA))

hostnames = list(reversed(range(0, MAGIC_NUMBER)))
sB = time.time()
results2 = method2(hostnames, 4, 100)
tB = time.time()

logging.warning("Naive Method = {}".format(tB - sB))

for i in range(0, len(results)):
    a = results[i]
    b = results2[i]
    if a != b:
        print("{} == {} : {}".format(a, b, a == b))



