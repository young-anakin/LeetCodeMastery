class Solution(object):
    def partitionLabels(self, s):
        dict = {}
        for a in range(0, len(s)):
            dict[s[a]] = a
        a = 0
        b = 0
        max = 0
        parti = []
        while(b < len(s)):
            if dict[s[b]] > max:
                max = dict[s[b]]
            if b == max:
                parti.append((b+1)-a)
                a = b+1
            b+=1
        return parti
        
