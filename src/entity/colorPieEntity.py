class colorPie:
	class color:
		def __init__(self, colorName, colorShort):
			self.colorName = colorName
			self.colorShort = colorShort

	white = color('White','W')
	blue = color('Blue', 'U')
	black = color('Black', 'B')
	red = color('Red', 'R')
	green = color('Green', 'G')
	colorList = [ white, blue, black, red, green]

	#Return a regex that checks if the colors informed exists in the column
	#TODO:Check how to do a "AND" on the regex in place o the "OR" = "|"
	def regexExistsColor(self, colorsToCheck, capsuleOpen = "'", capsuleClose = "'"):

		colorIdentity = ""
		moreThenOne = False
		for color in colorsToCheck:
			if moreThenOne == True:
				colorIdentity = colorIdentity + "|"
			colorIdentity = colorIdentity + capsuleOpen + color.colorShort + capsuleClose
			moreThenOne = True

		return colorIdentity

	#Return a regex that checks if the informed colors repeat in the column
	def regexColorRepeat(self, colorsToCheck, minimalRepeat, capsuleOpen = "'", capsuleClose = "'"):
		regex = ""
		moreThenOne = False

		for color in colorsToCheck:
			if moreThenOne == True:
				regex = regex + "|"
			regex = regex + "(" + capsuleOpen + color.colorShort + capsuleClose + ")"
			moreThenOne = True

		if moreThenOne == True:
			regex = regex + "{" + str(minimalRepeat) + ",}"

		return regex

