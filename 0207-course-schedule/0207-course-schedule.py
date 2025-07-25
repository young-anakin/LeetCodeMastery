class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        # we have n courses

        # [ai, bi] - inorder to take course ai, we first have to take course bi

        # Will a person take all of the courses? 


        # Number of courses dependent on a certain course
        dependent = defaultdict(int)
        dependentList = defaultdict(list)

        for ai, bi in prerequisites:
            dependent[ai] +=1
            dependentList[bi].append(ai)

        # First in First out principle (FIFO)
        nodependent = deque()        

        for i in range(numCourses):
            if dependent[i] == 0:
                nodependent.append(i)

        finishedCourses = 0

        # Whilst I have a no Current dependent Course, I want to iterate
        while nodependent:

            currentCourse = nodependent.popleft()
            finishedCourses +=1

            for val in dependentList[currentCourse]:
                dependent[val] -=1
                if dependent[val] == 0:
                    nodependent.append(val)
        
        if finishedCourses == numCourses:
            return True
        return False



