"""
Omat Gonzalez 
web scraper python project 
"""
import urllib.request
from bs4 import BeautifulSoup

class Scraper:
	"""
	Object Scraper takes in a website to scrape from as a parameter
	for example : "https://news.google.com/"
	"""
	def __init__(self,site):
		self.site=site

	def scrape(self):
		#urlopen() makes request to a website and returns response onjext that has its HTML stored in it
		r = urllib.request.urlopen(self.site) 
		#read() returns the HTML from the reponse object r. 
		html = r.read()
		parser = "html.parser"
		#BeautifulSoup object does the heavy lifting and parse the HTML passed 
		sp = BeautifulSoup(html, parser)
		"""
		This for loop will call the method find_all on BeautifulSoup object.
		Passing in "a" as a parameter which will tell the function to look fo <a></a> tags and the method will return all of the URLS the webstie 
		links to in the HTML you downloaded 
		-find_all method: returns iterable containing tag objects found. we just want the Href in the tag not the other elements
		"""
		for tag in sp.find_all("a"): 
			url=tag.get("href")
			if url is None:
				continue
			if "html" in url:
				print ("\n" + url)

news = "https://news.google.com/"
Scraper(news).scrape()
