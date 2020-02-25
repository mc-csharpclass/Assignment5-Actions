# task file

import math
import datetime


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


# this function takes two dates and returns the
# number of days between them
def days_between(startDate=[], endDate=[]):

    start = datetime.datetime(startDate[0], startDate[1], startDate[2])
    end = datetime.datetime(endDate[0], endDate[1], endDate[2])
    days = end - start
    return days.days
