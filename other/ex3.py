  
from typing import List, Dict, Tuple
from collections import defaultdict

class Solution:
    def __init__(self):
        # for pair, left is departure day of airplane, right is price of airplane
        self.airPlanes: Dict[str, Dict[str, Tuple[int, int]]] = {}
        self.hotelCosts: Dict[str, int] = {}
        self.budget: int = 0
        self.deadLine: int = 0
        self.result: List[str] = []

    def findLongestItinerary(self, currentLocation: str, currentDay: int) -> List[str]:
        self.dfs(currentLocation, currentLocation, 0, currentDay, [])
        return self.result

    def dfs(self, currentLocation: str, destination: str, currentCost: int, currentDay: int, itinerary: List[str]):
        if currentCost > self.budget:
            return
        if currentDay > self.deadLine:
            return

        itinerary.append(currentLocation)
        if currentLocation == destination and len(itinerary) > 1:
            if len(itinerary) > len(self.result):
                self.result = list(itinerary)
            itinerary.pop()
            return

        neibours = self.airPlanes.get(currentLocation, {})
        for neibour, (departureDay, ticketCost) in neibours.items():
            if departureDay < currentDay:
                continue
            hotelCost = self.hotelCosts.get(currentLocation, 0) * (departureDay - currentDay)
            self.dfs(neibour, destination, currentCost + hotelCost + ticketCost, departureDay, itinerary)

        itinerary.pop()

    def findLongestItinerary2(destination, current_day):
        airPlanes = {
        "Amsterdam": {"Paris": (10, 300)},
        "London": {"Paris": (15, 410), "Amsterdam": (17, 400)},
        "Paris": {"London": (13, 300), "Amsterdam": (21, 500)}
        }
        hotelCosts = {
            "Amsterdam": 400,
            "Paris": 500,
            "London": 300
        }
        budget = 5000
        deadLine = 21
         

# Example usage
if __name__ == "__main__":
    airPlanes = {
        "Amsterdam": {"Paris": (10, 300)},
        "London": {"Paris": (15, 410), "Amsterdam": (17, 400)},
        "Paris": {"London": (13, 300), "Amsterdam": (21, 500)}
    }

    hotelCosts = {
        "Amsterdam": 400,
        "Paris": 500,
        "London": 300
    }

    solution = Solution()
    solution.airPlanes = airPlanes
    solution.hotelCosts = hotelCosts
    solution.budget = 5000
    solution.deadLine = 21
    result = solution.findLongestItinerary("Amsterdam", 10)
    print(result)  # Expected output: Longest itinerary within budget and deadline    
    
#     Can someone please share the optimised/brute force solution for this question recently asked in booking dot com interview hackerrank round.
# Given a list of flights between destinations. we have to start from a given source and come back to source with in a given budget and time. lets say


# Amsterdam -> Paris on August 10, Price - 300 euros
# London -> Paris on August 15, Price - 410 euros
# Paris -> London on August 13, Price - 300 euros
# London -> Amsterdam on August 17, Price - 400 euros
# Paris -> Amsterdam on August 21, Price - 500 euros


# Hotel cost per night:
# Amsterdam - 400 euros
# Paris - 500 euros
# London - 300 euros


# Find the longest itinerary possible with in a given budget 5000 and time


# Lets say we start from amsterdam on 10th Aug. now we can go paris. from paris we have two options.
# either we can go to london again or back to amsterdam.


# Option 1:


# Amsterdam -> Paris {flight} 300
# Paris -> London {flight} 300
# London -> Paris {flight} 410
# Paris -> Amsterdam {flight} 400


# Total Flight cost : 1410


# Hotel paris : 3 days {10 to 13} 1500
# Hotel London : 2 days {13 to 15} 600
# Hotel Paris : 6 days {15 to 21} 3000


# Total cost is going above 5000 so user cant use this path


# Option 2:


# Amsterdam -> Paris {flight} 300
# Paris -> London {flight} 300
# London -> Amsterdam {flight} 400


# Total Flight code : 1000


# Hotel paris : 3 days {10 to 13} 1500
# Hotel London : 4 days {13 to 17} 1200


# Total cost = 1500 + 1200 + 1000 = 3700


# So this itin is possbile in the given budget and date . So output will be Amsterdam -> Paris -> London -> Amsterdam