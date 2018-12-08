#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list=[1223,23,45,67]


# In[2]:


my_list


# In[5]:


import numpy as np
arr=np.array(my_list)
print(arr)


# In[6]:


nArrayList=[[1,2,3],[65,6,7],[34,56,78]]
print(nArrayList)


# In[7]:


np.array(nArrayList)


# In[13]:


import numpy as n
arr=n.arange(0,12,2,dtype=int) # print from 0 to till 12 on 2 gap and the datatype of int is int
print(arr)


# In[16]:


arr=np.zeros(3,dtype=int)
print(arr)


# In[18]:


a=n.zeros((3,3),dtype=int)
print(a)


# In[24]:


# signatre of this function is np.linspace(start,end,num=50,endpoint=true,retstep=false, dtype=None)
# return spaced number over the given interval
np.linspace(2,10,5,dtype=int)


# In[28]:


# identity matrix
import numpy as nee
a1=nee.eye(4,dtype=complex)
print(a1)
a2=nee.eye(2,dtype=int)
print(a2)


# In[29]:


# random number There are many function on random number
np.random.rand(4)


# In[32]:


np.random.rand(5,5)


# In[36]:


# reshape methode
import numpy as n1
arr=n1.arange(25).reshape(5,5)
print(arr)


# In[39]:


import numpy as n1
arr=n1.arange(25).reshape(5,5)**2
print(arr)


# In[41]:


# finding max and min
print(arr.max())
print(arr.min())


# In[43]:


# finding datatype of array
arr.dtype


# In[ ]:




