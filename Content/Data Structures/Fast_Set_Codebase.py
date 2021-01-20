"optimize with linear-time scans using dictionaries"

import set
# fastset.Set extends set.Set


class Set(set.Set):
    def __init__(self, value=[]):
        self.data = {}                     # manages a local dictionary
        self.concat(value)                 # hashing: linear search times

    def intersect(self, other):
        res = {}
        for x in other:                    # other: a sequence or Set
            if x in self.data:             # use hash-table lookup; 3.X
                res[x] = None
        return Set(res.keys())             # a new dictionary-based Set

    def union(self, other):
        res = {}                           # other: a sequence or Set
        for x in other:                    # scan each set just once
            res[x] = None
        for x in self.data.keys():         # '&' and '|' come back here
            res[x] = None                  # so they make new fastset's
        return Set(res.keys())

    def concat(self, value):
        for x in value:
            self.data[x] = None

    # inherit and, or, len
    def __getitem__(self, ix):
        return list(self.data.keys())[ix]            # 3.X: list()

    def __repr__(self):
        return '<Set:%r>' % list(self.data.keys())  # ditto

# Code block from course.


"set operations for two sequences"


def intersect(seq1, seq2):
    res = []                          # start with an empty list
    for x in seq1:                    # scan the first sequence
        if x in seq2:
            res.append(x)             # add common items to the end
    return res


def union(seq1, seq2):
    res = list(seq1)                  # make a copy of seq1
    for x in seq2:                    # add new items in seq2
        if not x in res:
            res.append(x)
    return res

# Code block from course.


"set operations for multiple sequences"


def intersect(*args):
    res = []
    for x in args[0]:                  # scan the first list
        for other in args[1:]:         # for all other arguments
            if x not in other:
                break   # this item in each one?
        else:
            res.append(x)              # add common items to the end
    return res


def union(*args):
    res = []
    for seq in args:                   # for all sequence-arguments
        for x in seq:                  # for all nodes in argument
            if not x in res:
                res.append(x)          # add new items to result
    return res

# Code block from course.
