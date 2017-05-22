import urllib
from bs4 import BeautifulSoup
import re

pages = set()

def get_links(pageUrl):
	global pages
	pattern = re.compile("^(/wiki/)")

	html = urllib.urlopen("http://en.wikipedia.org"+pageUrl)
	bsOjb = BeautifulSoup(html,'html.parser')

	for link in bsOjb.findAll("a",href=pattern):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']
				print newPage
				pages.add(newPage)
				get_links(newPage)


get_links("")