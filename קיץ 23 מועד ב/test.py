# שאלה א
# x = int(input("enter a number"))
# min = x
# max = x
# while(x<100 or x>999):
#     x=int(input("anter a number :"))
#     if(x>max):
#         max=x

#     if (x<min):
#         min=x
# print(f"the biger num is {max} teh lower {min}")


# שאלה ב
# סעיף א
# def is_valid(s) :

#     if (len(s)%2==0):
#         return False
#     if (s[0]==s[len(s)-1] and s[0]== s[len(s)//2]):

#         return True
#     return False


# סעיף ב
# s = str(input("enter a string :  "))
# numOfTrueStr=0
# numOfFalseStr=0
# for i in range(22):
#     if is_valid(s):
#         numOfTrueStr+=1
#     else:
#         numOfFalseStr+=1
#     s = str(input("enter a string :  "))
# print(f"numOfTrueStr = :{numOfTrueStr}  numOfFalseStr = : {numOfFalseStr}")


# #שאלה ג
# def f(numarry):
#     postiv=0
#     negtiv=0

#     bollin=True
#     for i in numarry:
#         if (i==0):
#             bollin=False
#         if (i<0):
#             negtiv+=1
#         else:
#             postiv+=1
#     if postiv==negtiv and  bollin:
#         for i in numarry:
#             print(i)
#     else:
#         i=len(numarry)-1

#         while(i!=0):
#             print(numarry[i])
#             i-=1
# f([1,1,1,-1,0,-1])


# שאלה 4
# class FlowerPackage:
#     def __init__(type,num,price,time):
#         self.type=type
#         self.num=num
#         self.price=price
#         self.time=time


# class City:
#     def __init__(self ,name,popul,branch):
#         self.name=name
#         self.popul=popul
#         self.branch=branch

# def isFit(City):
#     if (City.branch>3 and city.popul>=5000) :
#         return True
#     return False

# cont=0
# name = str(input("enter name"))
# popul = int(input("enter popul num"))
# branch = int(input("enter branch"))
# while(name!="stop" and popul!="stop" and branch!="stop"):
#     newCity = City(name,popul,branch)
#     if (  isFit(newCity)):
#         print(F"{newCity.name} is fit")
#     else:
#         print(F"{newCity.name} is not fit")
#         cont+=1

#     name = str(input("enter name"))
#     popul = int(input("enter popul num"))
#     branch = int(input("enter branch"))
# print(cont)


# שאלה 6
# def secret(str):
#     i = 0;
#     while i < len(str)//2:
#       if str[i] < 'a' or str[i]> 'z':
#             return False
#       i+=1

#     if len(str)%2!=0:
#         i+=1

#     while i < len(str):
#         if str[i] < 'A' or str[i] > 'Z':
#             return False;
#         i+=1

#     return True


# def mystery(arr):
#     i = 0
#     j = len(arr) -1
#     while i < j:
#         if secret(arr[i]) != secret(arr[j]):
#             return False;
#         i+=1
#         j-=1

#     return True;

# print(mystery(["aaAA","bbGG" ,"abcABC"]))


# def what(arr, num):
#     c = 0
#     left = 0
#     right = len(arr)-1
#     while left < right:
#         if arr[left] + arr[right] >= num:
#             right -= 1
#         else:
#             c += (right - left)
#             left += 1

#     return c


# arr = [1, 3, 6, 11, 18, 21, 27, 35]

# print(what(arr, 7))
