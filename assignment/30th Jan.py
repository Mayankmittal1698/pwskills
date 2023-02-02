#!/usr/bin/env python
# coding: utf-8

# ##### Question 1. Write a program to accept percentage from the user and display the grade according to the following.
# 

# In[14]:


usr_in = int(input("Enter your percentage"))
if not usr_in.real:
    print("Please enter again without %age sign Integers only allowed")
elif usr_in >90:
    print("Congrats You Scored A Grade")
elif usr_in >80 and usr_in<=90:
    print("Good, put some more efforts. You got B Grade")
elif usr_in >= 60 and usr_in <= 80: 
    print("Be Serious toward your study. You got C Grade")
else:
    print("Don't play with your future. Just passed with D Grade")


# #### Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:
# 15% >1,00,000
# 10% >5,00,000 and <= 1,00,000
# 5% <=5,00,000`

# In[23]:


usr_in = int(input("Enter the price of bike "))

if usr_in >100000:
    print(f"For bike cost {usr_in} will attract total 15% tax which is {int(usr_in*0.15)} tax amount additional to bike price") 
elif 50000<usr_in<=100000:
     print(f"For bike cost {usr_in} will attract total 10% tax which is {int(usr_in*0.10)} tax amount additional to bike price") 
elif usr_in<=50000:
     print(f"For bike cost {usr_in} will attract total 5% tax which is  {int(usr_in*0.5)} tax amount additional to bike price") 
else: print("verify your entered detail")        


# #### Accept any city from the user and display monumnets of that city
# delhi >> Red fort \
# Agra >> Taj Mahal \
# Jaipu >> Jal Mahal 
# 

# In[30]:


usr_in = input("Enter city").upper()

if usr_in == "DELHI":
    print(f"Monument you can saw in {usr_in} is Red Fort")
elif usr_in == "AGRA":
    print(f"Monument you can saw in {usr_in} is Taj Mahal")
elif usr_in == "JAIPUR":
    print(f"Monumnet you can visit in {usr_in} is Jal Mahal")
else: print("Enter right city")


# ### Check how many times a give number can be divided by 3 before it is less than or equal to 10 

# In[41]:


usr_in = int(input("Enter your number to division check"))
tag = 0
while usr_in >=10:
    usr_in = int(usr_in/3)
    tag+=1
    print(usr_in)
print(f"Entered Number {usr_in} can be divided by {tag} times to 3 keeping remainder greater than 10" )


# #### Why and when to use while loop in Python give a detail description with example

# Python while loop is used to run a block code until a certain condition is met
# Why we use: to run a block of code that much of time till our conditions met True there is no counter where our block of code
# just ran for certain number of times even While loop can run infinitely till we break or interrupt our code if its conditions met true infinitely
# 
# When to use : Consider we have to run a block of code for x number of times and we don't know that value x soo we use while 
# whenever we don't knew about number of iteration needed by our loop we use While Loop if we knew number of iteration then we can go for both for and while
# 

# In[6]:


### Code for While loop
# this program calculate sum of numbers until user didn't enter 0

total = 0 
number = int(input("Enter a number: "))
#adding user entered number until user hit 0
while number != 0:
    total += number
    number = int(input("enter numbe to add or 0 to stop to get final total"))
print('Total = ', total)


# In[1]:


#Use nested while loop to display 3 different pattern 
i = 0

while i<=5:
    j = i
    while j<5:
        print("*" ,end = "")
        j+=1
    print()
    i+=1


# In[5]:


i = 5
while i>=1:
    j=5
    while j>=i:
        print("*", end= "")
        j-=1
    print()
    i-=1


# In[17]:


"""
        *
       ***
      *****
     *******
    *********
"""
i = 0
while i<=5:
    j = 5
    while j>=i:
        print(" ",end="")
        j-=1
    print("*"*(2*i-1))
    i+=1


# In[7]:


"""
*********
 *******
  *****
   ***
    *
"""
i = 5 
while i >=1 : 
    j= 0
    print("*"*(2*i-1))
    while j <=(5-i):
        print(" ",end="")
        j+=1
    i-=1


# In[9]:


#reverse a while loop to display 10 to 1 
i =10 
while i >=1:
    print(i)
    i-=1


# In[ ]:


Question 7 and 8 are same so no mean to do them twice 

