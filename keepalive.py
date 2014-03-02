from urllib import request
from os import environ
from urllib.parse import urljoin
from urllib.error import HTTPError

apps = ['weightmon', 'augmented-rss']
app_url_template = 'http://{0}.herokuapp.com'
for a in apps:
	print('pinging', a)
	try:
		request.urlopen(app_url_template.format(a)).read()
	except HTTPError as err:
		print('got error', err)
	print('pinged', a)
