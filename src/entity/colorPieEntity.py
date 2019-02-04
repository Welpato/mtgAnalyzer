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
	colorListObject = [ white, blue, black, red, green]
	colorListName = [ white.colorName, blue.colorName, black.colorName, red.colorName, green.colorName]
	colorListShort = [ white.colorShort, blue.colorShort, black.colorShort, red.colorShort, green.colorShort]
