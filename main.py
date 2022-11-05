# convert images to integer values 

from PIL import Image
import os
# get user input of image location and check it for access and format validity
while True:
  try:
    #imgdir = input("Please input full directory of the image you want to use:") 
    imgdir = './testing material/testimage.jpg'
    exists = os.path.exists(imgdir) # Checks if the file mentioned exists
    readacc = os.access(imgdir, os.R_OK) # Check for read access
    wracc = os.access(imgdir, os.W_OK) # check for write access
    imtype = Image.open(imgdir) # check to see if the file is an image
    break
    
  except: # does it exist? Can you read/write? is it usable by PIL ? Elsewise idfk
      if exists == False:print('Make sure you spelled the path correctly, and that the file you are referencing exists.')
      elif bool(readacc) != True or bool(wracc) != True:print("Python doesn't seem to have access to your image. Try rerunning this with administrator privilidges or moving your image (e.g. to the directory of this program)")
      elif IOError:print("Your file doesnt seem to be a valid format. Make sure your file is an image, or check the path you entered.")
      else: print('eh idk ')
      
# Read the image and find out all its pixels' positions and colors


# makes a tuple entry with all pixels, in a loop for every pixel, finding color and w/h and adding them to a list, then adding the list to a tuple of the image
workimage = Image.open(imgdir)
width, height = workimage.size
pixels = 1
hc = 1
wc = 1 
row = 1
imgset = []


# counter for width and height
while pixels <= ((width*height)-1):
  pixels = pixels + 1
  hc = hc + 1
  column = hc
  #defines each pixel and adds it to the imgset list
  wh = [column,row]
  pixrgb = workimage.load()
  rgba = pixrgb[(column-1),(row-1)]
  workpx = (list(rgba)+wh)
  imgset.append(tuple(workpx))

  if column == width:
    #row = wc
    wc = wc + 1
    hc = 0
    row = wc 
    
print(imgset)
# from here we should be able to comparing and grouping the pixels, and sticking them in objects (maybe name the group the color and a group iter?)
# how the fuck do tuples work ?????
#wkimageref[i] 
    
