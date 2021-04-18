#! /usr/bin/env python

from math import pi

class Rekenmethodes:

	def optellen(self, waarde1, waarde2):
		return waarde1 + waarde2

	def aftrekken(self, waarde1, waarde2):
		return waarde1 - waarde2

	def vermenigvuldigen(self, waarde1, waarde2):
		return waarde1 * waarde2

	def delen(self, waarde1, waarde2):
		try:
			return waarde1/waarde2
		except:
			print "Deling door 0 !!!"
			return 0
	def pi(self):
		return pi


if __name__ == '__main__':

	berekening = Rekenmethodes()

	getal1 = input("Voer getal 1 in: ")
	getal2 = input("Voer getal 2 in: ")

	print "Het resultaat van de optelling van " + str(getal1) + " en " + str(getal2) + " is " + str(berekening.optellen(getal1, getal2))
	print "Het resultaat van de aftrekking van " + str(getal1) + " en " + str(getal2) + " is " + str(berekening.aftrekken(getal1, getal2))
	print "Het resultaat van de vermenigvuldiging van " + str(getal1) + " en " + str(getal2) + " is " + str(berekening.vermenigvuldigen(getal1, getal2))
	print "Het resultaat van de deling van " + str(getal1) + " en " + str(getal2) + " is " + str(berekening.delen(getal1, getal2))
	print "Het getal pi is " + str(berekening.pi())



