#!/usr/bin/python3

def calculate_weighted_average(data_points=None):
    if not data_points:
        return 0

    total_weighted_sum = 0
    total_weight = 0

    for value, weight in data_points:
        total_weighted_sum += value * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return total_weighted_sum / total_weight
