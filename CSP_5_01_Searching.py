def randomSearch(items:list, target) -> int:
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value
    import random
    
    tries = 0
    
    while True:
        index = random.randint(0, len(items) - 1)
        tries = tries + 1
        
        if items[index] == target:
            print(f"Found in {tries} tries")
            return index


def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.
    checks = 0
    
    for i in range(len(items)):
        checks = checks + 1
        if items[i] == target:
            return (i, checks)
    
    return (-1, checks)


def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements binary search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
    checks = 0
    left = 0
    right = len(items) - 1
    
    while left <= right:
        middle = (left + right) // 2
        checks = checks + 1
        
        if items[middle] == target:
            return (middle, checks)
        elif items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    
    return (-1, checks)
