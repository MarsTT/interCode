#coding=utf-8

'''
	找到某一路径下的文件夹，返回该文件夹下的所有文件，
	如果存在子文件夹，将子文件夹的文件再次返回
'''
import os

def find_foler(folder_url):
	for file in os.listdir(folder_url):
		file_url = os.path.join(folder_url,file)
		if os.path.isdir(file_url):
			find_foler(file_url)
		print file_url

find_foler("/Users/marxia/Desktop/interCode")
