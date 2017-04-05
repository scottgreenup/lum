
import random
import sys
import unittest

from main import generator

def validation(choices):
    for i in range(0, len(choices) - 1):
        assert len(choices[i]) == len(choices[i+1])
        a = sorted(choices[i])
        b = sorted(choices[i+1])
        for j in range(len(choices[i])-1, -1, -1):
            if a[j] > b[j]:
                print("{} vs {}".format(a, b))
                for k in range(0, len(a)):
                    if a[k] == b[k]:
                        s = "=="
                    elif a[k] > b[k]:
                        s = ">"
                    elif a[k] < b[k]:
                        s = "<"

                    print("{} {} {}".format(a[k], s, b[k]))
                return False
            elif a[j] < b[j]:
                break
    return True


def create_random_list(length):
    return sorted([random.randint(0, 1e9) for _ in range(0, length)])


class LUMGeneratorTest(unittest.TestCase):

    def test_random(self):
        length = random.randint(100, 10000)
        ordered = create_random_list(length)
        top = list(generator(ordered, random.randint(5, 90), 10000))
        self.assertTrue(validation(top))

    def test_normal(self):
        ordered = list(range(0, 10))
        top = list(generator(ordered, 3, 20))
        self.assertTrue(validation(top))

if __name__ == '__main__':
    unittest.main()
