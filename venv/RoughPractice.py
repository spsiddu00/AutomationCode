# Map, Generator, Next, (pandas, date-time, threading, os, re, json, requests, numpy, sklearn, xlrd, pickle, paramico)
#
# class Employee:
#     def __init__(self,x,y):
#         self.First = x
#         self.Last = y
#     # First = "Muttu"
#     # Last = " Patil"
#
#     def fullname(self):
#          Name = self.First + self.Last
#          print(Name)
#          return Name
#
#
# class Muttu(Employee):
#     def length(self):
#         x = super().fullname()
#         print(len(x))
#
#
# a = Muttu("x","y")
# a.length()
#--------------------------------------------------------------
# #
# def inHandSalary(x):
#     # x = int (input("Enter your Salary: "))
#     PF = (12/100)*x
#
#     afterPF = x-PF
#
#     if(afterPF <= 250000):
#         # print("Enjoy, No Tax you are Paying, Only PF is Deducting: ", int(PF/12))
#         print("Per Month: ",int(afterPF/12))
#
#     elif(500000 >= afterPF >= 250000):
#         taxableSalary = afterPF - 250000
#         tax = (5/100)*taxableSalary
#         final_Salary = afterPF - tax
#         # print("You are paying the Tax + PF Amount of: ", int((PF+tax)/12))
#         print("Per Month: ",int(final_Salary/12))
#
#     elif(1000000 >= afterPF >= 500000):
#         taxableSalary = afterPF - 500000
#         tax_1 = 12500
#         tax_2 = (20 / 100) * taxableSalary
#         final_Salary = afterPF - tax_2 -tax_1
#         # print("You are paying the Tax + PF Amount of: ", int((PF + tax_1 + tax_2)/12))
#         print("Per Month: ",int(final_Salary/12))
#     else:
#         taxableSalary = afterPF - 500000
#         tax_1 = 12500
#         tax_2 = 100000
#         tax_3 = (10 / 100) * taxableSalary
#         final_Salary = afterPF - tax_3 - tax_2 - tax_1
#         # print("You are paying the Tax + PF Amount of: ", int((PF + tax_1 + tax_2 + tax_3)/12))
#         print("Per Month: ",int(final_Salary / 12))
# #
# inHandSalary(950000)
# -------------------------------------------------------------
# class Operations:
#
#     l = []
#
#     def __init__(self):
#         x = int(input("How many numbers you want to Enter:"))
#         for i in range(1, x + 1):
#             print("Enter", i, "value:")
#             z = int(input())
#             self.l.append(z)
#         print(self.l)
#
#     def addition(self):
#         list = self.l
#         count = 0
#         for x in list:
#             count = count + x
#         print(count)
#
#     def multiplication(self):
#         list = self.l
#         count = 1
#         for x in list:
#             count = count * x
#         print(count)
#
#
# a = Operations()
# a.addition()
# a.multiplication()

####################### Mphasis, Netradyne Usually Networking or Server Related Projects
#--------------------------------------------(Generator)

# def generator():
#     n = 1
#     print("1st Value is:", n)
#     yield n
#
#     n = 10
#     print("2nd Value is:", n)
#     yield n
#
#     n = 100
#     print("3rd Value is:", n)
#     yield n
#
# for item in generator():
#     print(item)

# x = generator()
# print(next(x))
# print(next(x))
# print(next(x))
#------------------------------------------ (map function)
# def numbers(x):
#     return (x)
#
# y = map(numbers,(1,2,3,'s'))
# print(list(y))
#----------------------------------------- (regex)
import re

# s = "I am writing this 1 line so that it shoud be Not24get1"

# print (re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?",s))

# print ()

###### ---------------------------- (Multithraeding)
# # Python program to illustrate the concept
# # of threading
# # importing the threading module
# from threading import Thread
# import time
#
# def print_square():
#     for i in range(5):
#         print("Square: {}".format(i * i))
#         time.sleep(0.8)
#
# def print_cube():
#     for i in range (5):
#         print("Cube: {}".format(i * i * i))
#         time.sleep(0.6)
#
# # print_square()
# # print_cube()
#
#
# # creating thread
# t1 = Thread(target=print_square)
# t2 = Thread(target=print_cube)
#
# # starting thread 1
# t1.start()
# # starting thread 2
# t2.start()
#
# # wait until thread 1 is completely executed
# t1.join()
# # wait until thread 2 is completely executed
# t2.join()
#
# # both threads completely executed
# print("Done!")
######## -----------------------------------------(Multithraeding)

