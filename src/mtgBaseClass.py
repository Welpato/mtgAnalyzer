import scipy
import copy
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

	def __init__(self, cardSetList):
		self.cardSetList = []
		self.rarity = rEntity.rarity()

		for name in cardSetList:
			self.cardSetList.append(cs.cardSet(name))	

	#Plot the total of cards of each set
	def plotCardsTotal(self):
		for cardSet in self.cardSetList:
			
			plt.bar(self.rarity.rarityList, cardSet.returnTotalCardsPerRarity(),
					color=self.rarity.rarityColors)
			
			plt.title( cardSet.setName +
							' Total cards :' + str(cardSet.returnSetFile().shape[0]))

			plt.show()

	#Plot the median CMC per rarity of each set
	def plotMedianCmc(self):
		for cardSet in self.cardSetList:
			
			plt.bar(self.rarity.rarityList, cardSet.returnMedianCmcPerRarity(),
					color=self.rarity.rarityColors)
			
			plt.title( cardSet.setName +
							' Median CMC :' + str(cardSet.returnSetFile()['cmc'].median()))

			plt.show()

	#Plot all the cards in the set with the given string in the name
	def plotCardsNameWith(self, checkString):
		for cardSet in self.cardSetList:
			display(cardSet.returnCardListByNameWith(checkString))

	#Plot all the cards in the set with the given color identity
	def plotCardsWithColorIdentity(self, colorIdentity):
		for cardSet in self.cardSetList:
			display(cardSet.returnCardListByColorIdentity(colorIdentity))