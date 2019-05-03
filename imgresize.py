from PIL import Image
import os
import win32api

MAXSIZE=800 #pixel
curdir=os.getcwd()
confirmation=win32api.MessageBox(0, 'All images in directory "'+curdir+'" might be resized to 800px maximum width or height!', 'Image Resicer', 0x00001031)
if confirmation==1: #ok-button
	dir=os.listdir(curdir)
	for file in dir:
		name=file[0:file.rindex('.')]
		extension=file[file.rindex('.'):].lower()
		if extension in ('.jpg','.png'):
			img=Image.open(file)
			owidth=img.size[0]
			oheight=img.size[1]
			if owidth>MAXSIZE or oheight>MAXSIZE:
				if owidth>=oheight:
					height=round(MAXSIZE*oheight/owidth)
					width=MAXSIZE
				else:
					width=round(MAXSIZE*owidth/oheight)
					height=MAXSIZE
				img = img.resize((width, height), Image.ANTIALIAS)
				newname='{0}_resized{1}x{2}{3}'.format(name,width,height,extension)
				img.save(newname)
				print (newname)
else: #cancel-button
	exit()
