# A special FIFO queue based on list. The element inside this queue is unique, and a method named "same_element" is
# required to judge whether two elements is same or not.


class UniqueQueue:
    def __init__(self, iterable=None):
        self.list = []
        if iterable is not None:
            for v in iterable:
                self.list.append(v)

    def __len__(self):
        return len(self.list)

    def __contains__(self, key):
        for v in self.list:
            if v.same_element(key):
                return True
        return False

    def append(self, value):
        for v in self.list:
            if v.same_element(value):
                return True
        self.list.append(value)

    def pop(self):
        return self.list.pop(0)

    def __iter__(self):
        return iter(self.list)

    def __repr__(self):
        if not self:
            return '%s[]' % (self.__class__.__name__,)
        return '%s%r' % (self.__class__.__name__, self.list)

    def __eq__(self, other):
        if isinstance(other, UniqueQueue):
            return self.list == other.list
        return False
