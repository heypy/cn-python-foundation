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
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
\"There are <count> different telephone numbers in the records.\"
"""
def get_phone_numbers(texts, calls):
    phone_numbers = set()

    for n in texts:
        phone_numbers.add(n[0])
        phone_numbers.add(n[1])

    for i in calls:
        phone_numbers.add(i[0])
        phone_numbers.add(i[1])
    
    return len(phone_numbers)

print("There are {} different telephone numbers in the records.".format(get_phone_numbers(texts, calls)))