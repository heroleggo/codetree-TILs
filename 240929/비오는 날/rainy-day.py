class info:
    def __init__(self, ymd, date, weather):
        self.ymd = ymd
        self.date = date
        self.weather = weather
    
    def p(self):
        print('{} {} {}'.format(self.ymd, self.date, self.weather))

n = int(input())

result = info('2100-12-31', 'asd', 'Sun')

for i in range(n):
    [ymd, date, weather] = input().split()
    if weather == 'Rain':
        if ymd < result.ymd:
            result = info(ymd, date, weather)

result.p()