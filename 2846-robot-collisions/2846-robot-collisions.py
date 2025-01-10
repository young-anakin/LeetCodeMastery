class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        arr = []

        for ind in range(len(positions)):
            arr.append((positions[ind], directions[ind], healths[ind]))
        
        arr.sort()

        stack = []
        print(arr)
        # print
        for ind in range(len(arr)):
            if not stack:
                stack.append(arr[ind])
            else:
                pos, dir, pow = arr[ind]
                fl = False
                if dir == "L" and stack[-1][1] == "R":
                    # print("yo", stack[-1], pow)
                    while stack and dir == "L" and stack[-1][1] == "R":
                        if pow > stack[-1][2]:
                            stack.pop()
                            fl = True
                            pow -=1
                            # stack.append((pos, dir, abs(pow - 1)))
                        elif pow == stack[-1][2]:
                            stack.pop()
                            fl = False
                            break
                        else:
                            x, y, z = stack.pop()
                            stack.append((x, y, abs(z - 1)))
                            fl = False
                            break
                    if fl:
                        stack.append((pos, dir, abs(pow )))
                    
                else:
                    stack.append((arr[ind]))
            
            # print(stack)

            # print(stack)
        
        # print("---------------------------------------")
        
        ans = []
        dd = defaultdict(int)
        for ind in stack:
            dd[(ind[0])] = (ind[2])
            # ans.append(ind[2])
        
        for ind in range(len(positions)):
            if dd[positions[ind]]:
                ans.append(dd[positions[ind]])
        # print(dd)
        return ans
        print(stack)

        print(arr)