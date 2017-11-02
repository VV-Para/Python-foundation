import expanddouban
import bs4
import requests
import csv
import time
import datetime

"""
任务1：获取每个地区、每个类型页面的URL
return a string corresponding to the URL of douban movie lists given category and location.

所需函数：getMovieUrl
"""

"""
[任务1]
函数getMovieUrl
功能：返回给定地区、类型的豆瓣电影页面的URL
输入：category（字符串）
	  location（字符串）	
输出：url（字符串）
"""
def getMovieUrl(category,location):
    
    return 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影' + ',' + category + ',' + location

"""
任务 2：通过 URL 获得豆瓣电影页面的 HTML
get HTML context of movie web 

所需函数：Html
"""	

"""
[任务 2]
函数Html
功能：返回给定地区、类型的豆瓣电影页面的URL
输入：category,类别名字（字符串）
	  location，地区名字（字符串）	
输出：给定地区、类型的豆瓣电影页面的URL（字符串）
"""
def Html(url):
    
    html = expanddouban.getHtml(url)

    return html

"""
任务 3:定义电影类 Define class of Movie
功能：定义电影类,实现电影类的构造函数

所需函数：class_Moviel
"""

"""
[任务 3]
函数class_Movie
功能：定义电影类,实现电影类的构造函数
输入：name,电影名字；rate,评分；location,电影所属地区；category,电影所属类别；info_link,电影页面链接；cover_link，电影海报图片链接	
输出：m，电影对象（object）
"""

def class_Movie(name, rate,location,category,info_link,cover_link):
	
	class Movie():
	
		#定义构造方法
		def __init__(self,n,r,l,ca,inf,co):
			self.name_s = n
			self.rate_s = r
			self.location_s = l
			self.category_s = ca
			self.info_link_s = inf
			self.cover_link_s = co

	m = Movie(name,rate,location,category,info_link,cover_link)
	
	return m


	
"""
任务4: 获得豆瓣电影的信息
功能：完整的构造每一个电影，并保存到一个列表中

所需函数：getMovies
"""

"""
[任务 4]
函数getMovies
功能：获取符合给定类别和地点的电影的列表，return a list of Movie objects with the given category and location.
输入：category,爬取的电影类型； location，爬取的电影地区
输出：movie_list（二维列表）。该列表中，每个元素为一个列表，保存了一部电影的名字、评分等信息。
"""
def getMovies(category,location):
	url = getMovieUrl(category,location)
	
	list_movie = []
	
	html = Html(url)
	
	soup = bs4.BeautifulSoup(html,"html.parser")
	
	content_div = soup.find(id="app").find(class_="list-wp")
	
	movie_list = []
	
	#根据<a>标签，识别出每一部电影
	for element in content_div.find_all("a"):
		tmp = []
		
		#获取电影页面链接和海报链接
		info_link_t = (element.get('href'))
		cover_link_t = (element.find("img").get('src'))
		
		#根据<p>标签，获取电影的标题和评分
		if element.find("p"):
			title_t = (element.find(class_="title").get_text())

			rate_t = (element.find(class_="rate").get_text())
		
		#将爬取到关于这部电影的各种信息保存到对象item_Movie中
		item_Movie = class_Movie(title_t, rate_t, location, category, info_link_t, cover_link_t)
		
		#tmp列表保存了一部电影的各种信息
		tmp.append(item_Movie.name_s)
		tmp.append(item_Movie.rate_s)
		tmp.append(item_Movie.location_s)
		tmp.append(item_Movie.category_s)
		tmp.append(item_Movie.info_link_s)
		tmp.append(item_Movie.cover_link_s)
		
		#构建二维列表
		movie_list.append(tmp)
	
	return movie_list

"""
任务5: 构造电影信息数据表
功能：从网页上选取你最爱的三个电影类型，然后获取每个地区的电影信息后，
我们可以获得一个包含三个类型、所有地区，评分超过9分的完整电影对象的列
表。将列表输出到文件 movies.csv

所需函数：w_csv,r_csv，main_movie
"""

"""
函数w_csv:CSV文件写模块
"""	
def w_csv(list):
	with open('movies.csv','w',newline='') as csvfile:
		moviewriter = csv.writer(csvfile, dialect='excel')
		
		for movie in list:
			moviewriter.writerow(movie)
	return

"""
函数r_csv:CSV文件读模块。将读取到的内容保存到列表list_r中。
"""	
def r_csv():
	list_r = []
	with open('movies.csv','r') as csvfile:
		moviereader = csv.reader(csvfile)
		
		for row in moviereader:
			list_r.append(row)
			
	return list_r

"""
任务6：将电影的统计结果输出到 output.txt。
包含你选取的每个电影类别中，数量排名前三的地区有哪些，分别占此类别电影总数的百分比为多少。

所需函数：Statistic_Cate,Dict_Movie，List_Output
"""

