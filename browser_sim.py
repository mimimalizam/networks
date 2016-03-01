import urllib as request_library

response = request_library.urlopen("https://news.ycombinator.com/")

for line in response:
    print line.strip()
