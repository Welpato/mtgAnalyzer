import copy
import csv
import re
import pandas as pd
import numpy
import matplotlib.pyplot as plt

import src.cardSet as cs
import src.entity.rarityEntity as rEntity
import src.entity.cardEntity as cEntity
import src.entity.colorPieEntity as colorEntity

from IPython.display import display, HTML

plt.rcParams['figure.figsize'] = (60,150)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)

class mtgBase:

	def __init__(self, cardSetList = []):
		self.cardSetList = []
		self.rarity = rEntity.rarity()
		self.card = cEntity.card()
		self.colorPie = colorEntity.colorPie()

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
	def plotCardsTotal(self, cardSetList):
		for cardSet in cardSetList:
			
			plt.bar(self.rarity.rarityList, cardSet.returnTotalCardsPerRarity(),
					color=self.rarity.rarityColors)
			
			plt.title( cardSet.setName +
							' Total cards :' + str(cardSet.setData.shape[0]))

			plt.show()

	#Plot the median CMC per rarity of each set
	def plotMedianCmc(self, cardSetList):
		for cardSet in cardSetList:
			
			plt.bar(self.rarity.rarityList, cardSet.returnMedianCmcPerRarity(),
					color=self.rarity.rarityColors)
			
			plt.title( cardSet.setName +
							' Median CMC :' + str(cardSet.setData['cmc'].median()))

			plt.show()

	#Apply an filter to the cardSetList informed and returns the filtred list
	def filterCardSetListBy(self, originCardSetList, columnFilter, filterValue):
		returnList = []
		cardSetList = copy.deepcopy(originCardSetList)
		for cardSet in cardSetList:
			cardSet.setData = cardSet.returnCardListBy(columnFilter,filterValue)
			returnList.append(cardSet)

		return returnList

	#Plot a filtred set list
	def plotCardSetList(self,cardSetList):
		for cardSet in cardSetList:
			print(cardSet.setName)
			display(cardSet.setData)


