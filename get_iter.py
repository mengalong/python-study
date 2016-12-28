#coding:utf8

import requests
from collections import Iterable, Iterator

class weather_iterator(Iterator):
	def __init__(self, cities):
		self.cities = cities
		self.index = 0

	def getWeather(self, city):
		r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
		data = r.json()['data']['forecast'][0]
		return '%s: %s, %s' % (city, data['low'], data['high'])

	def next(self):
		if self.index == len(self.cities):
			raise StopIteration
		city = self.cities[self.index]
		self.index += 1
		return self.getWeather(city)

class weather_iterable(Iterable):
	def __init__(self, cities):
		self.cities = cities

	def __iter__(self):
		return weather_iterator(self.cities)

for x in weather_iterable([u'北京', u'西安', u'上海', u'南京']):
	print x
