#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[2]:


f = open("crackstation-human-only.txt", "r", encoding="utf-8",errors='ignore')
PWs = f.readlines()


# In[3]:


goodPWs = []
for PW in PWs:
    if len(PW[:-1]) >= 8:
        goodPWs.append(PW[:-1])


# In[4]:


print(len(goodPWs))


# In[10]:


pd.DataFrame(goodPWs).to_csv("crackstation-human-only-8+.txt", index=False, header=False)


# In[ ]:




