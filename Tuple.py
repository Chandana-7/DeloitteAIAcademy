#!/usr/bin/env python
# coding: utf-8

# In[18]:


f=open("Countries.txt","r")


# In[19]:


f


# In[12]:


data=f.read()


# In[13]:


print(data)


# In[22]:


data=f.readlines(0)


# In[23]:


print(data)


# In[25]:


for i in data:
    print(i)


# In[57]:


f=open('NewFile.txt','w')


# In[58]:


list=['Algeria','India','USA','Korea']


# In[54]:


f.writelines(str(list))


# In[59]:


for i in list:
    f.write(i+'\n')


# In[60]:


f.close()


# In[61]:


f=open('NewFile.txt','w')


# In[62]:


import os


# In[65]:


print(os.listdir('FileFunctions'))


# In[71]:


for (root,dir,files) in os.walk('FileFunctions'):
    print(root)
    print(dir)
    print(files)


# In[72]:


a=(1,2,3)


# In[73]:


print(a)


# In[74]:


print(a[0])


# In[75]:


a[0]=10


# In[76]:


b=(10,20,30)


# In[78]:


print(b)


# In[79]:


print(a+b)


# In[80]:


c=a+b


# In[81]:


print(c)


# In[83]:


c.append(40)


# In[85]:


d=(0.01,0.02,0.03)


# In[86]:


print(d)


# In[87]:


e=('AI','Academy')


# In[88]:


print(e)


# In[89]:


print(len(e))


# In[90]:


dic={}


# In[91]:


dic[1]='AI'


# In[92]:


print(dic)


# In[93]:


dic[2]=['Academy','Deloitte',"JIgsaw"]


# In[94]:


print(dic)


# In[95]:


print(d)


# In[96]:


f=("AI",1,0.01,dic)


# In[97]:


print(f)


# In[98]:


print(f[3])


# In[99]:


print(f[3][2])


# In[100]:


print(f[3][2][0])


# In[ ]:




