#!/usr/bin/env python3
# font-evolve

import random
import pprint
import os
import time
import copy

random.seed()

jitter = 2
rows, cols = 10, 10
themodel = [[0 for _ in range(cols)] for _ in range(rows)]
themodel = [[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]]

thetest = [[0 for _ in range(cols)] for _ in range(rows)]
thetest = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def compare_arrays(model, test):
    score = 0
    for r in range(rows):
        for c in range(cols):
            if model[r][c] == test[r][c]:
                score = score + 1
    return score


def randomise(array):
    for r in range(rows):
        for c in range(cols):
            array[r][c] = random.randrange(0, 2, 1)
    return array


def iterate(test, amount):
    for iterations in range(amount):
        r = random.randrange(0, rows, 1)
        c = random.randrange(0, cols, 1)
        if test[r][c] == 0:
            test[r][c] = 1
        else:
            test[r][c] = 0
    return test


thetest = randomise(thetest)

currentscore = 0
iterations = 0
while True:
    if currentscore == 100:
        print("Evolved!")
        break
    os.system('clear')
    currentscore = int(compare_arrays(themodel, thetest))
    print(f"Current score - {currentscore}")
    iteratedtest = copy.deepcopy(thetest)
    iteratedtest = iterate(iteratedtest, jitter)
    print("-------------------------")
    pprint.pprint(themodel)
    print("")
    pprint.pprint(thetest)
    print("-------------------------")
    newscore = int(compare_arrays(themodel, iteratedtest))
    print(f"New score - {newscore}")
    print(f"Iterations - {iterations}")
    if newscore > currentscore:
        thetest = copy.deepcopy(iteratedtest)
    iterations = iterations + 1
#    time.sleep(.3)


