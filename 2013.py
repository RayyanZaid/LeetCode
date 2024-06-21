from typing import List
# Dictionary of coordinate to frequency

# {
#       (11,2) : 2
# }
class DetectSquares:

    def __init__(self):
        self.coordToFreq : dict[tuple:int] = dict()

    def add(self, point: List[int]) -> None:
        
        pointTuple = (point[0], point[1])

        if pointTuple not in self.coordToFreq:
            self.coordToFreq[pointTuple] = 1
        else:
            self.coordToFreq[pointTuple] += 1


    def count(self, point: List[int]) -> int:
        
        pointTuple = (point[0], point[1])

        for eachPoint in self.coordToFreq:

            isValidCorner = self.validSquareCorner(eachPoint, pointTuple)

            if isValidCorner:

                self.getRemainingPoints(eachPoint, pointTuple)
        
    def validSquareCorner(self, existingPoint, pointToCheck) -> bool:

        dx = abs(existingPoint[0] - pointToCheck[0])
        dy = abs(existingPoint[1] - pointToCheck[1])

        if dx == dy and dx != 0 and dy != 0:
            return True
        
        return False

    def getRemainingPoints(point1, point2):

        newXPoint = (-1,-1)
        newYPoint = (-1,-1)
        if point1[0] > point2[0]:
            newXPoint = (point1[0], point2[1])
        else:
            newXPoint = (point2[0], point1[1])

        if point1[1] > point2[1]:
            print("inc p2 y")
        else:
            print("inc p1 y")


        return newXPoint, newYPoint
# Your DetectSquares object will be instantiated and called as such:

point = (1,2)
obj = DetectSquares()
obj.add(point)
param_2 = obj.count(point)