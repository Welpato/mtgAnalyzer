class cardEntity:
	class cardColumn:
		def __init__(self, columnName, filterType = ''):
			self.columnName = columnName
			self.filterType = filterType

	name = cardColumn('name','text')
	multiverse_id = cardColumn('multiverse_id','')
	layout = cardColumn('layout','')
	names = cardColumn('names','text')
	mana_cost = cardColumn('mana_cost','')
	cmc	= cardColumn('cmc','')
	colors = cardColumn('colors','')
	color_identity = cardColumn('color_identity','')
	type = cardColumn('type','')
	supertypes = cardColumn('supertypes','')
	subtypes = cardColumn('subtypes','')
	rarity = cardColumn('rarity','text')
	text = cardColumn('text','text')
	flavor = cardColumn('flavor','text')
	artist = cardColumn('artist','text')
	number = cardColumn('number','')
	power = cardColumn('power','')
	toughness = cardColumn('toughness','')
	border = cardColumn('border','')
	life = cardColumn('life','')
	reserved = cardColumn('reserved','')
	release_date = cardColumn('release_date','')
	starter = cardColumn('starter','')
	rulings = cardColumn('rulings','')
	foreign_names = cardColumn('foreign_names','')
	printings = cardColumn('printings','')
	original_text = cardColumn('original_text','')
	original_type = cardColumn('original_type','')
	legalities = cardColumn('legalities','')
	source = cardColumn('source','')
	image_url = cardColumn('image_url','')
	set = cardColumn('set','')
	set_name = cardColumn('set_name','text')