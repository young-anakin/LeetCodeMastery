class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        cp = Counter(skill)
        def is_not_whole_number(num):
            return num % 1 != 0

        sm = sum(skill)
        under = len(skill)/2
        div = sm/under
        print(sm, under, div)
        fl = True
        if sm%2 != 0 and under %2 != 1:
            print("fa")
            return -1
        
        if sm%div != 0:
            print("saaa")
            return -1

        ans = 0
        for ind in range(len(skill)/2):
            # print(skill[ind], div-skill[ind])
            cp[skill[ind]] -=1
            if cp[div-skill[ind]] > 0:
                cp[div-skill[ind]] -=1
                ans += skill[ind] * (div-skill[ind])
            else:
                print("jja")
                return -1
        return ans



        