class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def play(l, r, turn):
            if l > r:
                return 0
            if turn == 0:
                return max(play(l+1, r, 1-turn) + nums[l], 
                           play(l, r-1, 1-turn) + nums[r])
            else:
                return min(play(l+1, r, 1-turn) - nums[l],
                           play(l, r-1, 1-turn) - nums[r])
        return play(0, len(nums)-1, 0) >= 0