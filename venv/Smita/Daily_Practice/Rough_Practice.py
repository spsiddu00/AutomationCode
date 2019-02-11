##### print and append and sorting

# l = []
# for i in range(1,6):
#     x = input("Enter a number")
#     l.append(int (x))
#
# print(l)
# z = sorted(l)
# print(z)


# ################## Swapping 2 numbers ######
# x = input ("Enter first number")
# y = input ("Enter second number")
# z = int (x)
# x = int (y)
# y = z
# print(x+y)


##############
# i = 0
# while (i < 6):
#   i += 1
#   if i == 10:
#     continue
#   print(i)

##############
# *
# **
# ***
# ****
# *****

###################
# x = int(input("Enter a number"))
# count =0
#
# for i in range(2,x):
#     if (x%i==0):
#         count = 1
#         break
#     else:
#         pass
#
# if (count==0):
#     print(x,"is a prime number")
# else:
#     print(x,"is not aprime number")

#########################
# for x in range(5,10):
#     count = 0
#     if (x <= 2):
#         count = 0
#     else:
#         for i in range(2, x):
#             if (x % i == 0):
#                 count = 1
#                 break
#             else:
#                 pass
#     if count == 0:
#         print(x)
#
# #####################

# str = "transform: translateX(-49%);"
# x = str.split("(")
# y = x[1].split("%")
# print(int(y[0]))
#
# # x = [int(s) for s in str.split() if s.isdigit()]
# # print(x)
#

##################

# List = ['Siddu', 'Smita', 'Manasa', 'Muttu']
#
# for x in range (4):
#     print([x], end=" ")
#
# print()
#
# for x in (List):
#     print(x, end=" ")

################## File Handling #############

# file = "File_Handling_Demo.txt"
# f = open(file)
# r = f.read()
# s = r.split()
#
# count = 0
# for i in s:
#     if i == "Smita":
#         count = count+1
# print(count)
#

#######################

#
# function(3,3)
# function(10,5)
# function(19,2)
# function(1,0)
# function(2,7)
# function(312,2)

#####################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys #To Click on Enter Button Used in line Number 130

x = webdriver.Chrome("C:\\Users\\shiddanagouda.patil\\Desktop\\Learning\\Extra_Practice\\venv\\Driver\\chromedriver.exe") ## Chrome Exe FIle

x.get("http://www.google.com") #### To enter URL

Search_Box_Xpath = "//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input" ### Xpath of Search Box

Search_Box_Obj = x.find_element_by_xpath(Search_Box_Xpath) ### Finding the Search Box using Xpath

Search_Box_Obj.send_keys("HP") #### To ENter the Text in Search Box

Search_Box_Obj.send_keys(Keys.ENTER) ### After the Search it clicks on the Enter Button

