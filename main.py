#!/usr/bin/env python

import argparse
import itertools
import logging
import sys
import textwrap
import time

parser = argparse.ArgumentParser(
    prog="Combinations sorted by Lowest Unique Maximum",
    description=textwrap.dedent("""\
        Produce the top N combinations, sorted by LUM. Normally combinations
        would come out as 1234, 1235, 1236, ... however this program wants to
        minimise the maximum.  Therefore the program produces 1234, 1235, 1245,
        1345, 2345, and 1236... Take two adjacent combinations, find the unique
        maximum you'll see it is strictly increasing for the wholeset.
        """))

parser.add_argument(
    '-c', '--choices',
    dest='choices',
    type=int,
    required=True)

parser.add_argument(
    '-n', '--number',
    dest='number',
    type=int,
    required=True)

parser.add_argument(
    '-l', '--list',
    nargs='+',
    type=int,
    dest='list',
    required=True)

args = parser.parse_args()


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

def slow_method(hostnames, n, choices):
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

sA = time.time()
results = method(args.list, args.number, args.choices)
tA = time.time()

for result in results:
    print(result)

logging.warning("Fast Method = {}".format(tA - sA))

#rev_list = list(reversed(args.list))
#sB = time.time()
#results2 = slow_method(rev_list, args.number, args.choices)
#tB = time.time()
#logging.warning("Naive Method = {}".format(tB - sB))
#for i in range(0, len(results)):
#    a = results[i]
#    b = results2[i]
#    if a != b:
#        print("{} == {} : {}".format(a, b, a == b))



