from PIL import Image
import numpy as np

def LSH(image1, image2):
    pix_image1 = image1.resize((8,9),Image.ANTIALIAS)
    pix_image2 = image2.resize((8,9),Image.ANTIALIAS)
    
    list_image1 = list(pix_image1.getdata())
    list_image2 = list(pix_image2.getdata())
    
    lsh = [i > j for i,j in zip(list_image1,list_image2)]
    lsh = np.reshape(lsh, (8, 9))
    return lsh

def hash(differences):
   for difference in differences:
       decimal_value = 0
       hex_string = []
       for index, value in enumerate(difference):
           if value:
               decimal_value += 2**(index % 8)
           if (index % 8) == 7:
               hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
               decimal_value = 0
       print ''.join(hex_string),

cat_one = Image.open('Cat1.png').convert('LA')
cat_two = Image.open('Cat2.png').convert('LA')
hash(LSH(cat_one,cat_two))
print '\n'
dog_one = Image.open('dog1.jpg').convert('LA')
hash(LSH(cat_one,dog_one))