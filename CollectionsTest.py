import hmac
from collections import OrderedDict
from collections import defaultdict
from collections import deque
from collections import namedtuple
from contextlib import contextmanager

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('f')

print(q)
q.popleft()
print(q[0])

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)


with tag('h1'):
    print('Hello World')


def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


print(fab(5))
