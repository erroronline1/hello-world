###############################################################################
# python version of the ruler image generator
# by error on line 1 (erroronline.one)
# you find the possible user inputs at the bottom of the document. these are
# preset but you can uncomment the input-commands. this is the main module for
# terminal-use only. here happens the important stuff.
#
# refactored as of 2018-08-16 to fit as importable module for gui application
# refactored as of 2018-08-21 to support background image and mostly pep8
###############################################################################

from PIL import Image, ImageDraw
import re
import math
from itertools import cycle
import sys

###############################################################################
# preparation of input values
###############################################################################

def ConvertColorInput(userinput):
	# returns either rgb or color name
    if userinput[0] == "#":
        chunk = int((len(userinput)-1)/3)
        try:
            rgb = [int(userinput[i:i+chunk], 16) for i in range(1, len(userinput), chunk)]
        except:
            print("c'mon. please enter serious values.")
            exit()
    else:
        rgb = [int(i) for i in re.split(r"\D+", userinput)]
    return tuple(rgb)

class inputs():
	# creates an object with user inputs
	# that is easier transferable to other objects and functions
	def __init__(self, **kwargs):
		self.x, self.y=int(kwargs["dim"][0]), int(kwargs["dim"][1])
		z = math.sqrt(self.y**2+self.x**2)
		scale = {"c":(z/kwargs["dia"]/2.54, (10, 5)),
				"i":(z/kwargs["dia"], (16, 8))}
		self.res = scale[kwargs["scaleto"]][0]
		self.unit = scale[kwargs["scaleto"]][1]
		self.width, self.height = self.x/self.res, self.y/self.res
		self.rotate="n"
	def update(self,**kwargs):
		self.fgcolor = ConvertColorInput(kwargs["fgcolor"])
		self.bgcolor = ConvertColorInput(kwargs["bgcolor"])
		self.bgimg = kwargs["bgimg"]
		try: self.bgalpha = float(kwargs["bgalpha"])
		except ValueError: self.bgalpha = 0
		try: self.reducefibo = int(kwargs["reducefibo"])
		except ValueError: self.reducefibo = 0
		try: self.fontsize = float(kwargs["fontsize"])
		except ValueError: self.fontsize = 10
		self.rotate = kwargs["rotate"]
		if "fileformat" in kwargs:
			self.fileformat = kwargs["fileformat"]
		else:
			self.fileformat = "jpg"

###############################################################################
# function and class to define output coordinates for all the elements
###############################################################################

