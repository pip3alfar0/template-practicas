def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Devuelve el índice del elemento encontrado
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
