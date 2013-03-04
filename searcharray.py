from dcarray import *
from copy import *

class SearchArray(DCArray):
    """a class for testing search methods

    contains search methods to use on DCArray, as well as methods to refresh
    the store of the array to research the same list."""


    def __init__(self,capacity):
        self._store = [0] * capacity
        self._capacity = capacity
        self._factor = 2
        self._size = 0
        self._startIndex = 0
        self._endIndex = 0

        self._default = None

    def default(self):
        self._default = deepcopy(self._store)

    def refresh(self):
        if self._default is not None:
            self._store = deepcopy(self._default)
        else:
            return 1

    def selectionsSort(self):
        pass

    def insertionSort(self):
        pass

    def quickSort(self):
        pass

    def mergeSort(self):
        pass