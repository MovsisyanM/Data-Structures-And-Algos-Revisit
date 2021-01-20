class Matrix:
    """No, not the movie.
    A 2d array with many methods to make it act like a matrix"""

    def __init__(self, size, fill_with=0):
        assert (size >= 1), "Matrix size too small, must be positive integer"
        this.size = math.floor(size)
        this.mem = [[fill_with] * this.size] * this.size

    def __getitem__(self, key):
        return copy.copy(this.mem[key])

    # this is where the fun begins!
    def __mul__(self, matrix):
        pass
        # No need to worry about matrix mult. compatability since all of them are created squares


# TODO


# arr = np.random.rand(50) * 50
# InsertionSort(arr)
# print(IsSorted(arr))

# Code block by Movsisyan
