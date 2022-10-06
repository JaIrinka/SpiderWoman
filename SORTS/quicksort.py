from typing import List


def preposition(arr: List[int], pivot: int):
    i = -1
    for j in range(pivot):
        if arr[j] < arr[pivot]:
            arr[i+1], arr[j] = arr[j], arr[i+1]
            i += 1
    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
    return i+1


def quicksort(arr: List[int], left: int = None, right: int = None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if right - left <= 0:
        return

    pivot = preposition(arr, right)

    quicksort(arr, left, pivot - 1)
    quicksort(arr, pivot + 1, right)
