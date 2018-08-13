import re
from datetime import datetime, timedelta, timezone


# import datetime

# now = datetime.datetime.now()
# now = datetime.now()
# print(now)
# print(now.timestamp())
# print(datetime.fromtimestamp(now.timestamp()))
# print(type(now))
# print(now.strftime('%A %Y-%m-%d'))
#
# print(now + timedelta(days=3))

def to_timestamp(dt_str, tz_str):
    re_utc = r'^UTC([+-]\d+):\d+$'
    re_result = re.match(re_utc, tz_str)
    dt_time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz = 0
    if re_result is not None:
        tz = int(re_result.group(1))
    print(dt_time)
    dt = dt_time.replace(tzinfo=timezone(timedelta(hours=tz)))
    print('tz is ', tz)
    print(dt)
    print(dt.timestamp())


to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')

s = '110223199008xxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})(?P<born_month>\d{2})', s)
print(res.groupdict())

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

s2 = '<div><a href="https://support.google.com/chrome/?p=ui_hotword_search" target="_blank">更多</a><p>dfsl</p></div>'
print(re.search(r'<a href=\"(.*?)\".*>(.*)</a>', s2).group(1))

ip_str = "ip=230.192.168.78,version='1.0.0'"
result = re.search(r'ip=(?P<ip>\d+\.\d+\.\d+\.\d+),version=\'(?P<version>.*)\'', ip_str)
print(result.group('ip'), result.group('version'))
