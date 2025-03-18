'''
https://www.hackerrank.com/challenges/calendar-module
'''
import calendar 

month, day, year = map(int, input().split())
day = calendar.weekday(year, month, day)
days = calendar.day_name
print(days[day].upper())