# from threading import Thread
# import time
# def square():
#     for i in range(5):
#         print("sqr =",i*i )
#         time.sleep(1)
#
# def cube():
#     for i in range(3):
#         print("cube=", i*i*i)
#         time.sleep(0.8)
#
# t1 = Thread(target=square)
# t2 = Thread(target=cube)
#
# t2.start()
# t1.start()
# # t1.join()
# # t2.join()
# print ("Muttu")


########### Extra Python Knowledge--------------- (Speacial In Python)

########### 1.import this

########### 2.
# def func(array):
#     for num in array:
#         if num % 2 == 0:
#             print(num)
#             break  # Case1: Break is called, so 'else' wouldn't be executed.
#     else:  # Case 2: 'else' executed since break is not called
#         print("No call for Break. Else is executed")
#
# func([1,3,5,4])

########### 3.
# def point(x, y):
#     print(x, y)
#
# foo_list = [3, 4]
# bar_dict = {'y': 'Siddu', 'x': 2}
#
# point(*foo_list)  # Unpacking Lists
# point(**bar_dict)  # Unpacking Dictionaries

############ 4. No Method Overloading in Python
#
# # First product method.
# # Takes two argument and print their
# # product
# def product(a, b):
#     p = a * b
#     print(p)
#
#
# # Second product method
# # Takes three argument and print their
# # product
# def product(a, b, c):
#     p = a * b * c
#     print(p)
#
#
# # Uncommenting the below line shows an error
# # product(4, 5)
#
# # This line will call the second product method
# product(1,2,3)


#---------------------------------------------------------------------
# class Muttu:
#     def Salary(self, x):
#          print("Siddu Salary=",x)
#
#
# class Siddu(Muttu):
#     def Salary(self, x):
#         print("This is the Updated Method, SO Muttu salary is:", x)
#     print("")
#
#
# y = Muttu()
# y.Salary(100)
#
# x = Siddu()
# x.Salary(10001)

# L = [x for x in range(10) if x%2 ==0]
# print(L)
#------------------------------------------- Salary Slabs in India
#
# def sqr(a):
#     return (a*a)
#
# x = map(sqr,(2,3,7))
# print(list(x))
#-----------------------------------------

# def M1():
#
#     print("Printing 1st Line", 1)
#     n = 11
#     yield n
#
#     n = 20
#     print("Printing Second set of instruction", 2)
#     yield n
#
#     n = 30
#     print("printing 3rd set", 3)
#     yield n
#
# x = M1()
# print(next(x))
# print(next(x))
# print(next(x))

# def random(x):
#     yield x
#     yield x**2
#     yield x**3
#
# a = random(4)
# print(next(a))
# print(next(a))
# print(next(a))

# x = lambda a : a**2
# print(x(2))
#

# L1 = ['AT_Oracle', 'Scan', 'Siddu','AT_java']
#
# def word(z):
#     if ('AT_' in z):
#         return True
#     else:
#         return False
#
# x = filter(word,L1)
# print(list(x))
#
# y = map(word,L1)
# print(list(y))

#################### iFrame
# from selenium import webdriver
# import time
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait as wait
#
# driver = webdriver.Chrome("C:\\Users\\shiddanagouda.patil\\Learnings\\Extra_Practice\\venv\\Driver\\chromedriver.exe")
# driver.get("https://www.tutorialrepublic.com/codelab.php?topic=html&file=open-links-in-an-iframe")
#
# ## Give time for iframe to load ##
# time.sleep(5)
# ## You have to switch to the iframe like so: ##
# # wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath("//iframe[@name='myFrame']")))
# driver.switch_to.frame('preview')
# time.sleep(1)
# driver.switch_to.frame('myFrame')
# time.sleep(1)
# ## Insert text via xpath ##
# elem = driver.find_element_by_xpath("//h1")
# print(elem.text)
# ## Switch back to the "default content" (that is, out of the iframes) ##
# driver.switch_to.default_content()
#############################################
#
# with open("textFile") as f:
#     x = f.read()
#     count = sum(1 for line in f for character in line if character.islower())
#     print(count)
#

