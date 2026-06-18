# LeetCode Daily Challenge (2026-06-18)\n# Title: Angle Between Hands of a Clock\n# Difficulty: Medium\n# Acceptance Rate: 64.77741953730416\n# Tags: Math\n# URL: https://leetcode.com/problems/angle-between-hands-of-a-clock/\n#\n# Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.
# 
# Answers within 10-5 of the actual value will be accepted as correct.
# 
#  


# Your solution starts here


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # find the position of each hand and subtract
        # for each minute how does the minute hand move?
        # same question with the hour hand?

        minute_angle = 6 * minutes
        hour_angle = 30 * (hour % 12) + 0.5 * minutes

        diff = abs(minute_angle - hour_angle)

        return min(diff, 360 - diff)