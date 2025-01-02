class Solution:
    def candy(self, ratings: List[int]) -> int:
        cp = 0
        candies = [1]
        for ind in range(len(ratings)-1):
            if ratings[ind] < ratings[ind+1]:
                candies.append(1 +  candies[-1])
            else:
                candies.append(1)

        i = len(ratings)-2
        while i >= 0:
            if ratings[i] > ratings[i+1]:
                if candies[i] <= candies[i+1]:
                    candies[i] = candies[i+1] + 1
            
            i -=1
         
        # 
        # print(candies)
        return sum(candies)