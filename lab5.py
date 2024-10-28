import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
#input: two inputs of class type time
#output: one input of class time, with seconds and minutes not over 60
#purpose: to get the sum of two times
def time_add(input1: data.Time, input2: data.Time) -> data.Time:
    sum_hour = input1.hour +  input2.hour
    sum_minutes = input1.minute + input2.minute
    sum_seconds = input1.second + input2.second
    if sum_seconds > 59:
        mins = sum_seconds//60
        sum_minutes = sum_minutes + mins
        sum_seconds = sum_seconds - mins*60
    if sum_minutes > 59:
        hrs = sum_minutes//60
        sum_hour = hrs+ sum_hour
        sum_minutes = sum_minutes - hrs*60

    return data.Time(sum_hour, sum_minutes, sum_seconds)

# Part 4
#input: a list
#output: bool
#purpose: to see if a list is in descending order
def is_descending(input: list) -> bool:
    for i in range(len(input)-1):
        if input[i]<=input[i+1]:
            return False
    else:
        return True

# Part 5
#input: list, and two integers
#output: an integer, that is the largest in the range of lower to upper inputs
#to find the largest number in between the lower index and upper index
def largest_between(input: list[int], lower: int, upper: int) -> int:
    largest = input[lower]
    if lower > upper:
        return None
    if lower < 0:
        return None
    if upper>(len(input)-1):
        return None
    for i in range(lower, upper+1):
        if input[i]>= largest:
            largest = input[i]
    return largest

# Part 6
#input: a list of Point classes.
#output: a point from the list that is the farthest from origin.
#purpose: to find the point in the list that is the furthest from the origin.
import math
def furthest_from_origin(input: list) -> data.Point:
    distancelist = []
    if input == []:
        return None
    for data in input:
        x_dist_sq = (data.x)**2
        y_dist_sq = (data.y)**2
        dist = math.sqrt(x_dist_sq + y_dist_sq)
        distancelist.append(dist)
    largest = distancelist[0]
    for i in range(len(distancelist)):
        if distancelist[i]>largest:
            largest = i
    return i
