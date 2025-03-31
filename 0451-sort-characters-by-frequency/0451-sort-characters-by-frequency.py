class Solution:
    def frequencySort(self, s: str) -> str:
        characters = list()
        count = Counter(s)
        for key, val in count.items():
            characters.append((-1 * val, key))
        heapq.heapify(characters)

        ans = ""
        while characters:
            val = heapq.heappop(characters)       

            ans += ((-1 * val[0]) * val[1])
        
        # print(ans)
        return ans