class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = len(digits)-1
        rem = 0
        while True:
            if digits[a] != 9:
                digits[a] +=1
                break
            else:
                while True:
                    if digits[a] == 9:
                        if a == 0:
                            digits.pop(a)
                            digits = [1,0] + digits
                            break
                        else:
                            digits[a] = 0
                            rem = 1
                    else:
                        digits[a] += 1
                        break
                    a -=1
                break
        return digits