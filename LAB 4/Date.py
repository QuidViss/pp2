import datetime
#TASK 1
now1 = datetime.datetime.now()
five_days_ago = now1 - datetime.timedelta(days = 5) 
# print(f'Date which was 5 days ago: {five_days_ago.strftime("%Y-%m-%d")}')

#TASK 2
today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days = 1)
yesterday = today - datetime.timedelta(days = 1)

# print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
# print("Today:", today.strftime("%Y-%m-%d"))
# print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#TASK 3
# print(f"Date without microseconds: {now1.strftime('%Y-%m-%d %H:%M:%S')}")

#TASK 4
def input_date():
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))
    d = datetime.date(year=year, month=month, day=day)
    return d

# a = input_date()
# b = input_date()
# c = abs(b - a)
# print(f"There is {c.total_seconds()} seconds between {a} and {b}")