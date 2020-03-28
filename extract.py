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
import re, csv

#raw = parser.from_file('_data/Nationals_2019.pdf')
#print(raw['content'])

#df = '_data/2019_Nationals.txt'
lines = None
with open('_data/2019_Nationals_Cleaned.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip(" \n") for line in lines]

# Prog has 3
prog = re.compile(r'(.+)\s(Drivers:)\s(\d{1,2})\s(Trophies:)\s(\d{1,2})')
r1 = re.compile(r'(T{0,1}\s)?(\d{1,3})\s(\d{1,3})\s(\w.+)\s(\d{4})\s(\w.+)\s(\w+)')
r2 = re.compile(r"^(M\s)?(\[(\d{1,3})\]\s)?(.+?)?\,\s(\w{2})?(.+)")
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
data = [['DriverNumber', 'DriverName', 'DriverPosition', 'RaceClass','WonTrophy','IsDoubleDriving','DoubleDriverNumber',
         'CarYear','Manufacturer','Car','Region','Division','Tire','City','State']]
class_data = []
driver_class = ''
trophies = 0

for l in range(0, (len(test1)-3)):
    class_info = prog.search(test1[l])
    if class_info:
        driver_class = class_info[1]
        num_drivers = class_info[3]
        trophies = class_info[5]
        ddrivers = []
        class_data.append([driver_class, num_drivers, trophies])
        
    dinfo = r1.search(test1[l])
    if dinfo:
        dloc = r2.search(test1[l+1])
        dtimes = ind_times.findall(test1[l+2] + test1[l+3])
        try:
            dscore = ind_score.search(test1[l+2])[1]
        except TypeError:
            dscore = 0
            
        tire = test1[l+4]
        dpos = dinfo[2]
        dnum = int(dinfo[3].strip())
        dname = dinfo[4]
        dcar_year = dinfo[5]
        dcar = dinfo[6]
        dreg = dinfo[7]
        
        if dloc[3]:
            double_drive = True
            ddnum = int(dloc[3].strip())
            ddrivers.append((dinfo[3], ddnum))
            
        elif not dloc[3]:
            double_drive = False
            ddnum = 0
            
        ddiv = 'Unknown'
        for d in divisions:
            if d in dloc[6]:
                ddiv = d
        try:
            dcity = dloc[4]
            dstate = dloc[5]
        except TypeError:
            dcity = ''
            dtstate = ''
            
        if class_data[-1][-1] >= dpos:
            hasTrophy = 1
        else:
            hasTrophy = 0
        
        if dcar == 'Chevrolet Corvette Z0':
            dcar = 'Chevrolet Corvette Z06'
            
        dcar = dcar.split(' ',1)
        
        if len(dcar) == 1:
            dcar.append(dreg)
        dcar[1] = dcar[1].replace('-','')
            
        if dcar[1].upper() in ('SHINSEN','MX5','MIATA', 'MX5 MIATA'):
            dcar[1] = 'Miata'
        data.append([dnum, dname, dpos, class_data[-1][0], hasTrophy, 
                     double_drive, ddnum, dcar_year, dcar[0],dcar[1], dreg, ddiv, tire, dcity, dstate])
        
        double_drive = None
        ddnum = None
#        double_drive_driver = None
#        double_drive_driver_num = None
        
with open('_data/NationalsDrivers2019.tsv', 'w') as tsvfile:
    carwriter = csv.writer(tsvfile, delimiter='\t')
    for line in data:
        carwriter.writerow(line)