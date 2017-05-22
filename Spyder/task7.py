#coding=utf-8
import urllib
from bs4 import BeautifulSoup
import re
import datetime
import random

#设置一个页面集合
pages = set()
#
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj,internalUrl):
	global pages
	pattern = re.compile("^(/|.*"+internalUrl+")")
	internalLinks = []
	for link in bsObj.findAll("a",href=pattern):
		if link.attrs['href'] is not None:
			if link.attrs['href'] is not internalLinks:
				internalLinks.append(link.attrs['href'])
	return internalLinks


def getExternalLinks(bsObj,externalUrl):
	global pages
	pattern = re.compile("^(http|www)((?!"+externalUrl+").)*$")
	externalLinks = []
	for link in bsObj.findAll("a",href=pattern):
		if link.attrs['href'] is not None:
			if link.attrs['href'] is not externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def splitAddress(address):
	addressPart = address.replace("http://","").split("/")
	return addressPart


def getRandomExternalLink(startingPage):
	html = urllib.urlopen(startingPage)
	bsObj = BeautifulSoup(html,"html.parser")
	externalLinks = getExternalLinks(bsObj,splitAddress(startingPage)[0])
	if len(externalLinks) == 0:
		internalLinks = getInternalLinks(startingPage)
		return getExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])
	else:
		return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
	externalLink = getRandomExternalLink(startingSite)
	print "Random num is "+externalLink
	followExternalOnly(externalLink)


followExternalOnly("http://oreilly.com")


