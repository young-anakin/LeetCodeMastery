class Solution:
    def intToRoman(self, num: int) -> str:
        nums = defaultdict(str)

        nums[1] = "I"
        nums[5] = "V"
        nums[10] = "X"

        ans = ""
        n = len(str(num))
        # print(n, str(num))
        for ind, val in enumerate(str(num)):
            print(ind, val, n - ind)
            if (n - ind) == 4:
                print("YOOO")
                if val == "3":
                    ans += "MMM"
                elif val == "2":
                    ans += "MM"
                else:
                    ans += "M"
            elif (n-ind) == 3:
                if val == "9":
                    ans += "CM"
                else:
                    if val == "8":
                        ans += "DCCC"
                    elif val == "7":
                        ans += "DCC"
                    elif val == "6":
                        ans += "DC"
                    elif val == "5":
                        ans += "D"
                    elif val == "4":
                        ans += "CD"
                    elif val == "3":
                        ans += "CCC"
                    elif val == "2":
                        ans += "CC"
                    elif val == "1":
                        ans += "C"
            elif (n - ind) == 2:
                if val == "9":
                    ans += "XC"
                else:
                    if val == "8":
                        ans += "LXXX"
                    elif val == "7":
                        ans += "LXX"
                    elif val == "6":
                        ans += "LX"
                    elif val == "5":
                        ans += "L"
                    elif val == "4":
                        ans += "XL"
                    elif val == "3":
                        ans += "XXX"
                    elif val == "2":
                        ans += "XX"
                    elif val == "1":
                        ans += "X"
            else:
                if val == "9":
                    ans += "IX"
                else:
                    if val == "8":
                        ans += "VIII"
                    elif val == "7":
                        ans += "VII"
                    elif val == "6":
                        ans += "VI"
                    elif val == "5":
                        ans += "V"
                    elif val == "4":
                        ans += "IV"
                    elif val == "3":
                        ans += "III"
                    elif val == "2":
                        ans += "II"
                    elif val == "1":
                        ans += "I"
            # print(ind, ans)
            

                        
        return(ans)