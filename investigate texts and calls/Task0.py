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

 """
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

#读取第一条短信记录和最后一条通话记录：
def task0(list_0,list_1):
    text_0 = 'First record of texts, {} texts {} at time {}'.format(list_0[0][0],list_0[0][1],list_0[0][2])
    call_1 = 'Last record of calls, {} calls {} at time {}, lasting {} seconds'.format(list_1[-1][0],list_1[-1][1],list_1[-1][2],list_1[-1][3])
    print(text_0)
    print(call_1)
    return(text_0,call_1)

task0(texts,calls)
