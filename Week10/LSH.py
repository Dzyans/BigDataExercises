from PIL import Image
import numpy as np


cat_one = Image.open('Cat1.png').convert('LA')
cat_two = Image.open('Cat2.png').convert('LA')

pix_cat_one = cat_one.resize((8,9),Image.ANTIALIAS)
pix_cat_two = cat_two.resize((8,9),Image.ANTIALIAS)

list_cat_one = list(pix_cat_one.getdata())
list_cat_two = list(pix_cat_two.getdata())

z = [i > j for i,j in zip(list_cat_one,list_cat_two)]

print z
#pix_cat_one.show()

#img = mpimg.imread('image.png')     
#gray = rgb2gray(img)    
#plt.imshow(gray, cmap = plt.get_cmap('gray'))
#plt.show()
