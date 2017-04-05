# Lowest Unique Maximum Combination Sort

Given a sorted list. Produce combinations of the list, minimising the unique
maximum. Unique maximum is calculated by comparing two sets of costs, the first
pair of costs that are not equal are the unique maxima. The lower value should
be sorted before the higher value.

```
{1, 2, 3, 4} < {1, 2, 3, 5}
  -- comparing [3] => 4 vs 5, 4 is less than 5, therefore LHS is lower

{1, 2, 3, 5} < {1, 2, 4, 5}
  -- comparing [3] => 5 vs 5, equal, keep going
  -- comparing [2] => 3 vs 4, 3 is less than 4, therefore LHS is lower
```

# Usage
```
usage: ./main.py [-h] -c CHOICES -n NUMBER -l LIST [LIST ...]

Produce the top N combinations, sorted by LUM. Normally combinations would
come out as 1234, 1235, 1236, ... however this program wants to minimise the
maximum. Therefore the program produces 1234, 1235, 1245, 1345, 2345, and
1236... Take two adjacent combinations, find the unique maximum you'll see it
is strictly increasing for the wholeset.

optional arguments:
  -h, --help            show this help message and exit
  -c CHOICES, --choices CHOICES
  -n NUMBER, --number NUMBER
  -l LIST [LIST ...], --list LIST [LIST ...]
```

## Example

```
# To have 10 choices, with 3 in each combination:

$ ./main.py --choices 10 --number 3 --list 0 1 2 3 4 5
['0', '1', '2']
['0', '1', '3']
['0', '2', '3']
['1', '2', '3']
['0', '1', '4']
['0', '2', '4']
['1', '2', '4']
['0', '3', '4']
['1', '3', '4']
['2', '3', '4']
```
