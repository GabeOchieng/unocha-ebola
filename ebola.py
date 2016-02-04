#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import csv

html = requests.get('http://fts.unocha.org/pageloader.aspx?page=search-reporting_display&showDetails=1&CQ=cq271014010140PK7VJ9PbGG')
soup = BeautifulSoup(html.text, "html.parser")
table = soup.find('table', attrs={ "id" : "ctl11_dtgResults" })

rows = []
row = []
trs = table.find_all("tr")
for tr in trs:
	cells = tr.find_all("td")
	for cell in cells:
		value = cell.text
		if value == u'\xa0':
			value = value.replace(u'\xa0',u' ')
		row.append(value.encode('utf-8'))
	if row[1] != ' ':
		rows.append(row)
	row = []

with open("ebola.csv","wb") as file:
	writer = csv.writer(file)
	writer.writerows(rows)


