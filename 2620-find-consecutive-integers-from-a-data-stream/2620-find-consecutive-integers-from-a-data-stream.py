class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.counter = 0  

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.counter += 1
        else:
            self.counter = 0  

        return self.counter >= self.k
