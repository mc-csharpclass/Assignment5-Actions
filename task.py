# task file

import math


def firstrun():
    return "success"


# this fucntion takes the radius of a circle and
# returns the area
def calc_circle_area(radius):

    area = math.pi * math.pow(radius, 2)
    return area


# this function accepts a list and returns the first
# and last elements of that list
def get_first_and_last(list=[]):

    first = list[0]
    last = list[-1]
    return [first, last]
