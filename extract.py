#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:33:40 2019

@author: AK47
#"""
#import tika
#tika.initVM()
#from tika import parser
#from tabula import read_pdf
import re

#raw = parser.from_file('_data/Nationals_2019.pdf')
#print(raw['content'])

#df = '_data/2019_Nationals.txt'
lines = None
with open('_data/2019_Nationals_Cleaned.txt', 'r') as file:
    lines = file.readlines()

# Prog has 3
prog = re.compile(r'(.+)\s(Drivers:)\s(\d{1,2})\s(Trophies:)\s(\d{1,2})')
r1 = re.compile(r'T{0,1}\s(\d{1,3})\s(\d{1,3})\s(\w.+)\s(\d{4})\s(\w.+)\s(\w+)')
r2 = re.compile(r"^(M\s)?(\[(\d{1,3})\]\s)?(.+?)\,\s(\w{2})(.+)")
ind_times = re.compile(r'(?<!\d{1})(\d{2}\.\d{3})+')
ind_score = re.compile(r'(\d{3}\.\d{3})')
test = lines[:150]
test1 = lines[:115]
result = prog.search(lines[5])
res = ind_times.findall(lines[13])
ress = ind_score.search(lines[13])
dinfo = r1.search(lines[6])
dback = r2.search(lines[17])
info_list = []
divisions = ["Southwest", "Central", "Rocky Moun", "SoPac", "NorPac", "Northeast", "Midwest", "Great Lakes", "Southeast"]

#
test1 = lines
# Process data
data = []
class_data = []
driver_class = ''
trophies = 0

for l in range(0,7008):
    class_info = prog.search(test1[l])
    if class_info:
        driver_class = class_info[1]
        num_drivers = class_info[3]
        trophies = class_info[5]
        
        class_data.append([driver_class, num_drivers, trophies])
        
    dinfo = r1.search(test1[l])
    if dinfo:
        dloc = r2.search(test1[l+1])
        dtimes = ind_times.findall(test1[l+2] + test1[l+3])
        dscore = ind_score.search(test1[l+2])[1]
        tire = test1[l+4]
        dpos = dinfo[1]
        dnum = dinfo[2]
        dname = dinfo[3]
        dcar_year = dinfo[4]
        dcar = dinfo[5]
        dreg = dinfo[6]
        if dloc[3]:
            doube_drive = True
        elif not dloc[3]:
            double_drive = False
        for d in divisions:
            if d in dloc[6]:
                ddiv = d
            else:
                ddiv = "Unknown"
        dcity = dloc[4]
        dstate = dloc[5]
        if class_data[-1][-1] >= dpos:
            hasTrophy = True
        else:
            hasTrophy = False

        data.append([dnum, dname, dpos, class_data[-1][0], hasTrophy, dcar_year, dcar, dreg, ddiv, tire, dcity, dstate])
        
        