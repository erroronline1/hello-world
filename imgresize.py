from PIL import Image, ExifTags
import os
import win32api

MAXSIZE=800 #pixel
curdir=os.getcwd()
#confirmation=win32api.MessageBox(0, 'All images in directory "'+curdir+'" might be resized to 800px maximum width or height!', 'Image Resicer', 0x00001031)
confirmation==1 # since saving reduced copies there is no further need of user confirmation
if confirmation==1: #ok-button
	dir=os.listdir(curdir)
	for file in dir:
		name=file[0:file.rindex('.')]
		extension=file[file.rindex('.'):].lower()
		if extension in ('.jpg','.png'):
			img=Image.open(file)

			try:
				for orientation in ExifTags.TAGS.keys():
					if ExifTags.TAGS[orientation]=='Orientation':
						break
				exif=dict(img._getexif().items())

				if exif[orientation] == 3:
					img=img.rotate(180, expand=True)
				elif exif[orientation] == 6:
					img=img.rotate(270, expand=True)
				elif exif[orientation] == 8:
					img=img.rotate(90, expand=True)
			except (AttributeError, KeyError, IndexError):
				# cases: image don't have getexif
				pass

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
				img.close()
else: #cancel-button
	exit()
