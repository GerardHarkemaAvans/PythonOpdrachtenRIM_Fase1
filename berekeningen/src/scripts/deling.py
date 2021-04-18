#! /usr/bin/env python

def deling(waarde1, waarde2):
	try:
		return waarde1/waarde2
	except:
		print "Deling door 0"
		exit()


if __name__ == '__main__':
	getal1 = input("Voer getal 1 in: ")
	getal2 = input("Voer getal 2 in: ")
	resultaat = deling(getal1, getal2)

	print "het resultaat van de deling van " + str(getal1) + " en " + str(getal2) + " is " + str(resultaat)



