import copy
import csv
import re
import pandas as pd
import numpy
import matplotlib.pyplot as plt

import src.cardSet as cs
import src.entity.rarityEntity as rEntity

from IPython.display import display, HTML

plt.rcParams['figure.figsize'] = (60,150)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)

class mtgBase:

	def __init__(self, cardSetList = []):
		self.cardSetList = []
		self.rarity = rEntity.rarity()

		if(cardSetList == []):
			with open('dataSet/allSets.csv', 'r', encoding='utf-8') as setsFile:
				reader = csv.DictReader(setsFile)
				setsFile.seek(0)
				for row in reader:  
					setName = re.sub(r'[\\/:"*?<>|]+', '', row['name'])
					self.cardSetList.append(cs.cardSet(setName))

		else:
			for name in cardSetList:
				self.cardSetList.append(cs.cardSet(name))


	#Plot the total of cards of each set
	def plotCardsTotal(self):
		for cardSet in self.cardSetList:
			
			plt.bar(self.rarity.rarityList, cardSet.returnTotalCardsPerRarity(),
					color=self.rarity.rarityColors)
			
			plt.title( cardSet.setName +
							' Total cards :' + str(cardSet.setFile.shape[0]))

			plt.show()

	#Plot the median CMC per rarity of each set
	def plotMedianCmc(self):
		for cardSet in self.cardSetList:
			
			plt.bar(self.rarity.rarityList, cardSet.returnMedianCmcPerRarity(),
					color=self.rarity.rarityColors)
			
			plt.title( cardSet.setName +
							' Median CMC :' + str(cardSet.setFile['cmc'].median()))

			plt.show()

	#Plot all the cards in the set with the given string in the name
	def plotCardsNameWith(self, checkString):
		for cardSet in self.cardSetList:
			print(cardSet.setName)
			displayList = cardSet.returnCardListByNameWith(checkString)
			if not displayList.empty:
				display(displayList)

	#Plot all the cards in the set with the given color identity
	def plotCardsWithColorIdentity(self, colorIdentity):
		for cardSet in self.cardSetList:
			print(cardSet.setName)
			display(cardSet.returnCardListByColorIdentity(colorIdentity))


	def plotListBy(self, columnFilter, filterValue):
		for cardSet in self.cardSetList:
			print(cardSet.setName)
			displayList = cardSet.returnCardListBy(columnFilter,filterValue)
			#if not displayList.empty:
			display(displayList)

