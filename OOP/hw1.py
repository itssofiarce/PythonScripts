class MyRange():
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
        self.idx = 0

    def has_next(self):  # how to know that there are more items to return
        # if the start is higher than the end, we know we have reached the end
        if self.step > 0:
            return self.start < self.end
        return self.start > self.end

    def get_next(self):
        rel = self.idx, self.start  # define the element
        self.start += self.step  # increment it, and set the star to start+ the steps
        self.idx += 1
        return rel


rng = MyRange(5, 10, -1)

while rng.has_next():
    print(rng.get_next())
