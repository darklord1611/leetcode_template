# LeetCode Daily Challenge (2025-12-12)\n# Title: Count Mentions Per User\n# Difficulty: Medium\n# Acceptance Rate: 31.78126213935092\n# Tags: Array, Math, Sorting, Simulation\n# URL: https://leetcode.com/problems/count-mentions-per-user/\n#\n# You are given an integer numberOfUsers representing the total number of users and an array events of size n x 3.
#
# Each events[i] can be either of the following two types:
#
#
# 	Message Event: [&quot;MESSAGE&quot;, &quot;timestampi&quot;, &quot;mentions_stringi&quot;]
#
#
# 		This event indicates that a set of users was mentioned in a message at timestampi.
# 		The mentions_stringi string can contain one of the following tokens:
#
# 			id&lt;number&gt;: where &lt;number&gt; is an integer in range [0,numberOfUsers - 1]. There can be multiple ids separated by a single whitespace and may contain duplicates. This can mention even the offline users.
# 			ALL: mentions all users.
# 			HERE: mentions all online users.
#
#
#
#
# 	Offline Event: [&quot;OFFLINE&quot;, &quot;timestampi&quot;, &quot;idi&quot;]
#
# 		This event indicates that the user idi had become offline at timestampi for 60 time units. The user will automatically be online again at time timestampi + 60.
#
#
#
#
# Return an array mentions where mentions[i] represents the number of mentions the user with id i has across all MESSAGE events.
#
# All users are initially online, and if a user goes offline or comes back online, their status change is processed before handling any message event that occurs at the same timestamp.
#
# Note that a user can be mentioned multiple times in a single message event, and each mention should be counted separately.
#
#


# Your solution starts here
def solution():
	pass
