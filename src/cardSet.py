import pandas as pd
import src.entity.rarityEntity as rEntity

class cardSet:
	def __init__(self, setName):
		self.setName = setName

		self.setData = pd.read_csv('dataSet/sets/'+self.setName+'.csv')

		r = rEntity.rarity()
		self.mythicCards = self.setData[self.setData['rarity'] == r.mythicRare]
		self.rareCards = self.setData[self.setData['rarity'] == r.rare]
		self.uncommonCards = self.setData[self.setData['rarity'] == r.uncommon]
		self.commonCards = self.setData[self.setData['rarity'] == r.common]

	def returnTotalCardsPerRarity(self):
		return [self.commonCards.shape[0], self.uncommonCards.shape[0], 
				self.rareCards.shape[0], self.mythicCards.shape[0]]

	def returnMedianCmcPerRarity(self):
		return [self.commonCards['cmc'].median(), self.uncommonCards['cmc'].median(), 
				self.rareCards['cmc'].median(), self.mythicCards['cmc'].median()]

	def returnCardListByRegex(self, columnFilter, checkRegex):
		return self.setData[self.setData[columnFilter].str.contains(checkRegex, na=False, regex=True)]

	def returnCardListByStringContaint(self, columnFilter,checkString):
		return self.setData[self.setData[columnFilter].str.contains(checkString, na=False)]

	#This should contain a list of possible filters based
	#And each column inside the cardEntity should be related to a possible filter
	def returnCardListBy(self,columnFilter, filterValue, showColumns=[]):
		return {
			'text': self.returnCardListByStringContaint(columnFilter.columnName, filterValue),
			'regex': self.returnCardListByRegex(columnFilter.columnName, filterValue)
		}.get(columnFilter.filterType, 'Filter type not found')
