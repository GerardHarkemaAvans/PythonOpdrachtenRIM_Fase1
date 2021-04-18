#! /usr/bin/env python

if __name__ == '__main__':
	print "Programma voor het berekenen van het gemiddelde"
	laatsteGetal = 0;
	getallen = []
	while(laatsteGetal != -1):
		laatsteGetal = input("Voer getal "+str(len(getallen) + 1) + " in: ")
		if (laatsteGetal != -1):
			getallen.append(laatsteGetal)

	totaal = 0
	for getal in getallen:
		totaal = totaal + getal

	print "Er zijn " + str(len(getallen)) + " getallen ingevoerd"
	print "het gemiddelde van deze getallen is: " + str(totaal/len(getallen))


