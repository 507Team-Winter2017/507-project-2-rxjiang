#proj2.py


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.nytimes.com'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all("h2", class_= "story-heading")
count = 0
for story_heading in title:
	if count < 10:
	    if story_heading.a: 
	        print(story_heading.a.text.replace("\n", " ").strip())
	        count = count + 1
	    else: 
	        print(story_heading.contents[0].strip())
	        count = count + 1



#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.michigandaily.com'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

most_read = soup.find_all("div", class_= "view view-most-read view-id-most_read view-display-id-panel_pane_1 view-dom-id-99658157999dd0ac5aa62c2b284dd266")
for story_heading in most_read:
	print(story_heading.get_text())



#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://newmantaylor.com/gallery.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

image = soup.find_all("img")
for img in image:
	alt = img.get('alt', '')
	if alt != '':
		print(alt)
	else:
		print('No alternative text provided!!')


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
count = 1

def email_dict(url, count):
	req = urllib.request.Request(url, None, {'User-Agent': 'SI_CLASS'})
	html = urllib.request.urlopen(req, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	contact_url = soup.find_all("div", class_= "field field-name-contact-details field-type-ds field-label-hidden")
	for url in contact_url:
		node = url.find("a")
		link = "https://www.si.umich.edu" + node.get('href', None)
		req1 = urllib.request.Request(link, None, {'User-Agent': 'SI_CLASS'})
		html_link = urllib.request.urlopen(req1, context=ctx).read()
		soup_link = BeautifulSoup(html_link, 'html.parser')
		emails = soup_link.find("div", class_= "field field-name-field-person-email field-type-email field-label-inline clearfix").find_all("div", class_="field-item even")
		for email in emails:
			if email.a: 
				print(str(count) + " " + email.a.text.replace("\n", " ").strip())
				count = count + 1
			else: 
				print(str(count) + " " + email.contents[0].strip())
				count = count + 1
	next_page = soup.find("a", title = "Go to next page")
	if next_page != None:
		next_page_link = 'https://www.si.umich.edu' + next_page.get('href', None)
		email_dict(next_page_link, count)

email_dict(url, count)