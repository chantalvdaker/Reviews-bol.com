#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
In dit bestand worden verschillende keywords geteld die voorkomen in de reviews van Bol.com voor 2020
'''

# Tellen hoeveel reviews in 2020 over het keyword 'bezorg' gaan
count_bezorg = 0
for i in df_2020['review']:
    try:
        
        if 'bezorg' in i:
            count_bezorg += 1
    except:
        
        continue
        
print('Het aantal reviews met bezorg erin in 2020 is ' + str(count_bezorg))

# Tellen hoeveel reviews in 2020 over het keyword 'product' gaan
count_product = 0
for i in df_2020['review']:
    try:
        
        if 'product' in i:
            count_product += 1
    except:
        
        continue
        
print('Het aantal reviews met product erin in 2020 is ' + str(count_product))

# Tellen hoeveel reviews in 2020 over het keyword 'service' gaan
count_service = 0
for i in df_2020['review']:
    try:
        
        if 'service' in i:
            count_service += 1
    except:
        
        continue
        
print('Het aantal reviews met service erin in 2020 is ' + str(count_service))

# Tellen hoeveel reviews in 2020 over het keyword 'levering' gaan
count_levering = 0
for i in df_2020['review']:
    try:
        
        if 'levering' in i:
            count_levering += 1
    except:
        
        continue
        
print('Het aantal reviews met levering erin in 2020 is ' + str(count_levering))

# Tellen hoeveel reviews in 2020 over het keyword 'slecht' gaan
count_slecht = 0
for i in df_2020['review']:
    try:
        
        if 'slecht' in i:
            count_slecht += 1
    except:
        
        continue
        
print('Het aantal reviews met slecht erin in 2020 is ' + str(count_slecht))

# Tellen hoeveel reviews in 2020 over het keyword 'goed' gaan
count_goed = 0
for i in df_2020['review']:
    try:
        
        if 'goed' in i:
            count_goed += 1
    except:
        
        continue
        
print('Het aantal reviews met goed erin in 2020 is ' + str(count_goed))

# Tellen hoeveel reviews in 2020 over het keyword 'nep' gaan
count_nep = 0
for i in df_2020['review']:
    try:
        
        if 'nep' in i:
            count_nep += 1
    except:
        
        continue
        
print('Het aantal reviews met nep erin in 2020 is ' + str(count_nep))

# Tellen hoeveel reviews in 2020 over het keyword 'misleid' gaan
count_misleid = 0
for i in df_2020['review']:
    try:
        
        if 'misleid' in i:
            count_misleid += 1
    except:
        
        continue
        
print('Het aantal reviews met misleid erin in 2020 is ' + str(count_misleid))