def ruler(ui):
	# returns list of x/y coordinates for drawing a ruler on the left side
	# this is a function because the ruler is nothing magic. 
	line, coords, y1=0, [], 0
	while y1<ui.y:
		label = ""
		if not line%ui.unit[0]:
			x1=25
			label = str(line//ui.unit[0])
		elif not line%ui.unit[1]:
			x1 = 15
		else:
			x1 = 10
		coords.append([label, (0, int(y1), x1, int(y1))])
		y1 += ui.res/ui.unit[0]
		line += 1
	return coords[0:]

class fibonacci():
	# creates an object with properties for fibonacci-spiral containing
	# coordinates, maximum dimension, etc. 
	def __init__(self, ui):
		# find maximum fibonacci areas fitting to screen regardless of
		# direction in cm or inch
		a, b, self.fibonaccis = 0, 1, []
		while b<max(ui.width,ui.height):
			a, b = b, a+b
			self.fibonaccis.append(a)
		self.fibonaccis.pop() # last element is already bigger that screen
		self.xstart, self.ystart, self.width, self.height = 0, 0, 0, 0
		self.findstart(ui, False)

	def findstart(self, ui, max=False):
		#find center to start with and define width and height of structure
		if not max:
			max = len(self.fibonaccis)
		startingpoint = {"n":(1, 0, 1, 2),
						"y":(0, 0, 2, 3)} # rotate yes/no
		self.xstart = startingpoint[ui.rotate][0]
		self.ystart = startingpoint[ui.rotate][1]
		for xc in self.fibonaccis[startingpoint[ui.rotate][2]:max:4]:
			self.xstart += xc
		for yc in self.fibonaccis[startingpoint[ui.rotate][3]:max:4]:
			self.ystart += yc
		for xm in self.fibonaccis[startingpoint[ui.rotate][2]:max:2]:
			self.width += xm
		for ym in self.fibonaccis[startingpoint[ui.rotate][3]:max:2]:
			self.height += ym

	def create(self, ui, max=False):
		#returns a list of coordinates for drawing sqares in fibonacci manner
		if not max:
			max = len(self.fibonaccis)
		self.findstart(ui, max)
		#define pixel coordinates counterclockwise
		startingpoint = [(-1, 1, -1, 0, 180), (1, 1, 0, 1, 90),
						(1, -1, 1, 0, 0), (-1, -1, 0, -1, 270)]
		if ui.rotate == "n": # shift once
			startingpoint.append(startingpoint.pop(0))
		def directions(startingpoint):
			for i in cycle(startingpoint):
				yield i
		dir = directions(startingpoint)	
		self.areas = []
		x2, y2 = (ui.width-self.xstart)*ui.res-1, self.ystart*ui.res
		for a in self.fibonaccis[:max]:
			curdir = next(dir)
			go = a * ui.res
			#coordinates for squares
			x1, x2 = x2, x2 + go*curdir[0]
			y1, y2 = y2, y2 + go*curdir[1]
			#coordinates for double size rectangle according to pillow.draw.arc
			x3, x4 = x1 - go*curdir[2], x2 + go*curdir[3]
			y3, y4 = y1 - go*curdir[3], y2 - go*curdir[2]
			#swap values to upperleft/lower right because of pillow.draw.arc
			if curdir[4] == 0:
				y3, y4 = y4, y3
			elif curdir[4] == 180:
				x3, x4 = x4, x3
			elif curdir[4] == 270:
				x3, x4, y3, y4 = x4, x3, y4, y3
			#coordinates for center of degree scale
			x5, y5 = x2 - go*curdir[2], y2 - go*curdir[3]
			
			# (label, square coordinates, additional arc coordinates for use
			# with pillow, startdegrees)
			self.areas.append([str(a), (int(x1), int(y1), int(x2), int(y2)),
								(int(x3), int(y3), int(x4), int(y4)),
								(int(x5), int(y5)), curdir[4]])
		return self.areas

	def degrees(self, ui, area = False):
		# returns list of x/y coordinates for drawing a degree scale to
		# fibonacci spiral in given area + numbers
		# this is a function because like the ruler it is nothing magic. 
		if not area:
			area = self.areas[-1]
		else:
			area = self.areas[area-1]

		#degree scale depending on given area
		xc, yc, radius = area[3][0], area[3][1], int(area[0])*ui.res
		#convert from pillow value (starting at 3 o"clock clockwise)
		startdeg = 360 - area[4]
		coords = []
		for deg in range(startdeg-90, startdeg, 5):
			cosinus = math.cos(math.radians(deg))
			sinus = math.sin(math.radians(deg))
			label = ""
			if deg % 3:
				length = 10
			else:
				length = 25
				label = str(startdeg-deg)
			x1, y1 = xc + cosinus*(radius-length), yc - sinus*(radius-length)
			x2, y2 = xc + cosinus*radius, yc - sinus*radius
			coords.append([label, (int(x1), int(y1), int(x2), int(y2))])
		return coords[1:]

###############################################################################
# initiation and processing of coordinates for drawing them to image
###############################################################################

def draw_img(ui):
	img = Image.new("RGB", (ui.x, ui.y), ui.bgcolor)

	draw = ImageDraw.Draw(img)
	fibo = fibonacci(ui)

	for c in ruler(ui):
		draw.line((c[1]), fill=ui.fgcolor)
		if c[0] != "":
			draw.text((c[1][2] + ui.fontsize*.5, c[1][3] - ui.fontsize*.5),
						c[0], fill=ui.fgcolor)

	for c in fibo.create(ui, len(fibo.fibonaccis)-ui.reducefibo):
		draw.rectangle(c[1], fill=None, outline=ui.fgcolor)
		xlabel = c[1][0] + (c[1][2]-c[1][0]) / 2
		ylabel = c[1][1] + (c[1][3]-c[1][1]) / 2
		draw.text((xlabel, ylabel), c[0], fill=ui.fgcolor)
		draw.arc(c[2], c[4], c[4] + 90, fill=ui.fgcolor)
		
	def drawdegree(square, ui):
		for c in square:
			draw.line(c[1], fill=ui.fgcolor)
			if c[0] != "":
				draw.text((c[1][0] + ui.fontsize*.5,
							c[1][1] - ui.fontsize*.5),
							c[0], fill=ui.fgcolor)

	drawdegree(fibo.degrees(ui), ui)
		
	if ui.bgimg:
		#print(ui.bgimg)
		try:
			bg = Image.open(ui.bgimg)
			ui_ratio = ui.x / ui.y
			if ui.x / ui.y >= bg.width / bg.height:
				#print("i"ll take the we borders" )
				cropamount = bg.height-bg.width/ui_ratio
				x1, y1 = 0, cropamount//2
				x2, y2 = bg.width, bg.height-cropamount//2
			else:
				#print("i"ll take the ns borders" )
				cropamount = bg.width-bg.height*ui_ratio
				x1, y1 = cropamount//2, 0
				x2, y2 = bg.width-cropamount//2, bg.height
			
			bg = bg.transform((ui.x, ui.y), Image.QUAD,
							(x1,y1,x1,y2,x2,y2,x2,y1)).convert("RGB")
			img = Image.blend(img, bg, ui.bgalpha)
		except FileNotFoundError:
			print("could not open background image file %s..."%(ui.bgimg))


	del draw 
	try: img.save("ruler." + ui.fileformat)
	except: print('nope')
	return True

###############################################################################
# user input and output settings, preparations and recommendations
###############################################################################

if __name__ == "__main__":
	print("this creates an image with ruler, areas, circles, degrees")
	print("type the screen dimensions...")
	# e.g. 720x1280 4.6" for xperia z5 compact
	# or 3200x1800 13.3" for lenovo yoga 2 pro 13
	dim,dia=[720,1280], 4.6 
	#dim,dia=[3200,1800], 13.3 #re.split(r"\D+",input("type screen pixel resolution (width/height): ")), float(input("type screen size in inch: "))
	print("type in desired scale... ")
	scaleto="c" #input("[c]m or [i]nch? ")

	ui=inputs(dim=dim,dia=dia,scaleto=scaleto)

	fibo=fibonacci(ui)
	reducefibo=0
	if fibo.width>ui.width or fibo.height>ui.height:
		print("the maximum amount of fibonacci squares is %d. it is recommended\
to rotate it by 90°. or you can reduce the number of squares."%len(fibo.fibonaccis))
		reducefibo=0 #int(input("reduce by 0, 1, 2, etc. or select rotation in next step: "))

	print("set direction of fibonacci areas... ")
	rotate="n" #input("rotate clockwise by 90 degrees [y]es / [n]o? ")

	print("type in colors as webcolors (#aabbcc) or rgb (126, 29, 254)... ")
	bgcol, fgcol="#000000","#ffffff" #input("type in background color: "), input("type in foreground color: ")

	print("specify background image (in same folder). image might be cropped... ")
	bgalpha, bgimg=0.8, "pythonlogo.png" #float(input("0.0 to 1.0 value for merging intensity: ")), input("filename or just [enter] to skip: ")

	#print("set font size... ")
	fontsize=18 #int(input("type in font-size in pixel: "))

	print("specify image format. recommendation: [png] for less colors, [jpg] \
for more colors (e.g. with use of background image)... ")
	fileformat="jpg" #input("enter format: "))


	ui.update(reducefibo=reducefibo, rotate=rotate, fgcolor=fgcol,
				bgcolor=bgcol, bgalpha=bgalpha, bgimg=bgimg, fontsize=fontsize,
				fileformat=fileformat)	
	
	if draw_img(ui):
		print("image ruler.%s saved"%(fileformat))
	else:
		print("image could not be saved")
	