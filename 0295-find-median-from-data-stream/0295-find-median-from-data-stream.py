class MedianFinder:
    def __init__(self):
        # stores the large numbers -> minHeap -> when we pop we pop the smallest element
        self.minHeap = []
        # stores the smallest numbers -> maxHeap -> -1 * val
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -1 * heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -1 * heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2