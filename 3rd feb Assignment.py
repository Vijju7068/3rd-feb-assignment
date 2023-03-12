#!/usr/bin/env python
# coding: utf-8

# #  Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
# # range of 1 to 25.

# In[1]:


#Ans
#Def keyword is used to define a function

def odd_numbers():
    odd_num = []
    for i in range(1,26):
        if i %2 != 0:
            odd_num.append(i)
    return odd_num
        
        
print(odd_numbers())


# # Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
# # to demonstrate their use.

# In[2]:


#Ans
# *args is use to pass a variable -length list of the arguments to the function. It allows you to pass any number of 
# arguments to a function by using the (*) before the parameter name. The arguments are packed into a tuple that can 
# be accessed within the function.

def add_num(*args):
    sum= 0
    for arg in args:
        sum= sum+arg
    return sum


add_num(1,2,3)


# In[3]:


#Ans
# *args is use to pass a variable -length dictionary of the arguments to the function. It allows you to pass any number of 
# arguments to a function by using the (*) before the parameter name. The arguments are packed into a dictionary that can 
# be accessed within the function.

def my_detail(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
        

my_detail(name = "vijendra", age = 25, designation = "data Scienctist")


# # Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
# # used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
# # 16, 18, 20].

# In[4]:


#Ans
# Iterator is an object that allows you to transverse a container and access its element one by one.

# 'iter' method is used to initialize an iterator object for a container, and the 'next' method is used 
# to iterate over the elements of the conatiner.


# In[5]:


lst = [2, 4, 6, 8, 10, 12, 14,16, 18, 20]
ite = iter(lst)

for i in range(5):
    print(next(ite))


# # Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
# # function.

# In[6]:


"""In Python, a generator function is a special kind of function that can generate a sequence of values using the
"yield" keyword. Instead of returning a value and terminating, a generator function can pause execution and save 
its current state, allowing it to resume execution later and continue generating values. This makes generator functions
useful for generating large sequences of values that can't be easily stored in memory all at once.

The "yield" keyword is used in a generator function to indicate where the function should pause and return a value to 
the caller. When the function is called again, it resumes execution from where it left off, and continues generating
values until it either reaches the end of the sequence or encounters a "return" statement."""


# In[7]:


def even_num(n):
    for i in range(20):
        if i %2 == 0:
            yield i
            
numm = even_num(5)
next(numm)


# In[8]:


next(numm)


# In[9]:


next(numm)


# In[10]:


next(numm)


# In[11]:


next(numm)


# # Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
# # first 20 prime numbers.

# In[12]:


def prime_num():
    for i in range(1,1001):
        if i%2 != 0 :
            yield i
            
            
v = prime_num()
next(v)


# In[13]:


next(v)


# In[14]:


next(v)


# In[15]:


next(v)


# In[16]:


next(v)


# In[17]:


next(v)


# In[18]:


next(v)


# In[19]:


next(v)


# In[20]:


next(v)


# In[21]:


next(v)


# In[22]:


next(v)


# # Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.

# In[36]:


a,b = 0,1
num = 0
while num <=10:
    print(a)
    c= a+b
    a=b
    b=c
    num = num+1


# # Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.
# # Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']

# In[23]:


stri = "pwskills"

[i for i in stri]


# # Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.

# In[29]:


num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if num == rev:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")


# # Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
# # Note: Use a list comprehension to create a list from 1 to 100 and use another List comprehension to filter
# # out odd numbers.

# In[24]:


list = [ i for i in range(1,101)]
v = [ i for i in list if i % 2 !=0 ]
print(v)


# In[ ]:




