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

#将原始通话记录列表转换成“电话号码-通话时间”形式的字典
def list_to_dict(list1):
    dict_tmp = {}

    for token in list1:
        #遍历主叫号码
        if token[0] in dict_tmp.keys():
            dict_tmp[token[0]] += int(token[3])
        else:
            dict_tmp[token[0]] = int(token[3])

        # 遍历被叫号码
        if token[1] in dict_tmp.keys():
            dict_tmp[token[1]] += int(token[3])
        else:
            dict_tmp[token[1]] = int(token[3])
        #print(dict_tmp[token[0]])
    return(dict_tmp)

#查找出通话时间最长的电话号码：
def max_time(list1):

    dict_tmp = list_to_dict(list1)

    # 找出新生成的字典中最大值，max_time的数据类型是tuple
    max_time = max(zip(dict_tmp.values(),dict_tmp.keys()))

    log = "{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_time[1],max_time[0])

    print(log)
    return(log)

#print(max_time(calls))
max_time(calls)




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

