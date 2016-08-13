import sys
import math

class Canvasser:
    def __init__(self):
        self.distance = 0
        self.addresses = []
        self.last_address_index = 0


def create_matrix(addresses):
    matrix = []
    i = -1
    for a1 in addresses:
        i += 1
        matrix.append([])
        for a2 in addresses:
            # duration in seconds
            a1lon = a1.loc_long
            a1lat = a1.loc_lat
            a2lon = a2.loc_long
            a2lat = a2.loc_lat
            distance = math.sqrt(math.pow(a1lat - a2lat, 2) + math.pow(a1lon - a2lon, 2))
            matrix[i].append(distance)
    return matrix


def get_start_houses(matrix, num_canvassers):
    max_distance = -1
    max_i = None
    max_j = None

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            distance = matrix[i][j]
            if max_distance < distance:
                max_distance = distance
                max_i = i
                max_j = j


    outliers = []
    outliers.append(max_i)
    outliers.append(max_j)

    for i in range(num_canvassers - 2):
        max_distance = 0
        max_j = 0
        for j in range(len(matrix)):
            sum_distance = 0
            for k in outliers:
                distance = matrix[j][k]
                sum_distance += distance

            if(sum_distance > max_distance):
                max_distance = sum_distance
                max_j = j

        outliers.append(max_j)

    return outliers


def select_houses(matrix, start_houses, address_list):
    remaining_indices = range(len(matrix))

    canvassers = []
    # now add addresses
    for i in range(len(start_houses)):
        canvasser = Canvasser()
        canvasser.last_address_index = start_houses[i]
        remaining_indices.remove(start_houses[i])
        canvassers.append(canvasser)

    while(len(remaining_indices) != 0):
        can_with_smallest_dist = None
        smallest_dist = sys.maxint
        for can in canvassers:
            if can.distance < smallest_dist:
                smallest_dist = can.distance
                can_with_smallest_dist = can

        next_address_index = None
        smallest_dist = sys.maxint
        for j in remaining_indices:
            distance  = matrix[j][can_with_smallest_dist.last_address_index]
            # add heuristics
            if smallest_dist > distance:
                smallest_dist = distance
                next_address_index = j

        can_with_smallest_dist.last_address_index = next_address_index
        can_with_smallest_dist.distance += smallest_dist
        can_with_smallest_dist.addresses.append(address_list[next_address_index])

        remaining_indices.remove(next_address_index)

    return canvassers
