import pandas as pd
import src.entity.rarityEntity as rEntity
import src.entity.colorPieEntity as colorPie

class cardSet:
	def __init__(self, setName):
		self.setName = setName

		self.setFile = pd.read_csv('dataSet/sets/'+self.setName+'.csv')

		r = rEntity.rarity()
		self.mythicCards = self.setFile[self.setFile['rarity'] == r.mythicRare]
		self.rareCards = self.setFile[self.setFile['rarity'] == r.rare]
		self.uncommonCards = self.setFile[self.setFile['rarity'] == r.uncommon]
		self.commonCards = self.setFile[self.setFile['rarity'] == r.common]

	def returnTotalCardsPerRarity(self):
		return [self.commonCards.shape[0], self.uncommonCards.shape[0], 
				self.rareCards.shape[0], self.mythicCards.shape[0]]

	def returnMedianCmcPerRarity(self):
		return [self.commonCards['cmc'].median(), self.uncommonCards['cmc'].median(), 
				self.rareCards['cmc'].median(), self.mythicCards['cmc'].median()]

	def returnCardListByColorIdentity(self, colorIdentity):
		return self.setFile[self.setFile['color_identity'] == colorIdentity]

	def returnCardListByStringContaint(self, columnFilter,checkString):
		return self.setFile[self.setFile[columnFilter].str.contains(checkString)]

	#This should contain a list of possible filters based
	#And each column inside the cardEntity should be related to a possible filter
	def returnCardListBy(self,columnFilter, filterValue, showColumns=[]):
		filterType = 'text'
		return {
			'text': self.returnCardListByStringContaint(columnFilter, filterValue),
		}[filterType]

		return fList
