class RecentCounter:
    def __init__(self):
        self.timeFrame= 3000
        self.queue=[]
        
    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < (t -  self.timeFrame):
            self.queue.pop(0)
        self.queue.append(t)
        return len(self.queue)

