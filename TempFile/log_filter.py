#!/usr/bin/env python-2.7.3
import os
import sys

def filter_anr(path, pkg_name, outfile, list_anr):
    with open(path, 'r') as f, open(outfile, 'w') as fout, open(list_anr, 'w') as fanr:
        memory_list = []
        anr_list = []
        line = f.readline()
        write = 0
        while line:
            if 'Caused by: java.lang.OutOfMemoryError' in line:
                line = line[:-1]
                memory_list.append(line)
            if 1 == write:
                line = line[:-1]
                fout.write(line)
                fout.write('\n')
            if 'ANR in %s' % (pkg_name) in line:
                line = line[:-1]
                string = line.split('ANR')[1]
                if string not in anr_list:
                    anr_list.append(string)
                    fout.write(line)
                    fout.write('\n')
                    write = 1
            if 'DEBUG' in line:
                write = 0
            line = f.readline()
        fout.write('COUNT ANR is %s' % (len(anr_list)))
        fout.write('\n')
        fout.write('---------------------------')
        fout.write('\n')
        for item in memory_list:
            fout.write(item)
            fout.write('\n')
        for item in anr_list:
            fanr.write(item)
            fanr.write('\n')


def filter_fc(path, pkg_name, outfile):
    with open(path, 'r') as f, open(outfile, 'w') as fout:
        fc_list = []
        line = f.readline()
        write = 0
        fw = []
        while line:
            line = line[:-1]
            if 1 == write:
                fw.append(line)
            if 'Force-killing crashed app' in line:
                write = 0
                if 'Force-killing crashed app %s' % (pkg_name) in line:
                    fc_list.append(line)
                    for item in fw:
                        fout.write(item)
                        fout.write('\n')
            if 'FATAL' in line:
                fw = []
                write = 1
                fw.append(line)
            line = f.readline()
        fout.write('COUNT FC is %s' % (len(fc_list)))
        fout.write('\n')


if __name__ == '__main__':
    path = sys.argv[1]
    pkg_name = sys.argv[2]
    outanr = sys.argv[3]
    outfc = sys.argv[4]
    list_anr = sys.argv[5]
    filter_anr(path, pkg_name, outanr, list_anr)
    filter_fc(path, pkg_name, outfc)