# L = ["A",'B','C','d','e']
# L1 = sum(1 for x in L if x.isupper())
# print(L1)
#########################################

# x = {
#     "Farrell": {
#         "fname": "Doug",
#         "lname": "Farrell",
#     },
#     "Brockman": {
#         "fname": "Kent",
#         "lname": "Brockman",
#     },
#     "Easter": {
#         "fname": "Bunny",
#         "lname": "Easter",
#     }
# }
# #
# #
# # x = [PEOPLE[key] for key in sorted(PEOPLE.keys())]
# #
# print(x['Siddu'])

######################
#
# d1 = {'Key1':1, 'Key2':2}
# d2 = {'Key1':'A', 'Key2':2}
# d = {}
#
# # d1 = [1,2,3]
# # d2 = ['A',2,3]
# # d3 = []
# # for x in d1:
# #     if x in d2:
# #         d3.append(x)
# # print(d3)
#
# print ({x:y for x,y in d1.items() if x in d2.keys() and d1[x]==d2[x]})
#
# # d3 = {x:y for x,y in d1.items() if d1.items() == d2.items()}
# # print(d3)

###################

# path = "C:\Users\shiddanagouda.patil\Learnings\Extra_Practice\venv\Driver\chromedriver.exe"
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as ec
# x = webdriver.Chrome('C:\\Users\\shiddanagouda.patil\\Learnings\\Extra_Practice\\venv\\Driver\\chromedriver.exe')
# x.get("https://www.google.com")
# search = "//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input"
# search_obj = x.find_element_by_xpath(search)
# search_obj.send_keys("https://any-api.com/")
# search_obj.send_keys(Keys.ENTER)
#
# openUrl = "//*[@id='rso']/div[1]/div/div/div/div/div[1]/a/h3"
# openUrl_object = x.find_element_by_xpath(openUrl)
# openUrl_object.click()
#
# x.implicitly_wait(10)
#
# x_path = "//*[@id='Gallery']/div[3]/div[2]/div[2]/div[4]/div/a"
# x_path_object = x.find_element_by_xpath(x_path)
#
# x_path_object.click()
#
#
# try_Xpath = "//*[@id='Documentation']/side-menu/div/div[2]/div/div/div[2]/div/div/operation-documentation/a"
# x_path_object = x.find_element_by_xpath(try_Xpath)
#
# x_path_object.click()

#################### API Testing
# import requests
# import urllib3
# import json
# d = {"name": "morpheus","job": "leader"}
# api_Url = "http://api.nytimes.com/api/users"                   #"http://api.nytimes.com/svc/news/v3/content.json"
# x = requests.post(api_Url,data=d)
# print(x)
# print(x.json())


# t1 = [1,2,3]
# t2 = ['a','b','c']
# t3 = {}
# t3 ['1'] = 'dimpy'
# t3 ['2'] = 'simpy'
# t3 ['3'] = 'radha'
# print(t3)


############ API Testing

# import requests
# import json
#
# api = "https://reqres.in/api/users?page=2"
# x = requests.delete(api)
# print(x)
# print(json.loads(x))

# l = x.json()["data"]
#
# for x in l:
#     print(x["id"],x["first_name"])


################
#
#
# def testing_Args(*args):
#     for x in args:
#         print(((x)))
#
# testing_Args('a','b',3,4,5)
#
# def testing(**kwags):
#     for x,y in kwags.items():
#         print(x, y)
# testing(x1='a',key2='b',key3=8,)
#
# # #####
# class A:
#     age = 25
#
#     def M1(self):
#         print('Muttu', self.age)
#
#     @classmethod
#     def M2(cls,):
#         print('Siddu', cls.age)
#
#     @staticmethod
#     def M3():
#         print('Accenture_1')
#
# A.M2()
#
#
#
# a = ['foo', 'bar', 'baz', ]
#
# def M1(x,y):
#     print(y,x)
#
# # x,y,z = (map(M1,(1,2,3)))
#
# # M1('a','b')

