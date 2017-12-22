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
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
texts_line = texts[0]
calls_line = calls[-1]

print("First record of texts, {} texts {} at time {}".format(texts_line[0], texts_line[1], texts_line[2]))
print("Last record of calls, {} texts {} at time {}".format(calls_line[0], calls_line[1], calls_line[2]))

