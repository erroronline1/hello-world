###############################################################################
# python version of the ruler image generator
# by error on line 1 (erroronline.one)
# this is the gui-version fully dependable of the original ruler.py
#
# the actual app extends the all purpose scrolling canvas class
# therefore values of input fields can be handled within the runtime
#
# TODO: ttk styling
###############################################################################

import tkinter as tk
from tkinter import ttk
import re
import ruler
import os
import universal_app_canvas

###############################################################################
# actual application
###############################################################################

class pages(universal_app_canvas.Container):
	def __init__(self, title="TitleNotFoundException ;)", geometry=(640, 480)):
		super().__init__(title, geometry)

		#self.menubar.add_command(label="Hello2") # add new submenu
		#self.filemenu.insert_command(1, label="next") # add new menu item

		info = ttk.Label(self.content,
				text="make your screen a measuring tool")
		self.add(info, None, 3)

		dim_info = ttk.Label(self.content,
				text="enter your screens resolution (width x height)")
		self.add(dim_info)
		self.dim = ttk.Entry(self.content)
		self.add(self.dim, (1, -1), 2)

		dia_info = ttk.Label(self.content,
				text="enter your screens diameter in inch")
		self.add(dia_info)
		self.dia = ttk.Entry(self.content)
		self.add(self.dia, (1, -1), 2)

		scaleto_info = ttk.Label(self.content,
				text="select desired unit")
		self.add(scaleto_info)
		self.scaleto = tk.StringVar()
		self.scaleto.set("c")
		self.scaleto0 = ttk.Radiobutton(self.content,
				text="cm", variable=self.scaleto, value="c")
		self.add(self.scaleto0, (1, -1))
		self.scaleto1 = ttk.Radiobutton(self.content,
				text="inch", variable=self.scaleto, value="i")
		self.add(self.scaleto1, (2, -1))
		
		default0 = ttk.Button(self.content,
				text="xperia z5 compact metric",
				command=lambda: self.setdefault0("720x1280", "4.6"))
		self.add(default0)
		default1 = ttk.Button(self.content,
				text="yoga 2 pro 13 metric",
				command=lambda: self.setdefault0("3200x1800", "13.3"))
		self.add(default1, (1, -1))
		default2 = ttk.Button(self.content,
				text="clear", command=self.setdefault0)
		self.add(default2, (2, -1))

		step1 = ttk.Button(self.content,
				text="proceed...", command=self.step1)
		self.add(step1)

		self.recommendation_info = ttk.Label(self.content,
				text="nothing set yet...")
		self.add(self.recommendation_info, None, 3)

		reduce_info = ttk.Label(self.content,
				text="reduce by x squares")
		self.add(reduce_info)
		self.reducefibo = tk.StringVar()
		self.reducefibo.set("0")
		option = tuple("0")
		self.reduce = ttk.OptionMenu(self.content,
				self.reducefibo, "choose value", *option)
		self.add(self.reduce, (1, -1), 2)

		rotation_info = ttk.Label(self.content,
				text="rotate")
		self.add(rotation_info)
		self.rotate = tk.StringVar()
		self.rotate.set("n")
		rotation = ttk.Checkbutton(self.content,
				text="by 90°", variable=self.rotate,
				onvalue="y", offvalue="n")
		self.add(rotation, (1, -1), 2)

		foregroundcolor_info = ttk.Label(self.content,
				text="foreground color (webcolor or rgb)")
		self.add(foregroundcolor_info)
		self.foregroundcolor = ttk.Entry(self.content)
		self.add(self.foregroundcolor, (1, -1), 2)

		backgroundcolor_info = ttk.Label(self.content,
				text="background color (webcolor or rgb)")
		self.add(backgroundcolor_info)
		self.backgroundcolor=ttk.Entry(self.content)
		self.add(self.backgroundcolor, (1, -1), 2)

		backgroundimg_info = ttk.Label(self.content,
				text="background image (in same folder)")
		self.add(backgroundimg_info)
		self.backgroundimg = tk.StringVar()
		files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
		files2 = []
		supported_formats = ['gif','bmp','jpg','jpeg','png']
		for f in files:
			if f[len(f)-f[::-1].find('.'):] in supported_formats:
				files2.append(f)
		option = tuple(f for f in files2)
		try:
			self.backgroundimg.set(option[1])
			bgimgo = ttk.OptionMenu(self.content,
					self.backgroundimg, "choose file", *option)
		except IndexError:
			bgimgo = ttk.Label(self.content,
					text="no possible background images found")
		self.add(bgimgo, (1, -1), 2)

		backgroundalpha_info = ttk.Label(self.content,
				text="merging intensity")
		self.add(backgroundalpha_info)
		self.backgroundalpha = tk.StringVar()
		self.backgroundalpha.set("0.5")
		option = tuple( str(x/10) for x in range(11))
		alpha = ttk.OptionMenu(self.content,
				self.backgroundalpha, "0", *option)
		self.add(alpha, (1, -1), 2)

		font_info = ttk.Label(self.content,
				text="font size")
		self.add(font_info)
		self.fontsize = tk.StringVar()
		self.fontsize.set("10")
		option = (10, 11, 12, 13)
		self.font = ttk.OptionMenu(self.content,
				self.fontsize, "choose size", *option)
		self.add(self.font, (1, -1), 2)

		extension_info = ttk.Label(self.content,
				text="output file extension")
		self.add(extension_info)
		self.extension = tk.StringVar()
		self.extension.set("jpg")
		self.extension0 = ttk.Radiobutton(self.content,
				text="jpg", variable=self.extension, value="jpg")
		self.add(self.extension0, (1, -1))
		self.extension1 = ttk.Radiobutton(self.content,
				text="png", variable=self.extension, value="png")
		self.add(self.extension1, (2, -1))

		default3 = ttk.Button(self.content,
				text="mobile default",
				command=lambda: self.setdefault1("n", "#ffffff", "#000000"))
		self.add(default3)
		default4 = ttk.Button(self.content,
				text="desktop default",
				command=lambda: self.setdefault1("y", "255,255,255", "0,0,0"))
		self.add(default4, (1, -1))
		default5 = ttk.Button(self.content,
				text="clear", command=self.setdefault1)
		self.add(default5, (2, -1))

		self.step2 = ttk.Button(self.content,
				text="create image...", command=self.step2, state="disabled")
		self.add(self.step2)

		self.responsive()


	def setdefault0(self, ndim="", ndia=""):
		self.dim.delete(0, tk.END)
		self.dim.insert(0, ndim)
		self.dia.delete(0, tk.END)
		self.dia.insert(0, ndia)
		self.scaleto0.invoke()

	def setdefault1(self, rotate="n", foregroundcolor="", backgroundcolor=""):
		self.foregroundcolor.delete(0, len(self.foregroundcolor.get()))
		self.foregroundcolor.insert(0, foregroundcolor)
		self.backgroundcolor.delete(0, len(self.backgroundcolor.get()))
		self.backgroundcolor.insert(0, backgroundcolor)
		self.rotate.set(rotate)

	def step1(self):
		self.step2.config(state="disabled")
		self.reduce["menu"].delete(0, "end")
		self.recommendation_info.config(text="nothing set yet...")
		if self.dia.get() and self.dim.get():
			dim = re.split(r"\D+",self.dim.get())
			dia, scaleto = float(self.dia.get()), self.scaleto.get()
			self.ui = ruler.inputs(dim=dim, dia=dia, scaleto=scaleto)

			fibo = ruler.fibonacci(self.ui)
			recommendation = '\nthe maximum amount of fibonacci squares is %d.'\
					%len(fibo.fibonaccis)
			if fibo.width > self.ui.width or fibo.height > self.ui.height:
				recommendation += '\nit is recommended to rotate it by 90°. or\
 you can reduce the number of squares.'
			self.recommendation_info.config(text=recommendation)
			option = tuple(str(x) for x in range(len(fibo.fibonaccis)))
			for choice in option:
				self.reduce["menu"].add_command(label=choice,
						command=tk._setit(self.reducefibo, choice))
			self.step2.config(state="normal")
		self.responsive()

	def step2(self):
		self.ui.update(reducefibo=self.reducefibo.get(),
						rotate=self.rotate.get(),
						fgcolor=self.foregroundcolor.get(),
						bgcolor=self.backgroundcolor.get(),
						bgimg=self.backgroundimg.get(),
						bgalpha=self.backgroundalpha.get(),
						fontsize=self.fontsize.get(),
						fileformat=self.extension.get())	
		
		ruler.draw_img(self.ui)

		finish_info = ttk.Label(self.content,
				text="\nthe image has been saved")
		self.add(finish_info)


app=pages("one app to make them all rulers", (470, 480))
app.root.mainloop()