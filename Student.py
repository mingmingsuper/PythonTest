class Student(object):
    # __slots关键字可以限制类里只能添加什么属性，出了这里定义的属性其他属性一律不能添加
    # __slots__ = ('_name', '_score', '_age')

    def __init__(self, name, score, age, animal):
        self._name = name
        self._score = score
        self._age = age
        self._animal = animal

    def print_score(self):
        print('%s %s' % (self._name, self._score))

    def say_hello(self):
        print('hello %s' % self._name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def animal(self):
        return self._animal

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('age must be an integer')
        if value < 0 or value > 100:
            raise ValueError('age must between 0 ~ 100')
        self._age = value

    def __str__(self):
        return 'Student object (name：%s)' % self._name

    __repr__ = __str__
