html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie<i>dada</i></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
b1 = soup.find_all('p')
for b11 in b1:
    a = b11.find('i', text=re.compile('d'))
    print (b11.string)
    print type(b11)
    print a
# print ('dada', type(b1))
# for tag in soup.find_all(re.compile("p")):
#     print(tag.attrs)
# print soup.string
