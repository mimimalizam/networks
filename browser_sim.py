import urllib as request_library
from bs4 import BeautifulSoup

response_html = request_library.urlopen("https://news.ycombinator.com/")
parsed_html = BeautifulSoup(response_html)

tags = parsed_html('a')

for tag in tags:
    print tag["href"]
