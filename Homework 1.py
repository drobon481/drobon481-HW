{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "9ceb78ee-008a-4ba8-8129-f2ef89bc3fa4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://github.com/drobon481/drobon481/blob/main/Homework%201\n"
     ]
    }
   ],
   "source": [
    "def github() -> str:\n",
    "    \"\"\"\n",
    "    Returns a link to solutions on GitHub.\n",
    "    \"\"\"\n",
    "    return \"https://github.com/drobon481/drobon481/blob/main/Homework%201\"\n",
    "\n",
    "print(github())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "492ae704-cd09-4b81-8b3e-baf2c7ae75d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import scipy as sc\n",
    "import matplotlib as mpl\n",
    "import seaborn as sb\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea6d732b-f25c-48f3-84c9-db7fcdadf326",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "0f2f0aab-5afa-4546-bd13-98eddfb79f05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'evens': 2550, 'odds': 2500}\n"
     ]
    }
   ],
   "source": [
    "def evens_and_odds(n: int) -> dict:\n",
    "    \"\"\"\n",
    "    Returns a dictionary with the sum of even and odd numbers less than n.\n",
    "    \n",
    "    Args:\n",
    "    n (int): A natural number\n",
    "    \n",
    "    Returns:\n",
    "    dict: A dictionary with keys 'evens' and 'odds' containing the sum of even and odd numbers less than n respectively.\n",
    "    \"\"\"\n",
    "    evens_sum = sum(i for i in range(n) if i % 2 == 0)\n",
    "    odds_sum = sum(i for i in range(n) if i % 2 != 0)\n",
    "    \n",
    "    return {'evens': evens_sum, 'odds': odds_sum}\n",
    "\n",
    "# Example usage\n",
    "result = evens_and_odds(101)\n",
    "print(result)  # Output: {'evens': 2, 'odds': 4}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "454fef32-e6b9-4bc2-a4f3-84d013c0bda6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1096\n",
      "there are 661452 days between the two dates\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime\n",
    "\n",
    "def time_diff(date_1: str, date_2: str, out: str = 'float') -> Union[str, float]:\n",
    "    \"\"\"\n",
    "    Returns the time difference between two dates.\n",
    "\n",
    "    Args:\n",
    "    date_1 (str): The first date in 'YYYY-MM-DD' format.\n",
    "    date_2 (str): The second date in 'YYYY-MM-DD' format.\n",
    "    out (str, optional): Output format, either 'float' or 'string'. Defaults to 'float'.\n",
    "\n",
    "    Returns:\n",
    "    Union[str, float]: The time difference in days, either as a float or a string.\n",
    "    \"\"\"\n",
    "    date_format = \"%Y-%m-%d\"\n",
    "    time1 = datetime.strptime(date_1, date_format)\n",
    "    time2 = datetime.strptime(date_2, date_format)\n",
    "    diff = time2 - time1\n",
    "\n",
    "    if out == 'float':\n",
    "        return abs(diff.days)\n",
    "    elif out == 'string':\n",
    "        return str('there are ' + str(abs(diff.days)) + ' days between the two dates')\n",
    "    else:\n",
    "        raise ValueError(\"Invalid output format. Use 'float' or 'string'.\")\n",
    "\n",
    "print(time_diff('2009-06-17', '2006-06-17'))\n",
    "print(time_diff('0209-01-03', '2020-01-01', 'string'))  # Should return '2'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "387517fb-e05a-47a9-9e13-09bf5bfb8bc7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['1', 'e', 'd', 'c', 'b', 'a']\n"
     ]
    }
   ],
   "source": [
    "def reverse(in_list: list) -> list:\n",
    "    \"\"\"\n",
    "    Returns the list in reverse order.\n",
    "\n",
    "    Args:\n",
    "    in_list (list): The input list.\n",
    "\n",
    "    Returns:\n",
    "    list: The input list in reverse order.\n",
    "    \"\"\"\n",
    "    reversed_list = []\n",
    "    for item in in_list:\n",
    "        reversed_list.insert(0, item)\n",
    "    return reversed_list\n",
    "\n",
    "# Example usage\n",
    "print(reverse(['a', 'b', 'c', 'd', 'e', '1']))  # Output: ['c', 'b', 'a']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "585b298f-2c03-4628-b87b-e1fd0507338a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.0007709427591180429\n"
     ]
    }
   ],
   "source": [
    "# Function to calculate factorial \n",
    "def fact(n):\n",
    "\t\n",
    "\tres = 1\n",
    "\tfor i in range(2, n + 1): \n",
    "\t\tres = res * i\n",
    "\treturn res\n",
    "\n",
    "# Applying the formula \n",
    "def prob_k_heads(n: int, k: int) -> float:\n",
    "\t\n",
    "\toutput = fact(n) / (fact(k) * fact(n - k))\n",
    "\toutput = output / (pow(2, n))\n",
    "\treturn output\n",
    "\n",
    "# Driver code\n",
    "n = 40\n",
    "k =30\n",
    "\n",
    "# Call count_heads with n and r\n",
    "print (prob_k_heads(n, k))\n",
    "\n",
    "# This code is contributed by Pratik Basu \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "613f7a23-faad-409f-a0a7-4d2352a73805",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
