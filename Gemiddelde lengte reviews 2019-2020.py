#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" In dit bestand wordt uitgelegd hoe de gemiddelde lengte in tekens van de reviews voor zowel 2019 als 2020 worden berekend.
"""

# De gemiddelde lengte van een review in tekens voor 2019
total_len_2019 = 0 
for record in records_2019:
    total_len_2019 += record['lengte-review']
mean_len_2019 = total_len_2019/len(records_2019)
print('Gemiddelde lengte van reviews in 2019 is ' + str(mean_len_2019))
Gemiddelde lengte van reviews in 2019 is 283.45706618962436


# De gemiddelde lengte van een review in tekens voor 2020
total_len_2020 = 0 
for record in records_2020:
    total_len_2020 += record['lengte-review']
mean_len_2020 = total_len_2020/len(records_2020)
print('Gemiddelde lengte van reviews in 2020 is ' + str(mean_len_2020))

