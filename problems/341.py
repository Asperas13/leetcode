# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._flattened = []

        for elem in nestedList:
            if elem.isInteger():
                self._flattened.append(elem.getInteger())
            else:
                self._flattened.extend(NestedIterator(elem.getList()).flattened)
        self.i = 0

    @property
    def flattened(self):
        return self._flattened

    def next(self) -> int:
        elem = self.flattened[self.i]
        self.i += 1
        return elem

    def hasNext(self) -> bool:
        return self.i < len(self.flattened)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())