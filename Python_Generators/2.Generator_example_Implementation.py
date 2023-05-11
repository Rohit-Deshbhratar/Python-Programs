class Week:
    def __init__(self) -> None:
        self.days = {1: 'Monday', 2:'Tuesday', 3:'Wednesday',
                     4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
    
    def week_gen(self):
        for x in self.days:
            yield self.days[x]

week = Week()
iter1 = week.week_gen()
iter2 = iter(week.week_gen())

print(iter1.__next__())
print(iter2.__next__())
print(next(iter1))
print(next(iter2))