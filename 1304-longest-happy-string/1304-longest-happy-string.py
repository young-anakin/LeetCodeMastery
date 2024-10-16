class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        heap = []
        heapq.heappush(heap, (-1* a, "a"))
        heapq.heappush(heap, (-1 *b, "b"))
        heapq.heappush(heap, (-1 *c, "c"))
        while c != 0 or b != 0 or a != 0:
            # while heap: 
            val, letter = heapq.heappop(heap)
            curr = letter

            if len(ans) >= 2:
                if ans[-1] == letter and ans[-2] == letter:
                    if heap:
                        val2, letter2 = heapq.heappop(heap)
                        curr = letter2
                        heapq.heappush(heap, (val, letter))
                        val = val2
                        if val2 == 0:
                            break   
                    else:
                        break             
                    

            if c != 0 and curr == "c":
                if len(ans) <= 1:
                    ans.append("c")
                    c-=1
                    heapq.heappush(heap, (val+1, curr))
                    continue
                else:
                    if ans[-1] == "c" and ans[-2] == "c":
                        pass
                    else:
                        ans.append("c")
                        c-=1
                        heapq.heappush(heap, (val+1, curr))

                        continue
            if b != 0 and curr == "b":
                if len(ans) <=1:
                     ans.append("b")
                     b -=1
                     heapq.heappush(heap, (val+1, curr))

                     continue
                else:
                    if ans[-1] == "b" and ans[-2] == "b":
                        pass
                    else:
                        ans.append("b")
                        b -=1
                        heapq.heappush(heap, (val+1, curr))

                        continue
            if a != 0 and curr == "a":
                if len(ans) <=1:
                     ans.append("a")
                     a -=1
                     heapq.heappush(heap, (val+1, curr))
                     continue
                else:
                    if ans[-1] == "a" and ans[-2] == "a":
                        pass
                    else:
                        ans.append("a")
                        a -=1
                        heapq.heappush(heap, (val+1, curr))
                        continue
            # if fl:
            #     break
        return "".join(ans)
                    