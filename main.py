#!/usr/bin/env python

"""
Example:

    $ ./main.py --choices 10 --list host1 host2 host3 host4 host5 --number 4
    ['host1', 'host2', 'host3', 'host4']
    ['host1', 'host2', 'host3', 'host5']
    ['host1', 'host2', 'host4', 'host5']
    ['host1', 'host3', 'host4', 'host5']
    ['host2', 'host3', 'host4', 'host5']

"""

import argparse
import textwrap

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
    dest='list',
    required=True)


def generator(ordered, n, choices):
    """Generates the next LUM combination starting with ordered[:n]

        ordered - Ascending list of elements
        n - The number of elements per combination
        choices - The number of choies

    run_time = O(choices)
    """

    if len(ordered) == n:
        yield ordered
        return

    if len(ordered) < n:
        print(
            "Can't create combinations of length {} with only {} elements"
            .format(n, len(ordered)))
        return

    y = n
    pool = []
    results = []
    curr = ordered[:n]

    counted = 0

    while True:

        yield list(curr)
        counted += 1
        if counted >= choices:
            return

        if not pool or (max(pool) < min(curr)):
            if y >= len(ordered):
                return
            pool.append(ordered[y])
            y += 1

        # TODO replace pool with ordered set or something
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

        do_swap(curr, index, pool, index_smallest)
        pool = sorted(pool)

        for i in range(0, index):
            if pool[0] < curr[i]:
                do_swap(curr, i, pool, 0)
                pool = sorted(pool)


def do_swap(curr, curr_index, pool, pool_index):
    a = pool[pool_index]
    pool.remove(pool[pool_index])
    pool.append(curr[curr_index])
    curr[curr_index] = a

if __name__ == '__main__':
    args = parser.parse_args()
    for result in generator(args.list, args.number, args.choices):
        print(result)


