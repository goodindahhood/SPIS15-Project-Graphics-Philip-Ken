# SPIS15-Project-Graphics-Philip-Ken


##Seam Carving

We first changed the colored picture into greyscale.  
Afterwards we then calculated energy through subtracting surrounding greyscale values of adjacent pixels for each pixel  
Then we calculated a path from top to bottom or left to right that acculumated the lowest amount of energy.
This was achieved through adding energy values from top to bottom or left to right where on the right or bottom side the energy values are the highest since all the lowest energy values on its were added.   
By finding the lowest energy value at the end (bottom/left), we can backtrack to find the lowest energy seam/line.  
Using the location of each pixel we created a red blank picture and painted the original picture on top of it while skipping the pixels that were apart of the lowest energy seam.  
A clear red line/seam of the lowest energy is shown on the new picture so we create a smaller picture (by 1 pixel) that skips the red line essentially removing the seam. 
This step is repeated by the desired amount of times to get the size we want.  

