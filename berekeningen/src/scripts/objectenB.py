#! /usr/bin/env python

from math import pi

class Rekenmethodes:
	def __init__(self, waarde1, waarde2):
		self.waarde1 = waarde1
		self.waarde2 = waarde2

	def optellen(self):
		return self.waarde1 + self.waarde2

	def aftrekken(self):
		return self.waarde1 - self.waarde2

	def vermenigvuldigen(self):
		return self.waarde1 * self.waarde2

	def delen(self):
		try:
			return self.waarde1/self.waarde2
		except:
			print "Deling door 0 !!!"
			return 0
	def pi(self):
		return pi


if __name__ == '__main__':


	getal1 = input("Voer getal 1 in: ")
	getal2 = input("Voer getal 2 in: ")

	berekening = Rekenmethodes(getal1, getal2)

	print "Het resultaat van de optelling van " + str(getal1) + " en " + str(getal2) + " is " + str(berekening.optellen())
	print "Het resultaat van de aftrekking van " + str(getal1) + " en " + str(getal2) + " is " + str(berekening.aftrekken())
	print "Het resultaat van de vermenigvuldiging van " + str(getal1) + " en " + str(getal2) + " is " + str(berekening.vermenigvuldigen())
	print "Het resultaat van de deling van " + str(getal1) + " en " + str(getal2) + " is " + str(berekening.delen())
	print "Het getal pi is " + str(berekening.pi())



