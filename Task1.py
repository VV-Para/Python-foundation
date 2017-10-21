"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#print(texts)
#print(calls)

#遍历list0，找出不在list1中的新元素
def trav(list0,list1):
    tmp = list1

    for token0 in list0:
        if token0[1] not in tmp:
            tmp.append(token0[1])

        if token0[2] not in tmp:
            tmp.append(token0[2])

    return(tmp)

#统计短信和通话记录中电话号码的数量
def count(list0,list1):
    tmp = []

    #思路：分别对短信和电话记录列表进行遍历，发现新的电话号码后立即放入tmp列表中
    #对短信记录进行统计
    tmp0 = trav(list0,tmp)

    #在短信记录的统计结果之上，增加对通话记录的统计
    tmp1 = trav(list1,tmp0)
    # for token0 in list0:
    #     if token0[1] not in tmp:
    #         tmp.append(token0[1])
    #
    #     if token0[2] not in tmp:
    #         tmp.append(token0[2])
    #
    # #print(len(tmp))
    #
    # for token1 in list1:
    #     if token1[1] not in tmp:
    #         tmp.append(token1[1])
    #
    #     if token1[2] not in tmp:
    #         tmp.append(token1[2])

    #print(len(tmp))

    #统计电话号码列表的长度
    num = "There are {} different telephone numbers in the records.".format(len(tmp1))

    return(num)

print(count(texts,calls))
"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
