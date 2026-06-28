import numpy as np

def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    values = list(values)
    n = len(values)

    i = 0
    while i < n:
        if values[i] is not None:
            i += 1
            continue

        left = i - 1
        j = i
        while j < n and values[j] is None:
            j += 1
        right = j

        if left >= 0 and right < n:
            for k in range(left + 1, right):
                values[k] = values[left] + (k - left) * (values[right] - values[left]) / (right - left)
        elif left >= 0:
            for k in range(left + 1, n):
                values[k] = values[left]
        elif right < n:
            for k in range(right):
                values[k] = values[right]

        i = right

    return values