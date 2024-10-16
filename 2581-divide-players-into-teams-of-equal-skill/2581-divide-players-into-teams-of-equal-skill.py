class Solution(object):
    def dividePlayers(self, skill):
        sortedSkill = sorted(skill)
        ass = []
        ass2 = 0
        ptr1 = 0
        ptr2 = len(skill)-1
        for a in range(0, int(len(sortedSkill)/2)):
            ass.append(sortedSkill[ptr1] + sortedSkill[ptr2])
            ass2 += sortedSkill[ptr1] * sortedSkill[ptr2]
            ptr1 += 1
            ptr2 -= 1
        if ass.count(ass[0]) == len(ass):
            return ass2
        return -1

        