import requests
import bs4

res = requests.get('http://quotes.toscrape.com')
soup = bs4.BeautifulSoup(res.text, 'lxml')

# printing the author of quotes in the page
for n in range(1, 10):
    quotes = soup.select('.author')[n].getText()
    print(quotes)

print("\n")

# printing all the tags in the page
tags = soup.select('.col-md-4.tags-box')[0].getText()
print(tags)


# printing the unique author in each page
page_url ='http://quotes.toscrape.com/page/{}'

authors = set()

for page in range(1, 10):
    url = page_url.format(page)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    for name in soup.select('.author'):
        authors.add(name.text)
        print(authors)

'''
usage of soup.select() in CSS code

1-selecting an element tag and identifying which one in [] brackets
soup.select('div')[0]
soup.select('title')[0]
soup.select('h1')[0]
soup.select('p')[0]

2-selecting element's id 
soup.select('#some_id')

3-selecting an element's class
soup.select('.some_class')

4.select an element's span
soup.select('div.span')

5-select an element's span within a div element, with nothing in between
soup.select('div > span')
'''
