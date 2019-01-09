class regex:
	#Return a regex that checks if the informed value exists in the column
	#TODO:Check how to do a "AND" on the regex in place o the "OR" = "|"
	def regexValueExists(self, valueToCheck, capsuleOpen = "'", capsuleClose = "'"):

		colorIdentity = ""
		moreThenOne = False
		for value in valueToCheck:
			if moreThenOne == True:
				colorIdentity = colorIdentity + "|"
			colorIdentity = colorIdentity + capsuleOpen + value + capsuleClose
			moreThenOne = True

		return colorIdentity

	#Return a regex that checks if the informed value repeat in the column
	def regexValueRepeat(self, valueToCheck, minimalRepeat, capsuleOpen = "'", capsuleClose = "'"):
		regex = ""
		moreThenOne = False

		for value in valueToCheck:
			if moreThenOne == True:
				regex = regex + "|"
			regex = regex + "(" + capsuleOpen + value + capsuleClose + ")"
			moreThenOne = True

		if moreThenOne == True:
			regex = regex + "{" + str(minimalRepeat) + ",}"

		return regex

