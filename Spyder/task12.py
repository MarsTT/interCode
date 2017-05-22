#coding=utf-8

import urllib
from bs4 import BeautifulSoup
import re
import string
import operator
import os
import pymysql



conn = pymysql.connect(host='127.0.0.1',user='root',passwd='lovol12345',charset='utf8')

cur = conn.cursor()
cur.execute('USE NGrams')


def insert_data(grams,count):
	cur.execute("select * from 2_grams where grams=%s",(grams))
	if cur.rowcount == 0:
		cur.execute("insert into 2_grams (grams,count) values (%s,%s)",(grams,int(count)))
		conn.commit()
	else:
		cur.fetchone()[0]




def cleanInput(input):
	#将换行符换成空格，并且都变成小写
	input = re.sub("\n+"," ",input).lower()
	#将[0-9]换成""
	input = re.sub("\[[0-9]*\]","",input)
	#将一连串空格换成空格
	input = re.sub(" +"," ",input)
	#将数据生成字节文件
	input = bytes(input)
	#将输入转成"ascii"编码
	input = input.decode("ascii","ignore")
	cleanInput = []
	#用空格号进行分隔
	input = input.split(' ')
	for item in input:
		#去掉所有标点符号
		item = item.strip(string.punctuation)
		if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
			cleanInput.append(item)
	return cleanInput


def ngrams(input,n):
	input = cleanInput(input)
	output = {}
	for i in range(len(input)- n + 1):
		ngramsTemp = " ".join(input[i:i+n])
		if ngramsTemp not in output:
			output[ngramsTemp] = 0
		output[ngramsTemp] += 1
	return output

url = "http://pythonscraping.com/files/inaugurationSpeech.txt"
html = urllib.urlopen(url)
content = html.read()
#content = str(urllib.urlopen().read())
# file = open(os.path.join(os.getcwd(),'origin_data.txt'),'w')
# file.write(content)
# file.close()

with open(os.path.join(os.getcwd(),'origin_data.txt'),'w') as file:
	file.write(content)


ngrams = ngrams(content,2)

storedNGrams = sorted(ngrams.items(),key = operator.itemgetter(1),reverse = True)

for gram in storedNGrams:
	insert_data(gram[0],gram[1])


#print type(storedNGrams[0])



cur.close()
conn.close()