#!/usr/bin/env python
# coding: utf-8

# In[5]:


from random import *
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']


# In[1]:


from random import *
import sys
m = int(input("Enter the length for letters in password:"))
if m < 5:
    print("Please check length")
    sys.exit()
n = int(input("Enter the length for numbers in password:"))
if n < 5:
    print("Please check length")
    sys.exit()
o = int(input("Enter the length for symbols in password:"))
if o < 5:
    print("Please check length")
    sys.exit()
password = []
while n>0:
    password.append(choice(letters))
    n= n-1

while m>0:
    password.append(choice(numbers))
    m= m-1

while o>0:
    password.append(choice(symbols))
    o= o-1
finalPass = ''
shuffle(password)
for i in range (0,len(password)):
    finalPass += password[i]
print(finalPass)


# 
# 
# 
