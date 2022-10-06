from quicksort import quicksort
from random import randrange


def create_array():
    n = randrange(10, 50)
    return [randrange(0, 1000) for i in range(n)]


if __name__ == "__main__":
    for i in range(10):
        arr1 = create_array()
        print(arr1)
        arr2 = sorted(arr1[:])
        quicksort(arr1)
        print(arr1)
        print(arr2)
        print(arr1 == arr2)
        print("="*100)
