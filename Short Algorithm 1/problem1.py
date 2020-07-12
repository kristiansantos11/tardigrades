# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:21:18 2020

@author: Rahino Quijano, Jedidiah Calayag, Leo Mark Castro, Kristian Santos
"""

test_case = int(input()) # number of cases

for x in range(test_case):
    items = list() # The items will be listed here
    query = list()
    n, q = map(int,input().split())  # number of items & number of queries

    # inputting the items: Strings are stored inside a list
    for _ in range(n):
        i = input() # Appends a list in the items list
        items.append(" " + i + " ")

    # inputting the queries: Strings are stored inside a list
    for _ in range(q):
        q_in = input()
        query.append(" " + q_in + " ")
    
    print("Case " + str(x + 1) + ":")
            
    for g in query:
        match = [test for test in items if g in test]
        print(len(match))      
      
      
#mode of input:
'''
2 							#number of batches
2 3 						#x y || x = number of lines to be stored in a database | y = number of lines to be tested to the database
ha he ho					
ho hu he hi ha
ha
he
mi
3 4							#new database and line to be tested initiated
ma me mi
mo mu me mi
me ma mo
as
ad
ma
me
'''
