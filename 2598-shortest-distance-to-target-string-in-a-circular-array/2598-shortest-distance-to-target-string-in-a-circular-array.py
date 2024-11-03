class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        og = len(words)
        words.extend(words)
        print(words)
        mn = float('inf')

        cp = 0 
        for ind in range(startIndex, len(words)):
            if words[ind] == target:
                print(ind, words[ind], cp)
                mn = min(cp, mn)
                # cp = 1
            else:
                cp +=1
        cp = 0
        for ind in range(startIndex+og, len(words)):
            if words[ind] == target:
                print(ind, words[ind], cp)
                mn = min(cp, mn)
                # cp = 1
            else:
                cp +=1
        cp = 0
        for ind in range(startIndex, 0, -1):
            if words[ind] == target:
                print(ind, words[ind], cp)
                mn = min(cp, mn)
                # cp = 1
            else:
                cp +=1

        cp = 0
        for ind in range(startIndex + og, 0, -1):
            if words[ind] == target:
                print(ind, words[ind], cp)
                mn = min(cp, mn)
                # cp = 1
            else:
                cp +=1
        if mn != float('inf'):
            return mn
        return -1