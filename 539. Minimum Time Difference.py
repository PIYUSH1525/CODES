# Given; a; list; of; 24 - hour; clock; time; points in "HH:MM"; format,return the; minimum; minutes; difference; between;
# any; two; time - points in the; list.;
# Example; 1: Input: timePoints = ["23:59", "00:00"]; Output: 1;
# Example; 2: Input: timePoints = ["00:00", "23:59", "00:00"]; Output: 0;
# Constraints: 2 <= timePoints.length <= 2 * 104; timePoints[i] is in the; format; "HH:MM".
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes_list = []
        for time in timePoints:
            hours, minutes = map(int, time.split(":"))
            total_minutes = hours * 60 + minutes
            minutes_list.append(total_minutes)
        minutes_list.sort()
        min_diff = (24 * 60 + minutes_list[0]) - minutes_list[-1]
        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])

        return min_diff


