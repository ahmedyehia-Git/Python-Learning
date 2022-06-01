# Pillow one of packages that can manbulate images like photoshop
import PIL # to import pillow


from PIL import Image # to deal with image
from PIL import ImageFilter # this allow to make effects on image like blur

# show in unix display only one img could not display the many image at the same time 

#img = Image.open('/home/ahmed/Documents/Programs_Web/Python_CS50/Pillow/cat.jpg') # if image not in the same folder I should give the full path
img = Image.open('Pillow/cat.jpg')
#img.show() 



bw = img.convert("L")
#bw.show()


val = (100,100, 1300,1300)# to ive dimenssion of crop (left, upper, right, lower)
crop = img.crop(val)
#crop.show()

blur = img.filter(ImageFilter.BoxBlur(15))
#blur.show()

emb = img.filter(ImageFilter.EMBOSS())
#emb.show()

edg = img.filter(ImageFilter.EDGE_ENHANCE())
#edg.show()