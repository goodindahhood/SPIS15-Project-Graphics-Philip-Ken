# SPIS15-Project-Graphics-Philip-Ken


##Seam Carving

**Process**
* We first changed the colored picture into greyscale.  
* Afterwards we then calculated energy through subtracting surrounding greyscale values of adjacent pixels for each &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pixel
* Then we calculated a path from top to bottom or left to right that acculumated the lowest amount of energy.
* This was achieved through adding energy values from top to bottom or left to right where on the right or bottom side &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; the energy values are the highest since all the lowest energy values on its were added.   
* By finding the lowest energy value at the end (bottom/left), we can backtrack to find the lowest energy seam/line.  
* Using the location of each pixel we created a red blank picture and painted the original picture on top of it while &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;skipping the pixels that were apart of the lowest energy seam.  
* A clear red line/seam of the lowest energy is shown on the new picture so we create a smaller picture (by 1 pixel) that &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;skips the red line essentially removing the seam. 
* This step is repeated by the desired amount of times to get the size we want.  

**Known Benefits -**  
1.) Picture is resized (smaller) while keeping all the important details included unlike cropping or scaling

**Known Detriments -**    
1.) Some of the important details do get cut out since the formula cuts that part of the image, thinking it has the lowest &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;energy  
*(Content Aware Seam Carving causes the important details to be saved by making the content contain more "energy", &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;negating this detriment)*  
2.)The picture sometimes become disjointed where the left side of a pixel might not blend well with the right  
 


**Known Problems -**    
1.) By removing lots of height or y pixel length, lines are created that move certain parts of the picture up 1 pixel  
2.) Removing lots of either x or y pixel length creates areas that don't blend well together  
*(Seam Carving through first resizing then seam carving fixes some detriments/problems like this)* 
  

**Examples**  
