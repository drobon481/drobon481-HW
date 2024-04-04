#!/usr/bin/env python
# coding: utf-8

# In[32]:


def github() -> str:
    """
    Returns a link to solutions on GitHub.
    """
    return "https://github.com/drobon481/drobon481/blob/main/Homework%201"

print(github())


# In[24]:


import numpy as np
import pandas as pd
import scipy as sc
import matplotlib as mpl
import seaborn as sb


# In[ ]:





# In[23]:


def evens_and_odds(n: int) -> dict:
    """
    Returns a dictionary with the sum of even and odd numbers less than n.
    
    Args:
    n (int): A natural number
    
    Returns:
    dict: A dictionary with keys 'evens' and 'odds' containing the sum of even and odd numbers less than n respectively.
    """
    evens_sum = sum(i for i in range(n) if i % 2 == 0)
    odds_sum = sum(i for i in range(n) if i % 2 != 0)
    
    return {'evens': evens_sum, 'odds': odds_sum}

# Example usage
result = evens_and_odds(101)
print(result)  # Output: {'evens': 2, 'odds': 4}


# In[60]:


from datetime import datetime
from typing import Union

def time_diff(date_1: str, date_2: str, out: str = 'float') -> Union[str, float]:
    """
    Returns the time difference between two dates.

    Args:
    date_1 (str): The first date in 'YYYY-MM-DD' format.
    date_2 (str): The second date in 'YYYY-MM-DD' format.
    out (str, optional): Output format, either 'float' or 'string'. Defaults to 'float'.

    Returns:
    Union[str, float]: The time difference in days, either as a float or a string.
    """
    date_format = "%Y-%m-%d"
    time1 = datetime.strptime(date_1, date_format)
    time2 = datetime.strptime(date_2, date_format)
    diff = time2 - time1

    if out == 'float':
        return abs(diff.days)
    elif out == 'string':
        return str('there are ' + str(abs(diff.days)) + ' days between the two dates')
    else:
        raise ValueError("Invalid output format. Use 'float' or 'string'.")

print(time_diff('2009-06-17', '2006-06-17'))
print(time_diff('0209-01-03', '2020-01-01', 'string'))  # Should return '2'


# In[11]:


def reverse(in_list: list) -> list:
    """
    Returns the list in reverse order.

    Args:
    in_list (list): The input list.

    Returns:
    list: The input list in reverse order.
    """
    reversed_list = []
    for item in in_list:
        reversed_list.insert(0, item)
    return reversed_list

# Example usage
print(reverse(['a', 'b', 'c', 'd', 'e', '1']))  # Output: ['c', 'b', 'a']


# In[20]:


# Function to calculate factorial 
def fact(n):
	
	res = 1
	for i in range(2, n + 1): 
		res = res * i
	return res

# Applying the formula 
def prob_k_heads(n: int, k: int) -> float:
	
	output = fact(n) / (fact(k) * fact(n - k))
	output = output / (pow(2, n))
	return output

# Driver code
n = 40
k =30

# Call count_heads with n and r
print (prob_k_heads(n, k))

# This code is contributed by Pratik Basu 


# In[ ]:




