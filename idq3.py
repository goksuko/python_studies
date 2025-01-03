
from typing import List

# Given a list of messages and a list of members, write a function that returns a list of messages that contain at least one of the members.
class Solution:
    def messages(self, messages, members):
        res = []
        temp = []
        second_temp = []
        third_temp = {}
        for msg in messages:
            temp.append(msg.split("@"))
        # print(temp)
        # [['Hi ', 'id741, id56. how does it go ', 'Amsterdam. ', 'id54 is happy id45'], 
        # ['', 'istanbul, ', 'id1, id2, id3, bye bye'], 
        # ['', 'id4, id5, hello hi, id']]
        for parts in temp:
            for part in parts:
                if part[0:2] == "id":
                    second_temp.append(part)
        # print(second_temp)
        #['id741, id56. how does it go ', 'id54 is happy id45', 'id1, id2, id3, bye bye', 'id4, id5, hello hi, id']
        for split in second_temp:
            l = 0
            while l < len(split):
                r = l + 2                
                if split[l:r] == "id":
                    while split[r] in "0123456789":
                        r += 1
                    third_temp[split[l:r]] = third_temp.get(split[l:r], 0) + 1
                    l = r
                    if l < len(split) and split[l] == ",":
                        l += 1
                    if l < len(split) and split[l] == " ":
                        l += 1
                else:
                    break
        # print(third_temp)                    
        # {'id741': 2, 'id56': 1, 'id54': 2, 'id1': 1, 'id2': 1, 'id3': 1, 'id4': 1, 'id5': 1}
        for key, value in third_temp.items():
            if key in members:
                res.append(key + "=" + str(value))   
        return res
        # ['id56=1', 'id54=2', 'id1=1', 'id2=1', 'id5=1']

messages = ["Hi @id741, id56. how does it go @Amsterdam. @id54 is happy id45", 
            "@istanbul, @id1, id2, id3, id741, id54 bye bye", 
            "@id4, id5, hello hi, id"]
members = ["id1", "id2", "id56", "id54", "id5"]

sol = Solution()
print(sol.messages(messages, members)) 
