#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
arr=np.arange(0,11,dtype=int)
print(arr)# [ 0  1  2  3  4  5  6  7  8  9 10]
a1=arr[2:4] 
print(a1)#[2 3]
arr[2:5]=10
print(arr)# it will replce the value 10 in range 2 to 5  out put will be [0  1 10 10 10  5  6  7  8  9 10]


# In[8]:


arr=np.arange(20) 
print(arr) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
slice=arr[2:5]
print(slice) #[2 3 4]
slice[0:3]=90
print(arr)#[ 0  1 90 90 90  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19] the change in slice is changing the original array


# In[9]:


# way to create the copy of an array
array_copy=arr.copy()
array_copy[:]=90
print(array_copy)#[90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90]change in slice

print(arr)#[ 0  1 90 90 90  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19] not change in original array


# In[10]:


# boolean array in numpy
import numpy as np
mat=np.arange(15)
print(mat)


# In[16]:


bool_array=mat>3
print(bool_array) # [False False False False  True  True  True  True  True  True  True  TrueTrue  True  True]

# return the true  value
print(mat[bool_array])#[ 4  5  6  7  8  9 10 11 12 13 14]

#write in single line
print(mat[mat>5])#[ 6  7  8  9 10 11 12 13 14]


# In[ ]:




