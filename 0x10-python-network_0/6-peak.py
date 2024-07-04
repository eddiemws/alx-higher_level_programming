def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    def find_peak_util(arr, low, high):
        mid = low + (high - low) // 2
        
        # Check if mid is a peak element
        if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
            (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid])):
            return arr[mid]
        
        # If the left neighbor is greater, the peak must be in the left half
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return find_peak_util(arr, low, mid - 1)
        
        # If the right neighbor is greater, the peak must be in the right half
        else:
            return find_peak_util(arr, mid + 1, high)

    return find_peak_util(list_of_integers, 0, len(list_of_integers) - 1)
