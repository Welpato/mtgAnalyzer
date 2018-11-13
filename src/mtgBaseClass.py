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

		for name in cardSetList:
			self.cardSetList.append(cs.cardSet(name))	

	def plotCardsTotal(self):
		r = rEntity.rarity()

		barCountList = []
		fillRight = 0
		count = 0
		for cardSet in self.cardSetList:
			
			plt.bar(r.rarityList, cardSet.returnTotalCardsPerRarity(),
					color=r.rarityColors)
			
			plt.title( cardSet.setName +
							' Total cards :' + str(cardSet.returnSetFile().shape[0]))
			
			if(fillRight == 1):			
				fillRight = 0
				count = count + 1
			else:
				fillRight = 1

			plt.show()


