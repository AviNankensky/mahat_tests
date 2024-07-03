#question 1 #################
def sum_(a):
    if a==0:
        return 0
    r=a%10
    return r+sum_(a//10)
# print(sum(150))

def bild():
    a=[]
    for i in range(1,1001):
        if i%sum_(i)==0:
            a.append(i)
    return a
print(bild())



## question 2 #################
def F(num_):
    if num_[0]=="0" and num_[1]=="5" and num_[3]=="-":
        for i in range(4,11):
            # print(ord(num_[i]))
            # print(num_[i])
            if (ord(num_[i]))>=48 and (ord(num_[i]))<=57:
                pass
            else:
                return False
        for i in range(8):
            if num_[2]==(f"{i}"):
                return True
    return False
print(F("053-3033109"),"053-3033109")
print(F("053-3033-09"),"053-3033-09")
print(F("053-30331i9"),"053-30331i9")



# ## question 3 #################

--------part a
def is_ordered(list_):
    val = list_[0]
    for i in range(1,len(list_)):
        if list_[i]<val:
            return False
        val=list_[i]
    return True

lst1 = [6, 24, 12, 8, 44, 3, 7] 
lst2 = [6, 24, 25, 30, 46, 52]
print(is_ordered(lst1)) 
print(is_ordered(lst2))

---------part b
from random import randint
def build_ordered(size, x, y) :
    a=[]
    for i in range(size):
        a.append(randint(x,y))
    return a
print(build_ordered(10,100,200))



 ## question 4 #################

from random import randint
class Time: 
    def __init__(self, hour, minutes): 
        self.hour=hour 
        self.minutes=minutes 

    def difference(self,other):
        self_time = self.hour*60+self.minutes
        other_time= other.hour*60+other.minutes
        return other_time-self_time


def chek_deliver_time(time_start,time_end):
    if time_start.difference(time_end)<180:
        print("The shipment was delivered on time")
    else:
        print("Delivery not delivered on time")

def build(num):
    arr=[]
    for i in range(num):
        arr.append(Time(randint(0,12),randint(0,60)))

    return arr

a =Time(3,30)
b =Time(6,30)
print(a.difference(b))
arr= build(100)

# for i in arr:
#     print(i.hour,i.minutes)


for i in range(len(arr)-1):
    
    index1=i
    index2=i+1
    chek_deliver_time(arr[index1] ,arr[index2])


 ## question 5 #################
def what(a): 
    length = len(a) 
    for i in range(2,length-1,2): 
        if a[i]<a[i-2]: 
            return False 
        i+=1 
        if a[i]>a[i-2]: 
            return False 
    return True

a = [1, 25, 3, 8, 10, 4, 20, 5] 
print(what(a))



