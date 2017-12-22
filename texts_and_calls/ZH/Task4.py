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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

"""
判断电话号码是否发送或接收过短信
"""
def is_texter(phone, texts):
    for n in texts:
        if n[0] == phone or n[1] == phone:
            return True

    return False

"""
判断电话号码是否接收到来电
"""
def is_caller(phone, calls):
    for n in calls:
        if n[1] == phone:
            return True
    return False

"""
输出电话推销员电话号码
"""
def out_telemarketers(calls, texts):
    print("These numbers could be telemarketers: ")
    # sets = set()
    for n in calls:
        if is_texter(n[0], texts) == False and is_caller(n[0], calls) == False:
            # sets.add(n[0])
            print("{}".format(n[0]))
    
    # return list(sets)

out_telemarketers(calls, texts)