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

# print(calls[0])
# print(type(calls[0][0][0:3]))

#获取班加罗尔呼出的固话区号
def area_code(list8):
    list_a = []

    for token in list8:
        if token[0] == "(" :
            seq = token.find(")")
            list_a.append(token[:seq+1])
        #print(token)

    #print(list_a)
    return(list_a)

#获取班加罗尔呼出的移动号码前缀
def tel(list9):
    list_b = []

    for token in list9:
        #if token[0] == "7" or "8" or "9" :
        if (token[0] == "7") or (token[0] == "8") or (token[0] == "9")  :
            list_b.append(token[:4])

    return(list_b)

#获取被叫记录中，班加罗尔地区的电话号码
def ban_tel(list6):
    list_c = []

    for token in list6:
        if token[0:5] == "(080)":
            list_c.append(token)

    return(list_c)

def main(list):
    #list0保存班加罗尔呼叫的电话
    list0 = []

    #list1保存固话区号
    list1 = []

    #list2保存移动号码前缀
    list2 = []

    list3 = []

    list4 = []

    #获取班加罗尔拨出的通话记录，并存储被叫号码
    for token in list:
        if token[0][0:5] == "(080)":
            list0.append(token[1])
    #print(list0)

    list1 = area_code(list0)
    list2 = tel(list0)

    #print(list1)
    #print(list2)

    #list3保存班加罗尔地区拨出的所有电话的区号和移动前缀（代号）
    list3 = list1 + list2
    #print(list0)
    print("The numbers called by people in Bangalore have codes:")

    for token in list3:
         print(token)

    #list4保存被叫电话中属于班加罗尔的
    list4 = ban_tel(list0)

    #由班加罗尔固话打往班加罗尔的电话所占比例，精确到小数点后2位
    per = float('%.2f' % (len(list4)/len(list3)))
    #print(per)
    print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(per))

    return()

main(calls)



"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出由班加罗尔地区拨出的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字母顺序输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
