from urllib import request
from os import environ
from urllib.parse import urljoin

apps = ['chord-search', 'weightmon']
app_url_template = 'http://{0}.herokuapp.com'
for a in apps:
	print('pinging', a)
	request.urlopen(app_url_template.format(a)).read()
	print('pinged', a)
