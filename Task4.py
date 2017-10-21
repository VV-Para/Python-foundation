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

#提取主叫/发送电话号码
def send(list):
    list0 = []
    for token in list:
        list0.append(token[0])
    return(list0)

#提取被叫/接收电话号码
def reci(list):
    list0 = []
    for token in list:
        list0.append(token[1])
    return(list0)

#去掉列表中的重复项
def derep(list):
    list0 = []

    for token in list:
        if token not in list0:
            list0.append(token)

    return(list0)

def main(list1,list2):
    tel_sen = []
    tel_rec = []
    ms_sen = []
    ms_rec = []
    telemark0 = []
    telemark = []

    #从原始清单整理出主叫电话列表
    tel_sen = send(list1)

    # 从原始清单整理出被叫电话列表
    tel_rec = reci(list1)

    # print(tel_sen)
    # print(tel_rec)
    # 从原始清单整理出发送短信的电话列表
    ms_sen = send(list2)

    # 从原始清单整理出接受短信的电话列表
    ms_rec = reci(list2)

    # print(ms_sen)
    # print(ms_rec)

    #检测可疑电话
    for token in tel_sen:
        if token in tel_rec:
            continue
        elif token in ms_sen:
            continue
        elif token in ms_rec:
            continue
        else:
            telemark0.append(token)
            #print(token)

    telemark = derep(telemark0)

    #print(len(telemark),len(telemark0))
    #print(len(tel_sen),len(telemark))
    print("These numbers could be telemarketers: ")
    #print(telemark)

    for token in telemark:
        print(token)
    return()

main(calls,texts)

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字母顺序输出。
"""

