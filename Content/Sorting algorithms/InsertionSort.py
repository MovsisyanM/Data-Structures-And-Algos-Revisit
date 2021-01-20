def InsertionSort(Array):
    for each in range(1, len(Array)):
        key = Array[each]
        pointer = each - 1
        while pointer >= 0 and key < Array[pointer]:
            Array[pointer + 1] = Array[pointer]
            pointer -= 1
        Array[pointer + 1] = key

# Code block by Movsisyan
