#!usr/bin/python
#coding: utf-8

import random, datetime

fornarlomb = [	"Alexander Gunnarsson",
				"Ari Freyr Ásgeirsson",
				"Ásta Björk Halldórsdóttir",
				"Björn Ingi Björnsson",
				"Daníel Brynjólfsson",
				"Davíð Bachmann Jóhannesson",
				"Davíð Kári Kárason",
				"Garðar Gíslason",
				"Gísli Rúnar Gíslason",
				"Hinrik Þór Ágústsson",
				"Hjördís Hera Hauksdóttir",
				"Jóhann Björn Gulin",
				"Jón Björn Árnason",
				"Kári Gunnarsson",
				"Marteinn Guðberg Þorláksson",
				"Pálmar Gíslason",
				"Sigurður Bjarki Haraldsson",
				"Sigursteinn Bjarni",
				"Sveinn Darri Ingólfsson",
				"Unnur Gígja Ingimundardóttir",
				"Valdís Ösp Gísladóttir",
				"Vilhjálmur Heimir Baldursson",
				"Ævar Ísak Ástþórsson"]

random.shuffle(fornarlomb)
startdate = datetime.date(2013, 10, 4)
dateincr =  datetime.timedelta(days=7)


for item in fornarlomb:
	print ("{0} er {1}".format(item, startdate.strftime('%d-%m-%Y')))
	startdate += dateincr