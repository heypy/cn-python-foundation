# -*- coding: utf-8 -*-
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
import os
homedir = os.getcwd()

with open(homedir+'/texts_and_calls/ZH/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open(homedir+'/texts_and_calls/ZH/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

def longest_call(calls):
    dist = {}
    for i in calls:
        if i[0] in dist:
            dist[i[0]] += int(i[3])
        else:
            dist[i[0]] = int(i[3])

        if i[1] in dist:
            dist[i[1]] += int(i[3])
        else:
            dist[i[1]] = int(i[3])

    sortV = [ v for v in sorted(dist.values())]
    sortK = [ k for k in sorted(dist.keys())]
    return [sortK[-1], sortV[-1]]

res = longest_call(calls)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(res[0], res[1]))