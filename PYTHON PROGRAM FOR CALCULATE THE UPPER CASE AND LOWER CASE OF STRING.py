#!/usr/bin/env python
# coding: utf-8

# In[60]:


def upper_lower(string):
    uppers = 0
    lowers = 0
    for char in string:
        if char.isupper():
            uppers += 1
        elif char.islower():
            lowers += 1
        else:
            pass
    return ("no of upper caser character :" , uppers ,  "no of lower case character : ",lowers) 
print(upper_lower('The quick Brow Fox'))


# In[ ]:




