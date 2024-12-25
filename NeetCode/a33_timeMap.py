from typing import List
from collections import defaultdict
from sortedcontainers import SortedDict


#brute force
class TimeMap:
    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = {}
        if timestamp not in self.keyStore[key]:
            self.keyStore[key][timestamp] = []
        self.keyStore[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        seen = 0

        for time in self.keyStore[key]:
            if time <= timestamp:
                seen = max(seen, time)
        return "" if seen == 0 else self.keyStore[key][seen][-1]
    

# 2. Binary Search (Sorted Map)
class TimeMap2:
    def __init__(self):
        self.m = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        
        timestamps = self.m[key]
        idx = timestamps.bisect_right(timestamp) - 1
        
        if idx >= 0:
            closest_time = timestamps.iloc[idx]
            return timestamps[closest_time]
        return ""

# 3. Binary Search (Array)

class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


# sol = TimeMap()
# Input:
# ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

# Output:
# [null, null, "happy", "happy", null, "sad"]

# Explanation:
timeMap = TimeMap()
timeMap.set("alice", "happy", 1);  # store the key "alice" and value "happy" along with timestamp = 1.
timeMap.get("alice", 1);           # return "happy"
timeMap.get("alice", 2);           # return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3);    # store the key "alice" and value "sad" along with timestamp = 3.
timeMap.get("alice", 3);           # return "sad"
print(f"happy => {timeMap.get('alice', 1)}")
print(f"happy => {timeMap.get('alice', 2)}")
print(f"sad => {timeMap.get('alice', 3)}")



# Time Based Key-Value Store
# Implement a time-based key-value data structure that supports:

# Storing multiple values for the same key at specified time stamps
# Retrieving the key's value at a specified timestamp
# Implement the TimeMap class:

# TimeMap() Initializes the object.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
# Note: For all calls to set, the timestamps are in strictly increasing order.

# Example 1:

# Input:
# ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

# Output:
# [null, null, "happy", "happy", null, "sad"]

# Explanation:
# TimeMap timeMap = new TimeMap();
# timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
# timeMap.get("alice", 1);           // return "happy"
# timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
# timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
# timeMap.get("alice", 3);           // return "sad"
# Constraints:

# 1 <= key.length, value.length <= 100
# key and value only include lowercase English letters and digits.
# 1 <= timestamp <= 1000


# Recommended Time & Space Complexity
# You should aim for a solution with O(1) time for set(), O(logn) time for get(), and O(m * n) space, where n is the total number of values associated with a key, and m is the total number of keys.


# Hint 1
# Can you think of a data structure that is useful for storing key-value pairs? Perhaps a hash-based data structure where we not only store unique elements but also associate additional information with each element?


# Hint 2
# We store key-value pairs in a hash map. In this case, we store the keys as usual, but instead of a single value, we store a list of values, each paired with its corresponding timestamp. This allows us to implement the set() method in O(1). How can you leverage this hash map to implement the get() method?


# Hint 3
# A brute force solution would involve linearly going through every value associated with the key and returning the most recent value with a timestamp less than or equal to the given timestamp. This approach has a time complexity of O(n) for each get() call. Can you think of a better way? Since the timestamps in the value list are sorted in ascending order by default, maybe an efficient searching algorithm could help.


# Hint 4
# We can use binary search because the timestamps in the values list are sorted in ascending order. This makes it straightforward to find the value with the most recent timestamp that is less than or equal to the given timestamp.