#!/usr/bin/env python
# coding: utf-8

# ## 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# *
# 
# 'hello'
# 
# -87.8
# 
# -
# 
# /
# 
# +
# 
# 6
# 

# ### Answer
# values: -87.8 , 'hello', 6
# 
# mathematical operators: * , + , - , /
# 

# ## 2.What is the difference between string and variable?

# ### Answer
# 
# String is an data type.
# variable is a place where we can store a data in a program.

# ## 3.Describe three different data types.

# ## Answer
# String
# 
# Integers
# 
# Float

# ## 4. What is an expression made up of? What do all expressions do?

# ## Answer
# An expression is made up of operators and operands.
# The expression in Python produces some value after being interpreted by the Python interpreter.
# In all expressions operators perform operation on the operands and gives some values.
# 

# ## 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# 

# ## Answer
# An expression is made up of operators and operands.Expression is used for producing a value.
# 
# Staetment is for displaying values.
# 
# here, spam=10 is an statement as it displays a value.
# 
# 10+20 is an example for expression

# ## 6. After running the following code, what does the variable bacon contain?
# bacon = 22
# 
# bacon + 1

# ## Answer
# 23

# ## 7. What should the values of the following two terms be?
# 'spam'+'spamspam'
# 
# 'spam'*3

# ## Answer
# 
# while running 'spam'+'spamspam' 
# we get answer as 'spamspamspam'. 
# 
# while running 'spam' * 3
# we  get answer as 'spamspamspam'

# ##  8. Why is eggs a valid variable name while 100 is invalid?

# ## Answer
# according to the rules of python variable name should not start with numbers and variable name can start with an alphabet that is also if that starting alphabet is in small letter then more preferable.
# So eggs is a valid variable name while 100 is invalid

# ## 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
# 

# ## Answer
# int()
# 
# float()
# 
# str()

# In[6]:


int(2.0)


# In[7]:


float(2)


# In[8]:


str(2.0)


# ## 10. Why does this expression cause an error? How can you fix it?  'I have eaten'+99+'burritos'

# ## Answer
# concatenation is possible only when the data types involved are same.
# 
# Here, 99 is integer and'I have eaten' and 'burritos' both are string.
# so only we are getting error.
# 
#  To fix it, if we convert 99 integer to a string as '99'. error will be fixed.

# In[10]:


'I have eaten' + ' 99 '+ 'burritos'


# In[ ]:




