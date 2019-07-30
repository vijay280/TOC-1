# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:37:45 2019

@author: Student
"""

s=input()
if(s.count('[')==s.count(']') and s.count('{')==s.count('}') and s.count('(')==s.count(')')):
    print("balanced")
else:
    print("unbalanced")