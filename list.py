from typing import List
from rich import print

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #check the total time to be elapsed for each car
        #find longer times when they are listed according to their starting positions
        #pos: 0 and time: 4
        #pos: 2 and time: 5 => every car behind (having small positions) with longer time may create a fleet together

        d = []
        for i in range(len(position)):
            d.append((position[i], (target - position[i]) / speed[i]))
        print(d)
        fleet = 1
        d.sort(key = lambda x: x[0]) # sorts the list d based on the first element of each tuple
        print(d)
        min_time = d[-1][1]
        print(min_time)
        for i in range(len(position)-1, -1, -1):
            if d[i][1] > min_time:
                fleet += 1
                min_time = d[i][1]
                print(min_time)
        return(fleet)
    
    def trial(self) -> None:
        d = []
        print(d)
        # d = [4,1,0,7,5]
        print(d)
        d.sort(key = lambda x: x[0])
        print(d)
        # d = [1,2,5,7,3,9, -1,-3]
        print(d)
        d.sort(key = lambda x: x[0])
        print(d)
        e = sorted(d, key = lambda x: x[0])
        print(e)
        f = [[0] * 2 for _ in range(5)]
        print(f)
        
sol = Solution()
sol.trial()
target = 10
position = [4,1,0,7,5]
speed = [2,2,1,1,3]
print(f"3 => {sol.carFleet(target, position, speed)}")   
