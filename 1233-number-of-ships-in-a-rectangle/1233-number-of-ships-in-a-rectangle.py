# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:

        # horizontal classification
        cp = 0
        visited = set()
        def horizontal(topRight, bottomLeft):
            nonlocal cp
            nonlocal visited
            # Base Case
            if topRight.x == bottomLeft.x:
                vertical(topRight, bottomLeft)
                # print(cp)
                return
            # divvy it up based on x
            newX = (topRight.x + bottomLeft.x)//2

            lowerBound = Point(newX+1, bottomLeft.y)
            upperBound = Point(newX, topRight.y)
            # print("hi", (bottomLeft.x , bottomLeft.y), (upperBound.x, upperBound.y))

            if sea.hasShips(upperBound, bottomLeft):
                visited.add((upperBound, bottomLeft))
                horizontal(upperBound, bottomLeft)
            # print("bye", (topRight.x, topRight.y), (lowerBound.x, lowerBound.y))
            if sea.hasShips(topRight, lowerBound):
                visited.add((topRight, lowerBound))
                horizontal( topRight, lowerBound)

        def vertical(topRight, bottomLeft):
            nonlocal cp
            if topRight.y == bottomLeft.y:
                cp +=1
                return
            newY = (topRight.y + bottomLeft.y)//2

            lowerBound = Point( topRight.x , newY +1)
            upperBound = Point( bottomLeft.x , newY)
            

            if sea.hasShips(upperBound, bottomLeft):
                vertical(upperBound, bottomLeft)
            if sea.hasShips(topRight, lowerBound):
                vertical(topRight, lowerBound)
        
        horizontal(topRight, bottomLeft)
        return cp
        

        