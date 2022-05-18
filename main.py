import requests
from bs4 import BeautifulSoup

# gets the content of the website
url = "https://codewithharry.com"
r = requests.get(url)
htmlContent = r.content

# beautifies the content and gives it a tree like structure:
soup = BeautifulSoup(htmlContent, 'html.parser') 

# print the html content with proper indentations and formatting:
# print(soup.prettify)


title = soup.title
paras = soup.find_all('p')
anchors = soup.find_all('a')

# get first element: 
first_para = soup.find('p')

#get text in first para:
first_para_text = first_para.get_text()

# get class of first element: 
first_para_classes = soup.find('p')['class']

# get id of first element (the first para doesn't have an id) : 
# first_para_id = soup.find('p')['id']

# find all elements with class lead:
para_class_lead = soup.find_all('p',class_="lead")

# get text from a element: 
first_para_text = soup.find("p").get_text()

# get all links on the page:
all_links = set()
for link in anchors:
    linkText = url + link.get('href') # we add url at the start because all the links in the page are relative
    all_links.add(linkText)