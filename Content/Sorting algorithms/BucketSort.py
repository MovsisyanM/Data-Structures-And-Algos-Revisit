def bucketsort(array):
    """ ...."""
    output = []
    length = len(array)
    chulan = [[]] * length

    # BUG HEREEEEEE BE CAREFULLL
    for element in array:
        bucket_index = math.floor(element * length)
        chulan[bucket_index].append(element)
    # NO BUGS AFTER THIS (probably)

    for bucket in chulan:
        bucket.sort()

    for bucket in chulan:
        print(output)
        output = output + bucket

    return output
