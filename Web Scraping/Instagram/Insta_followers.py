import requests
from bs4 import BeautifulSoup

post = input("Enter the instagram account for which you want to find the number of followers:\n")
post_page = requests.get(post)
#print(post_page.content)

s_post = BeautifulSoup(post_page.content, 'html.parser')
print(s_post.prettify())
print(s_post.find_all('a'))
