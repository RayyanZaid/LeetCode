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

                print("YAY")
        
    def validSquareCorner(self, existingPoint, pointToCheck) -> bool:

        dx = abs(existingPoint[0] - pointToCheck[0])
        dy = abs(existingPoint[1] - pointToCheck[1])

        if dx == dy:
            return True
        
        return False


# Your DetectSquares object will be instantiated and called as such:

point = (1,2)
obj = DetectSquares()
obj.add(point)
param_2 = obj.count(point)