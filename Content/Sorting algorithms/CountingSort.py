def CountingSort(array, maximum):
    """Prettiest counting sort just for you :D
    Takes an array to sort and the maximum value that an element might have in the given array."""
    length = len(array)
    # in practice try smaller ints :P
    counts = np.full((maximum + 1,), 0, dtype="int")
    output = np.full((length,), 0, dtype="int")

    # Count the elements
    for item in array:
        counts[item] += 1

    # Calculate the change of count in elements
    for possible_value in range(1, maximum):
        counts[possible_value] += counts[possible_value - 1]

    # Fill the aux array with the original elements
    ind = 0
    for item in array:
        output[ind] = item
        ind += 1
    del ind

    # Replace the elements that changed places during sorting
    for item in range(length - 1, -1, -1):  # kinda reversed but still works like a charm
        output[counts[array[item]] - 1] = array[item]
        counts[array[item]] -= 1

    return output.tolist()

# Code block by Movsisyan


# testCase = [1, 5, 2, 7, 11, 2, 5, 2, 6, 8, 2, 4, 1, 3, 1, 3, 1, 3, 6, 7, 6, 2, 5, 4, 5, 1, 12]
# sortedd = CountingSort(testCase, max(testCase))
# print(sortedd)
# print("Hurray!" if len(testCase) == len(sortedd) else "Oopsie :/")

# Code block by Movsisyan
