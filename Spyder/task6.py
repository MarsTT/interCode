import urllib
from bs4 import BeautifulSoup
import re


pages = set()

def get_link(page_url):

	global pages

	pattern = re.compile("^(/wiki/)")

	html = urllib.urlopen("http://en.wikipedia.org"+page_url)
	bsObj = BeautifulSoup(html)

	try:
		print bsObj.h1.get_text()
		print bsObj.find(id="mw-content-text").findAll("p")[0]
		print bsObj.find(id="ca-edit")
	except AttributeError:
		print "not found!"

	for link in bsObj.findAll("a",href=pattern):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']
				print "=============\n"+newPage
				pages.add(newPage)
				get_link(newPage)

get_link("")