"""
Statistic_Cate函数：统计每种类型电影的总量，返回字典cate_dict，{类型：数量}
输入：二维列表，保存了页面内容中每一部电影的信息
输出：字典，电影类型：数量
"""
def Statistic_Cate(list):
	#字典cate_dict存储每种类型电影的数量
	cate_dict = {}
	
	#item代表一部电影，第3项表示地区，第4项表示类型
	#统计每个类型的电影数量
	for item in list:
		if item[3] in cate_dict:
			cate_dict.update({item[3]:(cate_dict[item[3]]+1)})
		else:
			cate_dict.update({item[3]:1})
	
	return cate_dict
	
"""
Dict_Movie函数：统计电影信息，返回一个二维字典。该字典会统计各种类型的电影中，属于每个地区的数量
输入：list，列表，保存了页面内容中每一部电影的信息
输出：movie_dict，二维字典。{类型：{地区：数量}}
"""
def Dict_Movie(list):
	
	#二维字典movie_dict存储每种类型电影中每个地区的数量
	movie_dict = {}
		
	#item的第3项表示电影的地区，第4项表示电影的类型
	#统计每个类型中每个地区的数量
	for item in list:
		if item[3] in movie_dict:
			if item[2] in movie_dict[item[3]]:
				movie_dict[item[3]].update({item[2]:(movie_dict[item[3]][item[2]]+1)})

			else: 
				movie_dict[item[3]].update({item[2]:1})
		else:
			movie_dict.update({item[3]:{item[2]:1}})
		
	return movie_dict

"""
函数List_Output：对每种类型的电影进行统计，结果保存在字典中。字典结构：{地区：该地区的电影占此类别电影总数的百分比}
输入参数：list，降序列表，[（地区，数量）]；num，整数，某类型电影的总数；max，整数，取前几大值
输出：列表[元组]，[（地区：百分比）]，共有max项。表示数量排名前max的地区及所占百分比
"""
def List_Output(list,num,max):
	cnt = 0
	list_loca = []
	list_val = []
	list_out = []
	
	#取前max大值
	for i in range(len(list)):
		cnt += 1
		if cnt > max:
			break
		
		loca = list[i][0]
		#保留小数点后2位
		val = float('%.2f' % (100*(list[i][1]/num)))
		
		list_loca.append(loca)
		list_val.append(str(val) + "%")
		
	list_out.append (list_loca)
	list_out.append(list_val)
		
	return list_out

"""
函数 w_txt：将每种类型电影的统计结果写入到txt文件。
输入参数：category，电影类型；list，列表，{地区：百分比}
输出：无。	
"""	
def w_txt(category,list):
	with open('output.txt','a') as f:
		f.write("---" * 18)
		#记录写入文件时间
		f.write(datetime.datetime.now().strftime('  %Y-%m-%d %H:%M:%S  '))
		f.write("---" * 18)
		f.write("\n")
		
		str0 = "{}类别电影中，数量排名前三的地区包括：".format(category)
		f.write(str0)
		f.write(",".join(str(loca) for loca in list[0]) + "。")
		f.write('分别占此类别电影总数的百分比为:')
		f.write(",".join(str(per) for per in list[1]) + "。")
		f.write("\n" * 2)
	
	return
	
	
"""
主程序
"""
def main(category0,category1,category2):
	#记录程序开始运行的时间：
	with open('output.txt','a') as f:
		f.write("Start crawler at: ")
		f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		f.write("\n" * 2)
	
	dict1 = {}
	dict2 = {}
	
	
	#电影所属国家列表
	location_list = ["大陆","美国","香港","台湾","日本","韩国","英国","法国","德国","意大利","印度","泰国","俄罗斯","伊朗","加拿大","澳大利亚","爱尔兰","瑞典","巴西","丹麦"]
	
	#电影类型
	cate_list = [category0,category1,category2]
		
	#列表movie_total汇总爬取到的电影信息
	movie_total = []
	
	#根据国家、类型进行遍历，保存爬取的电影信息
	for cate in cate_list:
		#tmp0 = []
		for loca in location_list:
			tmp = getMovies(cate, loca)		
			movie_total += tmp
	
	#将爬取到的电影信息写入csv文件（会清空上一次写入）
	w_csv(movie_total)
	
	#读取生成的csv文件，以供任务6进行分析
	read = r_csv()
	
	#dict1:统计每种类型电影的总量
	dict1 = Statistic_Cate(read)
	
	#dict2:统计各种类型电影中，每个地区的数量
	dict2 = Dict_Movie(read)
	
	#各种类型电影中，按电影数量对地区进行降序排列
	for cate in dict2:
		list3 = []
		cate_dict2 = []
		
		#获取某种类型的电影总数num
		num = int(dict1[cate])
		
		#对每种类型，按照电影数量对地区进行降序排列，获得列表cate_dict2
		cate_dict2 = sorted(dict2[cate].items(),key=lambda item:item[1],reverse=True)

		list3 = List_Output(cate_dict2,num,3)
		
		#将当前类型电影的最终统计结果写入txt文件（不清空连续写入）
		w_txt(cate,list3)
					
	return

if __name__ == '__main__':

	main("剧情","悬疑","战争")

	
	
	
	
	
	
	
	
	
	
	
	
	
	
