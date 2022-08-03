class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        if not self.calendar:
            self.calendar.append([start,end])
        else:
            for i in range(len(self.calendar)):
                if start<self.calendar[i][1] and end>=self.calendar[i][1]:
                    return False
                elif start>=self.calendar[i][0] and end<=self.calendar[i][1]:
                    return False
                elif start<self.calendar[i][0] and end>self.calendar[i][0]:
                    return False
            self.calendar.append([start,end])
        return True       

