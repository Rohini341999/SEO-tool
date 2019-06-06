"""
Created by : Rohini Koli  
Project topic : SEO Analyser tool
Start date : 04-06-2019
End Date : 06-06-2019
Completion time : 16:53
"""
class seo:
	def __init__(self,url):
		self.url=url
	def totalnoofscripts(abc):
		fo = urlopen(url)
		html = fo.read()
		ctr=0
		soup = BeautifulSoup(html,"html.parser")
		for s in soup(["script"]):
			s.extract()
			ctr+=1
		fo.close()
		print("There are ",ctr," number of scripts")
		print("~"*120)
		
	def displaylistofscript(abc):
		fo = urlopen(url)
		html = fo.read()
		soup = BeautifulSoup(html,"html.parser")
		print("SCRIPTS:-\n")
		scriptlist=[]
		for s in soup(["script"]):
			s.extract()
			scriptlist.append(s)
		fo.close()
		print(scriptlist)
		print("~"*120)
	
	def totalnumofwords(abc):
		fo = urlopen(url)
		html = fo.read()
		fo.close()
		soup = BeautifulSoup(html,"html.parser")
		for s in soup(["style","script"]):
			s.extract()
		text = soup.get_text()
		words = text.split()
		print(words)
		worddict = {}
		count=0
		for word in words:
			worddict.setdefault(word,words.count(word))
		for key,value in worddict.items():
			if value >= 1:
				count+=1
		print("There are ",count,"number of words excluding the style and script tags")
		print("~"*120)

	def keywordmeta(abc):
		fo = urlopen(url)
		html = fo.read()
		fo.close()
		soup = BeautifulSoup(html,"html.parser")
		counter=0
		keyworddict={}
		for meta in soup(["meta"]):
			if "Keywords" in str(meta):
				keywords = meta.attrs["content"].split(",")
				for keyword in keywords:
					keyworddict.setdefault(keyword,keyword.count(keyword))
				for key,value in keyworddict.items():
					if value>=1:
						counter+=1
				print(keyworddict)
		if not "Keywords" in str(meta):
			print("There are no keywords in meta tag")		
		workbook = xlsxwriter.Workbook("Keywords.xlsx")
		worksheet = workbook.add_worksheet()
		heading_format = workbook.add_format()
		heading_format.set_bold()
		heading_format.set_font_color("blue")
		keyword_format = workbook.add_format({"bold":True,"font_color":"red"})
		worksheet.write(0,0,"Keyword",heading_format)
		worksheet.write(0,1,"Occurrences",heading_format)
		row = 1
		for key,value in keyworddict.items():
			worksheet.write(row,0,key,keyword_format)
			worksheet.write(row,1,value)
			row = row + 1
		chart = workbook.add_chart({"type":"column"})
		chart.add_series({"name":"Occurrences","categories":"=Sheet1!$A$2:$A$"+str(row),"values":"=Sheet1!$B$2:$B$"+str(row),"data_labels":{"value":True}})
		chart.set_x_axis({"name":"Keywords"})
		chart.set_y_axis({"name":"Occurrences"})
		worksheet.insert_chart("H1",chart)
		chart.set_legend({"position":"right"})
		chart.set_title({"name":"Keyword Occurrence Chart"})
		workbook.close()
		

from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3
import xlsxwriter

try:
	url = input("Enter a url: ")
	p1=seo(url)
	p1.totalnoofscripts()
	p1.displaylistofscript()
	p1.totalnumofwords()
	p1.keywordmeta()

finally:
	print("~"*120)
	print("The SEO tool has done with analysis ")
	print("	"*20,"THANK YOU")



