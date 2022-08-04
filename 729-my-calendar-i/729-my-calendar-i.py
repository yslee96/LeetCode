from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.s = SortedList()

    def book(self, start, end):
        if not self.s:
            self.s.add([start,end])
            return True

        # Get the index of the new elment if its inserted into the sorted array
        indx = self.s.bisect_left([start,end])

        # If its the first element in the sorted list
        if not indx:
            if end<=self.s[indx][0]:
                self.s.add([start,end])
                return True

        # If its the last element in the sorted list
        elif indx == len(self.s):
            if start >= self.s[indx-1][1]:
                self.s.add([start,end])
                return True

        # If its the somewhere in the middle
        elif self.s[indx-1][1]<=start and end<=self.s[indx][0]:
            self.s.add([start,end])
            return True
        return False