########################
#
# grid = [[0, 0, 0, 0, 0, 1],
#
#         [1, 1, 0, 0, 0, 1],
#
#         [0, 0, 0, 1, 0, 0],
#
#         [0, 1, 1, 0, 0, 1],
#
#         [0, 1, 0, 0, 1, 0],
#
#         [0, 1, 0, 0, 0, 2]]
#
# print(grid)
#
# def search(x,y):
#     # print("Method")
#     if(grid[x][y])== 2:
#         print('found exit')
#         return True
#     elif(grid[x][y])== 1:
#         print('wall')
#         return False
#     elif (grid[x][y])== 3:
#         print('Visited',(x,y))
#         return False
#
#     grid[x][y] = 3
#
#     if ((x < len(grid) - 1 and search(x + 1, y)) or (y > 0 and search(x, y-1)) or (x > 0 and search(x-1, y)) or (y < len(grid)-1 and search(x, y+1))):
#         return True
#     return False
#
# search(0,0)
# #
# x = lambda x: 2/3 ==1 and re
#
# print(x(6))

# a = 3,4,5
#
# x,y,z = a
#
# print(x)
# print(y)
# print(z)

# help(frozenset)

####################################################################### (Regex)
#
# s = "Siddu is Big 420 and spends Big money @an avarage of 10.23 per day"
#
# import re
#
# print((re.match(r'Big',s)))


######################## System Command

# import sys
#
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))
#
# getattr()
# setattr()
# from collections import Counter
# Old_List = [1,2,3,4,5,5,5,5,5.5]
# 
# d = dict.fromkeys(Old_List)
# 
# new_d = {x:Old_List.count(x) for x,y in d.items()}
# 
# print(new_d)
#
# L = [1,2,3,7,8,9]
#
# if(5 in L):
#     print('Yes')
# else:
#     print("No")
# ############################# Program
# L = [1,3,5,2,4,6]
#
# even = 0
# odd = 0
#
#
# for x in L:
#     if(x%2 == 0):
#         even +=1
#     else:
#         odd +=1
#
# for i in range(even):
#     if(L[i]%2 == 0):
#         continue
#     else:
#         for j in range(even,len(L)):
#             if(L[j]%2 == 0):
#                 temp = L[i]
#                 L[i] = L[j]
#                 L[j] = temp
# print(L)
# #
#
# d1 = {'Name':1}
# d2 = {'Name':2}
# d2.update(d2)
# print(d1)

# ------------

# L = [2,7,8,43,44]
# even = 0
# odd = 0
# for x in L:
#     if x % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(even)
# print(odd)
# for a in range(0,even):
#     if L[a] % 2 == 0:
#         continue
#     else:
#         for b in range (3, len(L)):
#             if L[b] % 2 == 0:
#                 temp = L[a]
#                 L[a] = L[b]
#                 L[b] = temp
# print(L)
# --------------------------------------------------------------
#
# L = [5,4,1,2,3]
# count = 0
# status = 0
# for x in L:
#     if x == 1:
#         status += 1
#     else:
#         for i in range(1,x):
#             if i in L[:L.index(x)+1]:
#                 count += 1
#             else:
#                 count = 0
#                 break
#             if count == x-1:
#                 status += 1
# print(status)
#
#




# a = (L.index(x))
# print(L[:x+1])
# for i in range(0,L[a]):
#     if 1 in L[:a+1]:
#         print("Yes")
#     else:
#         print("NO")

#
# #
# from abc import ABC,abstractproperty
# class Smart_Phone(ABC):
#     def __init__(self):
#         print("ABC")
#
#     def Call(self):
#             print("Calling and Dailing ....")
#     @abstractproperty
#     def Connect_to_Server(self):
#         print("Connection is left to the SIM (the Networek Owner)")
#
#
# class Jio(Smart_Phone):
#
#     def CostPerCall(self):
#         print("1rs Deducted")
#
#     def TimeSpent(self):
#         print("10 hrs Spent")
#
#     def Connect_to_Server(self):
#         print("Connection is in JIo")
#
# obj_1 = Jio()
# obj_1.TimeSpent()

