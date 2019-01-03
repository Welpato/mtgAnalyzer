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

	#Return a regex that is used to filter by color identity
	#TODO:Check how to do a equal function but to colorName
	#TODO:Check how to do a "AND" on the regex in place o the "OR" = "|"
	def returnColorIdentity(self, white = False, blue = False, 
		black = False, red = False, green = False):

		colorIdentity = ""
		moreThenOne = False
		
		if white == True:
			colorIdentity = colorIdentity + "'" + self.white.colorShort + "'"
			moreThenOne = True

		if blue == True:
			if moreThenOne == True:
				colorIdentity = colorIdentity + "|"
			colorIdentity = colorIdentity + "'" + self.blue.colorShort + "'"
			moreThenOne = True

		if black == True:
			if moreThenOne == True:
				colorIdentity = colorIdentity + "|"
			colorIdentity = colorIdentity + "'" + self.black.colorShort + "'"
			moreThenOne = True

		if red == True:
			if moreThenOne == True:
				colorIdentity = colorIdentity + "|"
			colorIdentity = colorIdentity + "'" + self.red.colorShort + "'"
			moreThenOne = True

		if green == True:
			if moreThenOne == True:
				colorIdentity = colorIdentity + "|"
			colorIdentity = colorIdentity + "'" + self.green.colorShort + "'"

		return colorIdentity

	def regexCostColorRepeat(self, colorsToCheck, minimalRepeat):
		regex = ""
		moreThenOne = False

		for color in colorsToCheck:
			if moreThenOne == True:
				regex = regex + "|"
			regex = regex + "(\{" + color + "\})"
			moreThenOne = True

		if moreThenOne == True:
			regex = regex + "{2,}"

		return regex

