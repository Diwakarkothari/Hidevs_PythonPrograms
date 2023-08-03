

import math

#problem1

"""x=2000
mylist=[]
while(x<=3200):
    if (x%7==0 and x%5!=0):
        mylist.append(x)
    x=x+1
print(mylist)


#problem2

x=int(input())
fact=1
while x>=1:
    fact=fact*x
    x=x-1
print(f"factorial of {x} is {fact}")


#problem3

n=int(input())
i=1
dict={}
while i<=n:
    x=i
    y=i*i
    dict[x]=y
    i=i+1
print(dict)


#problem4

n=int(input("enter numbers to insert"))
mylist=[]
while n!=0:
    mylist.append(input())
    n=n-1
print(mylist)


#problem6

mylist=[]
n=int(input("no. of words you want to insert"))
while n!=0:
    mylist.append(input())
    n=n-1
mylist.sort()
print(mylist)


#problem7

x=input()
y=x.upper()
print(y)


#problem 8

temp=input()
set1=set()
z=""

for i in temp:
    if i==" ":
        set1.add(z)
        z=""
    else:
        z+=i


ans=[]
for j in set1:
    ans.append(j)

ans.sort()
print(ans)


#problem 9

mylist=[]
n=int(input("no of binary input"))
num=int(n)
while n!=0:
    temp=int(input())
    mylist.append(temp)
    n=n-1
i=0
dec=0
base=1
div=[]
while i<num:
    temp1=mylist[i]
    while (temp1):
        last = int(temp1 % 10)
        temp1 = int(temp1 / 10)
        dec = dec + (last * base)
        base = base * 2
    if dec%5==0:
        div.append(mylist[i])
    i=i+1
print(div)

#problem10

n=1000
mylist=[]
templist=[]
while n<=3000:
    temp=n
    while(temp):
        last=int(temp%10)
        temp=int(temp/10)
        templist.append(last)
    i=0
    count=0
    while (i<4):
        if templist[i]%2==0:
            count=count+1
        else:
            break
    if count==4:
        mylist.append(n)
    while (templist):
        templist.pop()
    n=n+1
print(mylist)

#optimal solution

values = []
for i in range(1000, 3001):
    s = str(i) #converting the number into a string
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(values)


#problem12

countupper=0
countlower=0

str1=input()
for i in str1:
    if i.isupper():
        countupper=countupper+1
    if i.islower():
        countlower=countlower+1

print("lower case = " ,countlower)
print("upper case = " , countupper)



#problem 11

digit=0
letters=0
str1=input()

for i in str1:
    if i.isdigit():
        digit=digit+1
    if i.isalpha():
        letters=letters+1

print("Letters  = ",letters)
print("digit = ",digit)


#problem 13

nun=int(input())
a=str(nun)#a*2 means writing 'a' two times
term1=int(a)
term2=int(a*2)
term3=int(a*3)
term4=int(a*4)

value=term1+term2+term3+term4
print(value)


#problem 14

mylist=[]
print("enter no. of items in list")
n=int(input())
m=n
while n>0:
    a=int(input())
    mylist.append(a)
    n=n-1

ans=[]
i=0
while i<m:
    temp=mylist[i]
    if temp%2==0:
        pass
    else:
        ans.append(temp*temp)
    i=i+1

print(ans)


#problem 15

bal=0

while 1 :
    print("if you want to transact enter 1 \n"
          "to exit enter -1")
    n=int(input())
    if n==-1:
        print("after transactions balance = ", bal)
        exit(1)

    print("to deposit enter 3 \n"
          "to withdraw enter 4")
    m=int(input())

    if m==3 :
        print("enter amount to deposit")
        dep=int(input())
        bal =bal+dep

    if m==4 :
        print("enter amount to withdraw")
        withdraw=int(input())
        bal=bal-withdraw


#problem 16

mylist=[]
special=["@","#","$"]
print("enter no. of passwors to check")
n=int(input())
while n>0:
    mylist.append(input())
    n=n-1
ans=[]
for i in mylist:
    upper, lower, spec, num = 0, 0, 0, 0
    for j in i:
        if j.isupper():
            upper = 1
        if j.islower():
            lower = 1
        if j.isnumeric():
            num = 1
        if j in special:
            spec = spec + 1

    if len(i) > 6 and len(i) < 12 and upper > 0 and lower > 0 and num > 0 and spec > 0:
            ans.append(i)

print("passwords which are correct are ")
print(ans)


#problem 18

up=5
down=3
left=3
right=2
vert=abs(up-down)
horz=abs(left-right)

dist=vert*vert+horz*horz
ans=int(math.sqrt(dist))
print(ans)


#problem 19

temp=input()
words=temp.lower().split() #lists of words in sentence
#print(words)
mydict={}

for i in words:
    mydict[i]=mydict.get(i,0)+1

#print(mydict)
mydict=sorted(mydict.items());
print(mydict)


#problem 20

def sqr(n):
    return n*n

n=int(input("enter number"))
m=sqr(n)
print("square = ",m)"""


