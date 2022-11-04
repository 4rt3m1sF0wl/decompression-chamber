# convert images to integer values 

from PIL import Image
import os
# get user input of image location and check it for access and format validity
while True:
  try:
    imgdir = input("Please input full directory of the image you want to use:") 
    readacc = os.access(imgdir, os.R_OK) # Check for read access
    wracc = os.access(imgdir, os.W_OK) # check for write access
    im=Image.open(imgdir) # check to see if the file is an image
    break
    
    except readacc != True or wracc != True: 
      print("Python doesn't seem to have access to your image. Try rerunning this with administrator privilidges or moving your image (e.g. to the directory of this program)")

    except IOError:
      print("Your file doesnt seem to be a valid format. Make sure your file is an image, or check the path you entered.")
  
  
    # read image - find number of pixels - make a loop to add an entry for every pixel by adding its rgb vals and location, also ID of loop iter

# image gets opened and read, then a list(tuple) is made of all pixels, l to r, downwards of the R G B and alpha values 
workimage = Image.open(imgdir, 'r')
wkimset = list(workimage.getdata())

# in theory this code counts up the width and height of the image and adds them to each individual set of the old tuple as a new list (R,G,B,A,W,H) and makes a new tuple element out of this list
width = Image.width(imgdir)
height = Image.height(imgdir)
for global int height:
  height = height + 1 
  loopheight = height
  width = 0
  for global int width:
    count = count + 1 
    width = width + 1 
    wkimlist = list(wkimset[count])
    wkimlist.extend(str width, str loopheight)
    wkimageref = tuple + (wkimlist)

# from here we should be able to comparing and grouping the pixels, and sticking them in groups (maybe name the group the color and a group iter?)
    
    