#-------------------------------------------------------------------------------------
# d = {'F_Name':'Siddu', 'S_Name':'Patil', 1:1, 2:3}
#
# # d['First Name'] = d.pop('F_Name')
#
# print(d.pop('F_Name'))
# print(d)
# print(d.popitem())
# print(d)


# x = [1,2,3,4,5]
# y = x
# print(y)
# x[2]='siddu'
# print(y)
#
# def decorator(func):
#     def innercall(*args, **kwargs):
#         print("Decorator")
#         x = func(*args, **kwargs)
#         print("End Decorator")
#         return x
#     return innercall
#
#
# @decorator
# def M1(x,y):
#     print("Function to add", x+y)
#     return x+y
#
#
# x = M1(2,5)
# #
# # print("X--->",x)
# testsFile= open("TestSuite_DIS_V2","r")
# for x in testsFile:
#     print(x)



# import pyautogui
# from PIL import ImageGrab
#
# class Corindates():
#     replayButton = (390,340)
#     dinosaur = (171,395)
#
# def restartTheGame():
#     pyautogui.click(Corindates.replayButton)
#
#
# restartTheGame()

# --------------------------------------------------- Sorting------------------------------------------

# L = [11, 0, 2,3,8,4,9,1]
# print(len(L))
# for i in range (0, len(L)):
#     for j in range (0, (len(L)-1)):
#         if L[j] > L[j+1]:
#             temp = L[j]
#             L[j] = L[j+1]
#             L[j+1] = temp
# print(L)

# --------------------------------------------- ----------------------------------------------------

############## 1st Question
# a = [ 1,2,3,4]
# import copy
# b = copy.deepcopy(a)
# print(id(a),id(b))
# print(a,b)
# a[1] = "Siddu"
# # a.append(10)
# print(id(a),id(b))
# print(a,b)

################ 2nd Question
# a = 23
# def outer():
#     a = 7
#     def inner():
#         print(a)
#         # a = a+1
#     inner()
#
# outer()
# print(a)
################### 3rd Question
# def x(a,L=[]):
#     for i in range(a):
#         L.append(i)
#     print(L)
#
# x(2)
# x(3,L=[1,2,3])
# x(3)
#########################################  ASM Technologies
#1. Sum of last two unique largest Number in L = [3,4,1,2,3,4,7,7,7]

# L = [3,4,1,2,3,4,7,7]
# L.sort(reverse = True)
# print(L)
# sum = 0
# # # print(L)
# for i in range(0 , len(L)-1):
#     if L[0] == L[i +1 ]:
#         pass
#     else:
#         sum = L[0] + L[i + 1]
#         break
# print(sum)

# L = sorted(list(set(L)))
# print(L[-1]+L[-2])

################################### SpanIdea Systems
# a = 10
# b = 20
# c = 30
#
# s = "b-a+c"
#
# print(eval(s))
#
###################################
# f = open("textFile")
# for i in range(0,10):
#     x = f.readline()
#     if(i%2 == 0):
#         y = x.replace("the", "XXX")
#         print(y)
#     else:
#         print(x)


# for x in l:
    # x.replace("the","XXX" )
    # print(x)


#
#     print(i , file[i])
#     file.readline()
#     x=file.replace("the", "XXX", 2)
#
# print(x)

# import requests as R
# r = R.get("https://api.nytimes.com/api/users/2")
# data = r.json()

# if "url" in data.values():
#
# L = [1,2,3,4,5,6,7,8,9,10]
# x = 0
# y = 0
# for a in L:
#     if a%2 == 0:
#         x += 1
#     else:
#         y += 1
# # print(x)
# # print(y)
# for c in range(0,x):
#     if L[c]%2 == 0:
#         continue
#     else:
#         for d in range(x,len(L)):
#             if L[d]%2 == 0:
#                 temp = L[c]
#                 L[c] = L[d]
#                 L[d] = temp
#
# print(L)
