#problem 21

def myfun():
    """ Documentation of myfun() -> Contains only a single print line."""
    """print("Hello world")

print(abs.__doc__)
print(int.__doc__)
print(myfun.__doc__)"""


#problem 22

"""def comp(str1,str2):
    if len(str1)>len(str2):
        return str1
    elif len(str1)==len(str2):
        str3=str1+str2
        return str3
    else:
        return str2

print("enter two strings")
n=input()
m=input()
ans=comp(n,m)
print(ans)


#problem 23

def fun():
    i = 1
    thisdict = {}
    while i < 21:
        thisdict[i] = i * i
        i = i + 1
    print(thisdict)

fun()


#problem 24

def sqr(n):
    return n*n

mylist=[1,2,3,4,5,6,7,8,9,10]
x=map(sqr,mylist)

print(list(x))


#problem 26

num=int(input())
den=int(input())

try:
    ans=num/den
    print(ans)
except :
    print("cannot divide by zero")


#problem 25

tupl1=(1,2,3,4,5,6,7,8,9,10)
ans=[]
for i in tupl1:
    if i%2==0:
        ans.append(i)
ans1=tuple(ans)
print(ans1)


#problem 27

ans=0
def fun(n):
    if n==0:
        return 0
    return fun(n-1)+100

w=fun(5)
print(w)


#problem 28

def fun(n):
    first=0
    second=1
    print("fibonacci series -> ")
    print(first)
    print(second)
    i=2
    while i<=n:
        next=first+second
        first=second
        second=next
        print(next)
        i=i+1

fun(7)


#problem 29

import random
list1=[]
for i in range(9,150):
    if i%5==0 and i%7==0:
        list1.append(i)
print(random.choice(list1))


#problem 30

for i in ["I","You"]:
    for j in ["Play","Love"]:
        for k in ["Hockey","Football"]:
            print(i," ",j," ",k)


#problem 31

list1=[12,24,35,70,88,120,155]
result=list1[:2]+list1[5:]

print(result)


#probelm 32

temp=input()
temp=temp.lower();
mydict={}
for i in temp:
    mydict[i] = mydict.get(i, 0) + 1

print(mydict)


#problem 33

str1=input()
ans=""           #reversed give object address
str1=ans.join(reversed(str1))
print(str1)   #use join to handle such situation


#problem 34

temp=input("Enter string: ")
j=0

for i in temp:
    if j%2==0:
        print(i)
    else:
        pass
    j +=1


#problem 36

temp=input("Enter string: ")
num_digits = 0
num_letters = 0

for i in temp:
    if i.isdigit():
       num_digits += 1
    elif i.isalpha():
       num_letters += 1

print("Digits-> ",num_digits)
print("Letters-> ",num_letters)

      """























