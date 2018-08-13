import re

splitResult = re.split(r'\s+', '0 1  2   4   f')
print(splitResult)

splitResult2 = re.split(r'[\s\,\;]+', '0 1,  2   4;   f')
print(splitResult2)

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

if m is not None:
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
