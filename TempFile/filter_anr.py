#!/usr/bin/env python-2.7.3
import os
import sys

def compare_str(str1, str2):
    str1_list = str1.split(' ')
    str2_list = str2.split(' ')
    if len(str1_list) != len(str2_list):
        return 0
    else:
        count = 0
        for i in range(0, len(str1_list)):
            if str1_list[i] == str2_list[i]:
                count = count + 1
        if count > len(str1_list)-3:
            return 1
        else:
            return 0

def compare_same(cmp1, cmp2):
    if len(cmp1) == len(cmp2):
        count = 0
        for i in range(0, len(cmp1)):
            if compare_str(cmp1[i], cmp2[i]) == 1:
                count = count + 1
        if count > len(cmp1)-3:
            return 1
        else:
            return 0
    i = 0
    j = 0
    while i < len(cmp1) and j < len(cmp2):
        if compare_str(cmp1[i], cmp2[j]) == 1:
            i = i + 1
            j = j + 1
        elif i == len(cmp1)-1 and j == len(cmp2)-1:
            break
        elif i < len(cmp1)-1 and j == len(cmp2)-1: 
            if compare_str(cmp1[i+1], cmp2[j]) == 1:
                i = i + 1
            else:
                break
        elif i == len(cmp1)-1 and j < len(cmp2)-1: 
            if compare_str(cmp1[i], cmp2[j+1]) == 1:
                j = j + 1
            else:
                break
        elif compare_str(cmp1[i+1], cmp2[j]) == 1:
            i = i + 2
            j = j + 1
        elif compare_str(cmp1[i], cmp2[j+1]) == 1:
            i = i + 1
            j = j + 2
        else:
            if len(cmp1) > len(cmp2):
                i = i + 1
            else:
                j = j + 1
    if i == len(cmp1) and j == len(cmp2):
        ret =  1
    else:
        ret = 0
    return ret


file_path = sys.argv[1]
f = open(file_path)
line = f.readline()
store = []
temp = []
uniq = 0
count = 0
compare = 0
record = 0
same = 0
system = 0

while line:
    line = line[:-1]
    if '***'  in line:
        record = 1
    if record == 1:
        temp.append(line)
    if 'Crash dump' in line and '***' not in line:
        if compare == 1:
            count = count + 1
        if compare == 1 and system == 0:
            if store == []:
                store.append(temp)
                uniq = uniq + 1
            else:
                for item in store:
                    same = same + compare_same(item, temp)
                if same == 0:
                    store.append(temp)
                    uniq = uniq + 1
        temp = []
        record = 0
        compare = 0
        system = 0
        same = 0
    if 'com.cootek.smartinputv5' in line:
        compare = 1
    if 'system' in line:
        system = 1
    line = f.readline()
f.close()
print count, uniq
f = open('result', 'w+')
f.write(str(count))
f.write('\n')
f.write(str(uniq))
f.write('\n')
for column in store:
    for row in column:
        f.write(row)
        f.write('\n')
    f.write('\n')
f.close()
