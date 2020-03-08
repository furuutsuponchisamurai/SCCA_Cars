#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:33:40 2019

@author: AK47
"""
import tika
tika.initVM()
from tika import parser
from tabula import read_pdf
import re

#raw = parser.from_file('_data/Nationals_2019.pdf')
#print(raw['content'])

df = '_data/2019_Nationals.txt'
lines = None
with open('_data/2019_Nationals_Cleaned.txt', 'r') as file:
    lines = file.readlines()
    
prog = re.compile(r'(.+)\s(Drivers:)\s(\d{1,2})\s(Trophies:)\s(\d{1,2})')
r1 = re.compile(r'T{0,1}\s(\d{1,3})\s(\d{1,3})\s(\w.+)\s(\d{4})\s(\w.+)\s(\w+)')
r2 = re.compile(r'^(\[(\d{1,3})\])?(\s)?(\w+)\,\s(\w{2})\s(\w.+)\s(\w+)$')
ind_times = re.compile(r'(?<!\d{1})(\d{2}\.\d{3})+')
ind_score = re.compile(r'(\d{3}\.\d{3})')
test = lines[:150]

result = prog.search(lines[5])