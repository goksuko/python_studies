#Booking
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
  
class Solution:
    def suggestedMeetingTime(self, working_hours, meetings, currentTime, duration):
        for meet in meetings:
            first = min(500000000, meet.start)
            last = max(0, meet.end)
        day = Interval(currentTime, first)
        new = []
        new.append(day)
        new += meetings
        evening = Interval(last, working_hours.end)
        new.append(evening)
        for meet in new:
            if meet.end - meet.start == duration:
                hours = meet.start // 60
                mins = meet.start - hours * 60
                ans = str(hours) + ":" + str(mins)
                if mins < 10:
                    ans += "0"
                return ans
            
    def suggested_meeting_time(self, working_hours, meetings, current_time, duration):
        # corner case
        start, end = working_hours[0]
        if current_time + duration > end:  # can't schedule any meeting cuz it will be overtime
            return "No time available"

        # define and initialize
        ans = end  # initialize the ans to be an impossible value
        if current_time <= start:
            current_time = start  # you can't schedule meeting before work day started, so just wait until work day starts
        else:
            current_time = max(start, current_time)

        # iterate
        for m_start, m_end in meetings:
            # we only need to check the time before the current meeting start time, because the data is not sorted,
            # so we don't know what's the next meeting start time.
            # if you try to see if you can arrange a meeting after the current meeting end time,
            # like if m_end + duration <= current time: ans = min(m_end, ans)
            # there could be an existed meeting, starting right after the current one,
            # and you just haven't iterated to that meeting yet.
            if current_time + duration <= m_start:
                ans = min(current_time, ans)  # keep the earliest time
            # if it's impossible to schedule a new meeting before the current meeting,
            # we can only wait until the current meeting ends or current_time already passed the current meeting end time
            current_time = max(current_time, m_end)
            
        if ans < end:
            return [ans, ans + duration]
        else:
            return "No time available"



working_hours = Interval(480, 1080)
meetings = []
meetings.append(Interval(600, 660))
meetings.append(Interval(720, 780))
meetings.append(Interval(780, 825))
meetings.append(Interval(900, 940))
currentTime = 780
duration = 45
  
sol = Solution()
print(sol.suggestedMeetingTime2(working_hours, meetings, currentTime, duration))

