class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        arr = SortedList()
        sm = 0
        fin = ((10 ** 9) + 7)
        for ind in range(len(instructions)):
            x = arr.bisect_left(instructions[ind])
            y = len(arr) - arr.bisect_left(instructions[ind] + 1)
            arr.add(instructions[ind])
            # print(x, y)
            # print(arr)
            # print(x, y)
            sm += (min(x, y))
            sm %= fin

        
        return sm 