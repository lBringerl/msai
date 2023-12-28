class ExtendedList(list):
    @property
    def reversed(self):
        return self[::-1]

    @property
    def first(self):
        return self[0]

    @first.setter
    def first(self, value):
        self[0] = value

    @property
    def last(self):
        return self[-1]

    @last.setter
    def last(self, value):
        self[-1] = value

    @property
    def size(self):
        return len(self)

    @size.setter
    def size(self, value):
        if value > self.size:
            self.extend([None] * (value - self.size))
        elif value < self.size:
            data_copy = self[:value]
            self.clear()
            self.extend(data_copy)

    R = reversed
    F = first
    L = last
    S = size
