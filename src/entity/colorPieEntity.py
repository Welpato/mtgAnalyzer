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
