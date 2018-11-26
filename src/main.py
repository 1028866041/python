import math,string,time,functools,json
from functools import reduce
from src import *

def fun(x):
    return math.sqrt(x)
def add(x,y,fun):
    return fun(x)+fun(y)
print(add(3,5,fun))

def fun2(str):
    return str[0].upper()+str[1:].lower()
print(list(map(fun2, ['adam', 'LISA', 'barT'])))

def fun3(x, y):
    return x*y
print(reduce(fun3, [2, 4, 5, 7, 12]))

def fun4(x):
    return math.sqrt(x).is_integer()
print(list(filter(fun4, range(1, 101))))

def fun5(s):
    return s.lower()
print(list(sorted(['bob', 'about', 'Zoo', 'Credit'], key=fun5, reverse=False)))

def fun6(x):
    s=1
    def fun7(x):
        return s*x
    for i in range(len(x)):
        s=fun7(x[i])
    return s
print(fun6([1, 2, 3, 4]))

def count():
    fs = []
    for i in range(1, 4):
        def func(j):
            def g():
                return j*j
            return g
        fs.append(func(i))
        return fs
    print(fs)
print(filter(lambda x: x and len(x.strip())>0, ['test', None, '', 'str', '  ', 'END']))

def performance(u):
    def fun7(f1):
        def fun8(*args, **kw):
            t1 = time.time()
            f2=f1(*args, **kw)
            t2 = time.time()
            t=(t2-t1)*1000 if u == 'ms' else (t2-t1)
            print('call %s() in %d %s' % (f1.__name__, t, u))
            return f2
        return fun8
    return fun7
@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial(10))

def performance2(u):
    def fun9(f1):
        @functools.wraps(f1)
        def fun10(*args, **kw):
            t1 = time.time()
            f2=f1(*args, **kw)
            t2 = time.time()
            t=(t2-t1)*1000 if u == 'ms' else (t2-t1)
            print('call %s() in %d %s' % (f1.__name__, t, u))
            return f2
        return fun10
    return fun9
@performance2('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial.__name__)

sorted_ignore_case = functools.partial(sorted, key=str.capitalize)
print(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))

try:
    import json
except ImportError:
    import simplejson as json
print(json.dumps({'python':3.5}))

class Person:
    pass
xm = Person()
xh = Person()
print(xm == xh)

class Person(object):
    pass
p1 = Person()
p1.name = 'Bart'
p2 = Person()
p2.name = 'Adam'
p3 = Person()
p3.name = 'Lisa'
L1 = [p1, p2, p3]
L2 = sorted(L1, key=lambda x:x.name, reverse=False)
print(L2[0].name)
print(L2[1].name)
print(L2[2].name)

class Person(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.__dict__.update(kw)
xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
print(xiaoming.name)
print(xiaoming.job)

class Person(object):
    def __init__(self, name, score):
        self.name=name
        self.__score=score
p = Person('Bob', 59)
print(p.name)
try:
    print(p.__score)
except AttributeError:
    print('attributeerror')

class Person(object):
    count=0
    def __init__(self, nm):
        self.nm=nm
        Person.count+=1
p1 = Person('Bob')
print(Person.count)
p2 = Person('Alice')
print(Person.count)
p3 = Person('Tim')
print(Person.count)

class Person(object):
    __count = 0
    def __init__(self, nm):
        self.nm=nm
        Person.__count+=1
p1 = Person('Bob')
p2 = Person('Alice')
try:
    print(Person.__count)
except AttributeError:
    print('attributeerror')

class Person(object):
    def __init__(self, name, score):
        self.name=name
        self.score=score
    def get_grade(self):
        if self.score >= 90:
            return 'A-优秀'
        elif self.score >= 60:
            return 'B-及格'
        else:
            return 'C-不及格'
p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)
print(p1.get_grade())
print(p2.get_grade())
print(p3.get_grade())

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'
p1 = Person('Bob', 90)
print(p1.get_grade) #<function Person.__init__.<locals>.<lambda> at 0x000001E3E5BD09D8>
print(p1.get_grade())

class Person(object):
    __count = 0
    @classmethod
    def __init__(self,name):
        self.name = name
        self.__count+= 1
    @classmethod
    def how_many(self):
        return self.__count
print(Person.how_many())
p1 = Person('Bob')
print(Person.how_many())

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course=course
t = Teacher('Alice', 'Female', 'English')
print(t.name)
print(t.course)

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
t = Teacher('Alice', 'Female', 'English')
print(isinstance(t,Person))
print(isinstance(t,Student))
print(isinstance(t,Teacher))
print(isinstance(t,object))

class Students(object):
    def __init__(self, strlist):
        self.strlist = strlist
    def read(self):
        return self.strlist
s = Students('["Tim", "Bob", "Alice"]')
print(json.load(s))

#multi extends：
class Person(object):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass
class SkillMixin(object):
    pass
class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'
class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'
class BStudent(Student,BasketballMixin):
    pass
class FTeacher(Teacher,FootballMixin):
    pass
s = BStudent()
print(s.skill())
t = FTeacher()
print(t.skill())

class Person(object):
    def __init__(self, name, gender, **kw):
        self.name=name
        self.gender=gender
        self.__dict__.update(kw)
        #for k, v in kw.iteritems():
            #setattr(self,k, v)
p = Person('Bob', 'Male', age=18, course='Python')
print(p.age)
print(p.course)

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def __str__(self):
        return '(Student:%s, %s, %s)' % (self.name, self.gender, self.score)
    __repr__ = __str__
s = Student('Bob', 'male', 88)
print(s)

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__
    def __cmp__(self, s):
        if self.score < s.score:
            return 1
        elif self.score > s.score:
            return -1
        else:
            if self.name < s.name:
                return 1
            elif self.name > s.name:
                return -1
            else:
                return 0
L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]

class Fib(object):
    def __init__(self, num):
        a,b,L= 0,1,[]
        for i in range(num):
            L.append(a)
            a, b = b,a+b
        self.numbers= L
    def __str__(self):
        return str(self.numbers)
    __repr__ = __str__
    def __len__(self):
        return len(self.name)
print(Fib(10))

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
    def __mul__(self, r):
        return Rational(self.p * r.q * self.q * r.p, self.q * r.q)
    def __divmod__(self, r):
        return Rational(self.p * r.q , self.q * r.p)
    def __str__(self):
        if self.p < self.q:
            k = self.p
        else:
            k = self.q
        for x in range(k,0,-1):
            if self.p%x==0 and self.q%x==0:
                self.p = self.p/x
                self.q = self.q/x
                break
        return '%s%s' % (self.p, self.q)
    __repr__ = __str__
r1 = Rational(1, 2)
r2 = Rational(1, 4)
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __int__(self):
        return self.p // self.q
    def __float__(self):
        return float(self.p / self.q)
print(float(Rational(7, 2)))
print(float(Rational(1, 3)))

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
    @property
    def grade(self):
        if self.__score >= 80:
            grade = 'A'
        elif self.__score >= 60:
            grade = 'B'
        else:
            grade = 'C'
        return grade
s = Student('Bob', 59)
print(s.grade)
s.score = 60
print(s.grade)
s.score = 99
print(s.grade)

class Person(object):
    __slots__ = ('name', 'gender')
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    __slots__ = ('score')
    def __init__(self, name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score=score
s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print(s.score)

class Fib(object):
    def __init__(self):
        pass
    def __call__(self,num):
        L = [0,1]
        for i in range(num-2):
            L.append(sum(L[-2:]))
        return L
f=Fib()
print(f(10))