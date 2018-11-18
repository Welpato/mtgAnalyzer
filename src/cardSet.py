import pandas as pd
import src.entity.rarityEntity as rEntity

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

	def returnCardListByNameWith(self, checkString):
		return self.setFile[self.setFile['name'].str.contains(checkString)]

	def returnMythicCards(self):
		return self.mythicCards

	def returnRareCards(self):
		return self.rareCards

	def returnUncommonCards(self):
		return self.uncommonCards

	def returnCommonCards(self):
		return self.commonCards

	def returnSetFile(self):
		return self.setFile
