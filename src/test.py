import os,sys,string
import operator

help("lambda")
x=str(60)
print(type(x))
print(len(x))
print(range(len(x)))

p="big data  "
f=open("test.txt","w")
f.write(p)
f.close()

print(range(1,10,3))

q='abc'
for i in range(len(q)):
    print(q[i],'%f' % i)

dt={'h':'earth'}
dt['p']= 80
for i,key in enumerate(dt):
    print(i,key,dt[key])
    i=i+1
print(type(dt))
print(isinstance(dt, dict))
print(isinstance(dt, list))

lt= [1,3,4]
del(lt[1])
print(lt)
print(lt[::-1])
print(lt[::-2])
print(sorted(lt))
print(dir(sys))

data=[]
data.append({'a':'bj','b':"sh",'c':"nk"})
data.append({'a2':'bj2','b2':"sh2",'c2':"nk2"})
#data.sort(key=lambda z:(z['b'], -x['c']), reverse=True)
for d in data:
    print(d)
#spark.flatMap(lambada line: line.split()).map(lambada w: (w,1)).reduce(lambada a,b: a+b)

print(4>7<2!=1)

a=2; b=c=2
print(a == c)
print(a is b)
print(b is c)

print(operator.eq(a,'a'))
print(round(3.1415))
print('mp' not in "pkg")

str="world of w"
print(string.capwords("world"))
print(string.ascii_lowercase)
print(str.split(' ')[1])
print(str.strip("w"))

def test(num):
    return 3*num
def convert(func, seq):
    return [func(e) for e in seq]

seq = [1,3.14,5,7,2,4.8,6.9]
print(convert(int,seq))
print(convert(float,seq))
print(convert(test,seq))

def tst(a, b=0.5, *rest):
    for e in rest:
        #print("arg:", e)
        b+=e;
    return a+2*b;
def tst2(a, b=0.5, **rest):
    for e in rest.keys():
        b+=rest[e];
    return a+2*b;
print(tst(1))
print(tst2(1))
print(tst(1,2))
print(tst(1,2,1,1,1))
print(tst2(1,2,arg1=1,arg2=1,arg3=1))
print(os.path.isfile(r'E:\PythonProjects\Python\src\test.txt'))

#from __future__ import unicode_literals
#s = 'am I an unicode?'
#print(isinstance(s, unicode))
