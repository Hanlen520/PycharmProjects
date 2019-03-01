import re
import os
#需要处理的文件夹路径（绝对路径）
path = "/Users/a140/Desktop/testt"
#存放结果的文件路径（绝对路径）
results = "/Users/a140/Desktop/results.txt"
file_list = os.listdir( path )
file_list.sort()
for file in file_list:
    fo = open( path + '/' + file, "r")
    print("fileName: ", fo.name)
    resu = open(results, "a+")
    resu.write(fo.name + '\n')
    for line in fo.readlines():
        if len(re.findall('TOTAL:', line)) != 0:
            tmp = line
    fo.close()
    TotalLine = tmp.split('TOTAL SWAP')[0].split(': ')
    print('Name: {}, TotalNum:{}'.format(TotalLine[0], TotalLine[1]))
    resu.write('Name: {}, TotalNum:{}'.format(TotalLine[0], TotalLine[1]) + '\n\n')
    resu.close()