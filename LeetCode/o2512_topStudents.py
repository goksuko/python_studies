from typing import List

class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        """
        :type positive_feedback: List[str]
        :type negative_feedback: List[str]
        :type report: List[str]
        :type student_id: List[int]
        :type k: int
        :rtype: List[int]
        """
        scores = []
        for r in report:
            num = 0
            for w in r.split(" "):
                # print(w, r)
                if w in positive_feedback:
                    num += 3
                elif w in negative_feedback:
                    num -= 1
            scores.append(num)
        # print("scores", scores)
        mp = {}
        for i, score in enumerate(scores):
            mp[student_id[i]] = score
        highest = []
        for score in mp.values():
            highest.append(score)
        highest.sort()
        res = []
        while highest:
            n = highest.pop()
            for id, score in mp.items():
                if score == n:
                    # print("score", n, "id", id)
                    res.append(id)
            if len(res) >= k:
                break
        while len(res) > k:
            res.pop()
        return res
    
    
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        
        stud = []
        pos, neg = set(positive_feedback), set(negative_feedback)
    
        for rep, sid in zip(report, student_id):
            score = 0
            for w in rep.split(" "):
                if w in pos : score += 3
                if w in neg : score -= 1
            stud.append((-score,sid))
            
        stud.sort()
        return [sid for min_score, sid in stud[0:k]]
            
sol = Solution()
print(sol.topStudents(positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2))                
print(sol.topStudents( positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2))            
print(sol.topStudents(positive_feedback = ["fkeofjpc","qq","iio"], negative_feedback = ["jdh","khj","eget","rjstbhe","yzyoatfyx","wlinrrgcm"], report = ["rjstbhe eget kctxcoub urrmkhlmi yniqafy fkeofjpc iio yzyoatfyx khj iio","gpnhgabl qq qq fkeofjpc dflidshdb qq iio khj qq yzyoatfyx","tizpzhlbyb eget z rjstbhe iio jdh jdh iptxh qq rjstbhe","jtlghe wlinrrgcm jnkdbd k iio et rjstbhe iio qq jdh","yp fkeofjpc lkhypcebox rjstbhe ewwykishv egzhne jdh y qq qq","fu ql iio fkeofjpc jdh luspuy yzyoatfyx li qq v","wlinrrgcm iio qq omnc sgkt tzgev iio iio qq qq","d vhg qlj khj wlinrrgcm qq f jp zsmhkjokmb rjstbhe"], student_id = [96537918,589204657,765963609,613766496,43871615,189209587,239084671,908938263], k = 3))        

# 2512. Reward Top K Students
# Medium

# You are given two string arrays positive_feedback and negative_feedback, containing the words denoting positive and negative feedback, respectively. Note that no word is both positive and negative.

# Initially every student has 0 points. Each positive word in a feedback report increases the points of a student by 3, whereas each negative word decreases the points by 1.

# You are given n feedback reports, represented by a 0-indexed string array report and a 0-indexed integer array student_id, where student_id[i] represents the ID of the student who has received the feedback report report[i]. The ID of each student is unique.

# Given an integer k, return the top k students after ranking them in non-increasing order by their points. In case more than one student has the same points, the one with the lower ID ranks higher.

 

# Example 1:

# Input: positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2
# Output: [1,2]
# Explanation: 
# Both the students have 1 positive feedback and 3 points but since student 1 has a lower ID he ranks higher.
# Example 2:

# Input: positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2
# Output: [2,1]
# Explanation: 
# - The student with ID 1 has 1 positive feedback and 1 negative feedback, so he has 3-1=2 points. 
# - The student with ID 2 has 1 positive feedback, so he has 3 points. 
# Since student 2 has more points, [2,1] is returned.
 

# Constraints:

# 1 <= positive_feedback.length, negative_feedback.length <= 104
# 1 <= positive_feedback[i].length, negative_feedback[j].length <= 100
# Both positive_feedback[i] and negative_feedback[j] consists of lowercase English letters.
# No word is present in both positive_feedback and negative_feedback.
# n == report.length == student_id.length
# 1 <= n <= 104
# report[i] consists of lowercase English letters and spaces ' '.
# There is a single space between consecutive words of report[i].
# 1 <= report[i].length <= 100
# 1 <= student_id[i] <= 109
# All the values of student_id[i] are unique.
# 1 <= k <= n