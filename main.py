# convert images to integer values 

from PIL import Image
import os
"""This is the threshold for color distance for like pixels!! Changing this will change the inclusivity of group formation!!"""
margin = .05
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
hc = 0
wc = 1 
row = 1
imgset = []


# counter for width and height
while pixels <= ((width*height)):
  pixels = pixels + 1
  hc = hc + 1
  column = hc
  #defines each pixel and adds it to the imgset list
  pixrgb = workimage.load()
  rgba = pixrgb[(column-1),(row-1)]
  rgb = list(rgba) # this list is to make sure tuples are standard length with no alpha vals 
  workpx = (rgb[0],rgb[1],rgb[2],column,row)
  imgset.append(tuple(workpx))
  if column == width:
    #row = wc
    wc = wc + 1
    hc = 0
    row = wc 
    
# Group the pixels surrounding and compare them to see if they are similar color, then add them to lists respecting their color

i = -1
while i < ((width*height)-1):
  i = i + 1
  # get all comparing pixels and working pixels (l=< r=> u=^ lw=v)
  workpx = imgset[i]
  try: comppxl = imgset[i-1]
  except IndexError: comppxl = False #'noleftedge'
  try: comppxr = imgset[i+1]
  except IndexError: comppxr = False #'norightedge'
  try: comppxu = imgset[i-width]
  except IndexError: comppxu = False #'noupperedge'
  try: comppxlw = imgset[i+width]
  except IndexError: comppxlw =  False #'noloweredge'
  # if pixels dni, then their values are made null

# if i = 0 then make a new group called rgb0 for first group

  # test right pixel to see if it is same color, then add it to a group by surrounding pixels 
  if ((comppxr[0]-workpx[0])**2+(comppxr[1]-workpx[1])**2+(comppxr[2]-workpx[2])**2) <= round((margin*255)**2): print('working on it')
    ## WE WILL HAVE PROBLEMS WHEN THE COMPARATOR HITS AN EDGE!!! MAKE SURE TO COVER THIS LATER -- try except typeError ?? add higher if stmt for no edgepx??  
    ##check to see which of the surrounding pixels are the same and then add the closest one's group number on the pixel and add it to the group

  else:
    print('working on it')
    ##make new group and add the number to the pixels tuple
    ##group name format = concattenated rgb+i, group will contain full pixel tuple, maybe minus gid ? 
    ##maybe add an edge value ?! check if the pixel is completely surrounded by neighbors, then give it a T F for edge val on the tuple(7-1) for edge drawing later. 
