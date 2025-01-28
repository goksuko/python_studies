
from typing import List
from collections import Counter

# comments says that this is wrong solution

def top_k_hotels(hotels: List, k: int) -> List:
    count = Counter()
    parents = {hotel: parent for hotel, parent, _ in hotels}
    while hotels:
        h, p, c = hotels.pop()
        if p is None:
            count[h] += c
        else:
            hotels.append([p, parent[p], c])
    return count.most_common(k)


hotels = [ 
    [3,0,14],
    [0, None, 10],
    [4,0,44],
    [6, None, 7],
    [10, 6, 13],
    [7, 6, 17],
    [2, None, 2],
    [14, 2, 9],
    [25, 14, 10],
    [12, 2, 10],
    [13, 0, 1],
    [14, 2, 9],
]

# There is list of hotels and they are given in below format:
# { hotel id, parent hotel id, no. of hotel}
# mutlilevel hotel hierarchy exits in the system.
# example:
# [ { 3,0,14}
# {0, null, 10}
# {4,0,44}
# {6, null, 7}
# {10, 6, 13}
# {7, 6, 17}
# {2, null, 2}
# {14, 2, 9}
# {25, 14, 10}
# {12, 2, 10}
# {13, 0, 1}
# {14, 2, 9}
# ]


# Here null represent the top level of the hotel. We want to know top k hotel chains.
# o/p: if k =2:
# {(0,69), (2,56)}