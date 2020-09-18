import requests
from bs4 import BeautifulSoup

url = " "  #Enter the Url of the website which you want to scrap

# step 1: Get the html
r = requests.get(url)

html_content = r.content

# print(html_content)

# Step 2 : Parse the Html

soup = BeautifulSoup(html_content, "html.parser")

# print(soup)
# print(soup.prettify)
#
# for items in soup.stripped_strings:
#
#     print(items)

# Step 3: Tree Traversal

# title = soup.title
# print(title)
# print(title.string)
# print(type(title))
# print(type(soup))


# get paragraph
# para = soup.find_all('p')
# para =soup.find('p')
# para =soup.find('p')['class']
# print(soup.find('p').get_text())
# print(para)


# find all the elements with class name
# print(soup.find_all('p', class_ =" ")) # first agrument will be type of ele and second will be the class name.


# getting anchor tags
# anchor =soup.find_all('a')
# all_links =  set()
# print(anchor)

# get all the link in page
# for link in anchor:
#     if(link.get('href') != '#'):                 #This is used to not to print href with #
#         all_links.add( url + link.get('href'))
#
# print(all_links)


# navcontent = soup.find(id="")
# print(navcontent)
# print(navcontent.contents)  # it will give all the content of id and store it to memory
#  print(navcontent.childrens)  #  It will not save the content to memory
#   print(navcontent.parent)  #  It will give the parent of item
# print(navcontent.next_sibling)  #  It will give the next sibling of item
# print(navcontent.previous_sibling)  #  It will give the previous of item



# CSS Selectors

# print(soup.select(""))  #used to select css elements


