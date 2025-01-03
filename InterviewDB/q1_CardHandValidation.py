from typing import List

class Solution:
    def cardHand(self, cards: List) -> List:
        dic = []
        
        def valid(card1, card2, card3):
            if (card1["suit"] == card2["suit"] and card2["suit"] == card3["suit"]) or (card1["suit"] != card2["suit"] and card2["suit"] != card3["suit"] and card1["suit"] != card3["suit"]):
                if (card1["value"] == card2["value"] and card2["value"]== card3["value"]) or (card1["value"] != card2["value"] and card2["value"] != card3["value"] and card1["value"] != card3["value"]):
                    if (card1["count"] == card2["count"] and card2["count"] == card3["count"]) or (card1["count"] != card2["count"] and card2["count"] != card3["count"] and card1["count"] != card3["count"]):
                        return True
            return False

                
        for card in cards:
            one = {}
            one["suit"] = card[0]
            one["value"] = card[1]
            one["count"] = len(card) - 1
            dic.append(one)
        print(dic)
        for i in range(len(cards) - 2):
            for j in range(len(cards) - 1):
                for k in range(len(cards)):
                    if valid(dic[i], dic[j], dic[k]):
                        return [cards[i], cards[j],cards[k]]
        
          
    
sol = Solution()
hand = ["+AA", "-AA", "+AA", "-C", "-B", "+AA", "-AAA", "-A", "=AA"]
print("")
print(f"hand: {hand}")
print(sol.cardHand(hand))

# You are provided with a set of cards characterized by suits (+, -, =), values (A, B, C), and counts of these values ranging from 1 to 3. Your goal is to identify a valid hand from the given cards. A valid hand consists of 3 cards where:

# All the suits are either the same or all different,
# All the values are either the same or all different,
# All the counts are either the same or all different.
# Example 1:

# Input cards:

# { +AA, -AA, +AA, -C, -B, +AA, -AAA, -A, =AA }
# Valid hands could be:

# { +AA, +AA, +AA }
# Suit: Same [+ + +]
# Value: Same [A A A]
# Count: Same [2 2 2]

# { -A, -AA, -AAA }
# Suit: Same [- - -]
# Value: Same [A A A]
# Count: Different [1 2 3]

# { -C, -B, -A }
# Suit: Same [- - -]
# Value: Different [C B A]
# Count: Same [1 1 1]

# { +AA, -AA, =AA }
# Suit: Different [+, -, =]
# Value: Same [A A A]
# Count: Same [2 2 2]
# Example 2:

# A valid hand can also be:

# { -A, +BB, =CCC }
# Suit: Different [+, -, =]
# Value: Different [A B C]
# Count: Different [1 2 3]
# Task:
# Write a program to find and return the first valid hand from the provided list of cards. Input will be read from stdin.

# For example, given the input:

# +AA, -AA, +AA, -C, -B, +AA, -AAA, -A, =AA
# # Output any valid hand from this set.