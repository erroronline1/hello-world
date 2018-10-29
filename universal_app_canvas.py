###############################################################################
# scrollable all purpose app container
# refactored by error on line 1 (erroronline.one)
# original by noob oddy, now to be used responsive with any widget
#
# refactored as of 2018-08-22 to be responsive and mostly pep8 compliant
# 2018-08-23 added debugger display and method
###############################################################################

import tkinter as tk
from tkinter import ttk

class Container(ttk.Frame):
	"""
	this is the main class to create a program window with scrollable content.
	calling its add-method after defining the next widget adds to the grid layout.
	column and row can be defined realtive to previous widget.
	the actual app should extend the container-class so input values can be
	handled through the programm.
	the container has a responsive behaviour given a minimal width on initiation
	the initial width should represent the minimal width. if the window is resized
	below this value or the screen is smaller, the grid-layout changes automatically
	"""
	def __init__(self, title="all purpose application container",
					geometry=(640, 480)):
		self.geometry = geometry
		self.root = tk.Tk()
		self.root.geometry(str(geometry[0])+"x"+str(geometry[1]))
		self.root.title(title)
		self.root.grid_rowconfigure(0, weight=1) # change all content with window size
		self.root.grid_columnconfigure(0, weight=1) # change all with window size

		self.canv = tk.Canvas(self.root, bd=0, highlightthickness=0)
		self.hScroll = ttk.Scrollbar(self.root, orient="horizontal",
									command=self.canv.xview)
		self.hScroll.grid(row=1, column=0, sticky="we")
		self.vScroll = ttk.Scrollbar(self.root, orient="vertical",
									command=self.canv.yview)
		self.vScroll.grid(row=0, column=1, sticky="ns")
		self.vScroll.update_idletasks() #updates width-value
		self.canv.grid(row=0, column=0, sticky="nsew")
		self.canv.configure(xscrollcommand=self.hScroll.set,
									yscrollcommand=self.vScroll.set)

		self.content = ttk.Frame(self.canv) # holds actual content

		self.canv.create_window(0, 0, window=self.content, anchor="nw",
									tags="inner")
		self.canv.grid(row=0, column=0, sticky="nsew")

		self.menubar=tk.Menu(self.root)
		self.filemenu = tk.Menu(self.root, tearoff=0)
		self.filemenu.add_command(label="by error on line 1")
		self.filemenu.add_command(label="quit", command=self.root.quit)
		self.menubar.add_cascade(label=" \u2261 ", menu=self.filemenu)
		
		self.root.config(menu=self.menubar) # display the menu

		self.canv.bind("<Configure>", self.on_configure)
		self.canv.bind_all('<MouseWheel>', lambda event: self.canv.yview_scroll(int(-1*(event.delta/120)), "units"))
	def on_configure(self, event):
		"""updates on scroll-area in case of changed window-size"""
		w,h = event.width, event.height
		natural = self.content.winfo_reqwidth()
		self.canv.itemconfigure("inner", width=w if w > natural else natural)
		self.responsive()
	
	def responsive(self):
		"""swaps between grid-layout and flowed layout"""
		elements = self.content.winfo_children()
		for el in elements:
			if self.canv.winfo_width()+self.vScroll.winfo_width() >= self.geometry[0] \
			and self.content.winfo_reqwidth()+self.vScroll.winfo_width() <= self.root.winfo_screenwidth():
				el.grid_forget()
				el.grid(**el.gridsetting)
				self.content.grid_columnconfigure(0, weight=0)
			else:
				el.grid_forget()
				el.grid(column=0, padx=2, pady=2, columnspan=1, sticky="we")
				self.content.grid_columnconfigure(0, weight=1)
			if el.winfo_class() == "TLabel":
				el.configure(wraplength=self.canv.winfo_width()
						-self.vScroll.winfo_width())
		self.canv.update_idletasks()
		self.canv.configure(scrollregion=self.canv.bbox("all"))
		self.debug("grid if", self.canv.winfo_width()+self.vScroll.winfo_width(),">=", self.geometry[0],
			"and", self.content.winfo_reqwidth()+self.vScroll.winfo_width(),"<=", self.root.winfo_screenwidth(),self.root.winfo_geometry())
 
	def add(self, widget, colrow=None, columnspan=1):
		"""adds widgets to content one at a time.
		negative row adds to previous ones"""
		if colrow == None:
			colrow = (0,0)
		column = colrow[0]
		row = self.content.grid_size()[1] + colrow[1]
		widget.grid(row=row, column=column, columnspan=columnspan,
									padx=2, pady=2, sticky="we")
		widget.gridsetting = (widget.grid_info()) # save settings for responsiveness
		"""updates on scroll-area after content change"""
		self.content.update_idletasks()
		natural = self.content.winfo_width()
		self.canv.itemconfigure("inner", width=natural)
		self.canv.configure(scrollregion=self.canv.bbox("all"))
		#self.canv.yview("moveto","1.0")

	def debug(self,*args):
		info=[i for i in args]
		if info:
			try:
				self.debugm.entryconfig(0, label=info)
			except AttributeError:
				self.debugm=tk.Menu(self.root, tearoff=0)
				self.debugm.add_command(label=info)
				self.menubar.add_cascade(label="debug info", menu=self.debugm)

if __name__ == "__main__":
	""" DEMO if not used as module """
#	class pages(universal_app_canvas.Container): if imported as a module
	class pages(Container):
		def __init__(self, title="TitleNotFoundException ;)", geometry=(640, 480)):
			super().__init__(title, geometry)

			def new_label():
				test = ttk.Label(self.content,
						text="this is an label")
				self.add(test)
				test2 = ttk.Label(self.content,
						text="this is a 2nd label")
				self.add(test2, (1, -1))
				test3 = ttk.Label(self.content,
						text="this is a 3rd label. try resizing the window")
				self.add(test3, (2, -1))
				self.responsive()

			b = ttk.Button(self.root,
					text="new labels", command=new_label)
			b.grid(sticky="we")
			
			def new_entry():
				test = ttk.Label(self.content,
						text="this is an entry field")
				self.add(test)
				test2 = ttk.Entry(self.content)
				self.add(test2, (1, -1), 3)
				self.responsive()

			c = ttk.Button(self.root,
					text="new entryfield", command=new_entry)
			c.grid(sticky="we")

			def new_widelabel():
				testtext="this is a wide label that is supposed to \
have a wide appearance over three columns"
				test = ttk.Label(self.content, text=testtext)#, wraplength=150)
				self.add(test, None, 3)
				self.responsive()

			d = ttk.Button(self.root,
					text="new wide label", command=new_widelabel)
			d.grid(sticky="we")

	app=pages("all purpose app canvas", (640, 480))
	app.root.mainloop()