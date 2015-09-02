from PIL import Image, ImageDraw
land = Image.open('bench.jpg')
land2 = Image.open('Animulandscape.jpg')
land3 = Image.open('Animulandscape.jpg')
listenergy = []

##land.show()
##def copy(pic):
##    for x in range(width):
##        for y in range (height):
##            (r,g,b) = pic.getpixel((x,y))
##            


##def seampractice():
##    
## 
##    table = [[0 for suby in range(height)] for subx in range(width)] #Creates table to store basic greyscale value
##    for x in range(width):
##        for y in range(height):
##            (Red, Green, Blue) = land.getpixel((x,y))
##            newred = Red * .21
##            newgreen = Green * .72
##            newblue = Blue * .07
##            totalcolor =  int((newred + newgreen + newblue))
##            land2.putpixel((x,y), (totalcolor, totalcolor, totalcolor)) #Calculates Greyscale
##            table[x][y] = totalcolor
##    entable = [[0 for suby in range(height)] for subx in range(width)] #Creates table to calculates each pixel's energy values
##    for x in range(width):
##        for y in range(height):
##            a,b = 1,1
##            if y == (height -1):
##                a = 0
##            if x == (width - 1): #if cases are for when points on edges where outside values cannot be obtained (out of range)
##                b = 0
##            entable[x][y] = ((abs(table[x][y] - table[x+b][y])) + abs(table[x][y] - table[x][y+a]))
##    totalentable = [[0 for sub in range(height)] for subx in range(width)] #creates table for storing total least energy values
##    totalentable[0][0] = 0
##    for y in range(height): #For y and For x need to be in this order where we calculate energy row by row not column by column where above energy values will not be present
##        for x in range(width):
##            c,d = -1,1         #Cases for when the x is at the edge where a table value above a point would not be available.
##            if x == 0:             
##                c =0
##            if x == width -1:
##                d = 0
##            totalentable[x][y] = entable[x][y] + testtopmin(y,totalentable[x][y-1],totalentable[x+c][y-1],totalentable[x+d][y-1])
##                #adds the energy values and stores in table
##    a = 9999999
##    mintotalentable = [0 for i in range(height)]
##    for y in range(height - 1, 0, -1):
##        for x in range(width - 1):
##            b = min(totalentable[x][y], 1000000)
##            if a > b:
##                a = b
##                mintotalentable[y] = b
##    newimage = Image.new('RGB', (height, (width -1)), (255,255,255))
##    height2, width2 = newimage2.size           
##    for y in range(height2, 0, -1):
##        for x in range(width2):
##            if totalentable[x][y] == mintotalentable[y]:
##                x = x + 1
##            (red, green, blue) = newimage2.getpixel((x,y))
##            newimage.putpixel((x,y), (red, green, blue))

def testtopmin(y,q,w,e):
    """Compares the energy values above the point indicated (The three values being evaluated are above and above diagonally) Returns the lowest value of energy""" 
    if y == 0:
        return 0
    elif w >= q:
        if q < e:
            return q
        else:
            return e   
    elif w <= e:
        return w
    else:
        return e
    return 0


    





def seampractice(pic, n):
    
    width, height = pic.size
    table = [[0 for suby in range(height)] for subx in range(width)] #Creates table to store basic greyscale value

    for x in range(width):
        for y in range(height):
            (Red, Green, Blue) = pic.getpixel((x,y))
            newred = Red * .21
            newgreen = Green * .72
            newblue = Blue * .07
            totalcolor =  int((newred + newgreen + newblue))
##            land2.putpixel((x,y), (totalcolor, totalcolor, totalcolor)) #Calculates Greyscale
            table[x][y] = totalcolor

    entable = [[0 for suby in range(height)] for subx in range(width)] #Creates table to calculates each pixel's energy values

    for x in range(width):
        for y in range(height):
            a,b = 1,1
            if y >= (height -1):
                a = 0
            if x >= (width - 1): #if cases are for when points on edges where outside values cannot be obtained (out of range)
                b = 0
            entable[x][y] = ((abs(table[x][y] - table[x+b][y])) + abs(table[x][y] - table[x][y+a]))
    totalentable = [[0 for sub in range(height)] for subx in range(width)] #creates table for storing total least energy values
    totalentable[0][0] = 0


    newimage2 = Image.new('L', ((width - 1), (height)), (255))
    for x in range(width - 1):
        for y in range(height - 1):
            a = int(entable[x][y] * 2)
            newimage2.putpixel((x,y),(a))

    

    for y in range(height): #For y and For x need to be in this order where we calculate energy row by row not column by column where above energy values will not be present
        for x in range(width):
            c,d = -1,1         #Cases for when the x is at the edge where a table value above a point would not be available.
            if x <= 0:             
                c =0
            if x >= width -1:
                d = 0
            totalentable[x][y] = entable[x][y] + testtopmin(y,totalentable[x][y-1],totalentable[x+c][y-1],totalentable[x+d][y-1])
                #adds the energy values and stores in table

    a = 9999999 #beginning upper value to test for lower value
    mintotalentable = [[0 for i in range(height)] for h in range(2)] #create table of height length to store the mininum total energy for each row. (might not need all the table spaces)
    y = height - 1

    for x in range(width): #only tests for the lowest total energy value on the bottom
        b = totalentable[x][y]
        if a > b: #case to test for the lowest total energy value
            a = b
            mintotalentable[0][y] = b #stores the mininum total energy value
            mintotalentable[1][y] = x #stores x value (might be redunant because of variable 'c'
            c =x                      #stores the x value of the lowest total energy value on the bottom
##    newimage = Image.new('RGB', ((width - 1), (height)), (255,0,0)) #creates a new image of 1 less width to put picture
##    finx = c        #stores the value of c as finx
##
##
##
##
##    for y in range(height - 1, -1, -1): #starts from bottom then goes to top
##        for subx in range(-1, 2):
##            c,d = -1,1         #Cases for when the x is at the edge where a table value above a point would not be available.
##            if finx <= 0 +.5:
##                c =0
##            if finx >= width - 1.5:
##                d = 0
##            if finx >= (width -1) - .5:
##                if subx == 1:
##                    subx = 0
##            if finx <= 0 & subx == -1:
##                subx = 0
##            f = min(totalentable[finx][y],totalentable[finx + d][y],totalentable[finx + c][y])
##            a = totalentable[finx + subx][y]
##            if a <= f + .5:
##                finx = finx + subx
##                finy = y
##        for secx in range(width - 1):
##            subz = 1
##            thix = secx
##            forx = secx
##            if secx >= finx - .5:
##                if secx <= finx +.5:
##                    if thix >= (width -1) - .5:
##                        if subz >= 1 - .5:
##                            subz = 0
##                    if thix <= (1 -.5):
##                        subz = 0
##                    thix = thix -subz
##                    pass
##            (r,g,b) = pic.getpixel((forx, finy))
##            newimage.putpixel((thix,finy),(r,g,b))

    newimage = Image.new('RGB', ((width - 1), (height)), (255,0,0)) #creates a new image of 1 less width to put picture
    finx = c        #stores the value of c as finx




    for y in range(height - 1, -1, -1): #starts from bottom then goes to top
        for subx in range(-1, 2):
            c,d = -1,1         #Cases for when the x is at the edge where a table value above a point would not be available.
            if finx <= 0 +.5:
                c =0
            if finx >= width - 1.5:
                d = 0
            if finx >= (width -1) - .5:
                if subx == 1:
                    subx = 0
            if finx <= 0 & subx == -1:
                subx = 0
            f = min(totalentable[finx][y],totalentable[finx + d][y],totalentable[finx + c][y])
            a = totalentable[finx + subx][y]
            if a <= f + .5:
                finx = finx + subx
                finy = y
        for secx in range(width - 1):
            subz = 1
            thix = secx
            forx = secx
            if secx >= finx - .5:
                if secx <= finx +.5:
                    if thix >= (width -1) - .5:
                        if subz >= 1 - .5:
                            subz = 0
                    if thix <= (1 -.5):
                        subz = 0
                    thix = thix -subz
                    pass
            (r,g,b) = pic.getpixel((forx, finy))
            newimage.putpixel((thix,finy),(r,g,b))
         



    
        
        
            

##    for y in range(height - 1, 0, -1):
##        for x in range(width - 3):
##            if totalentable[x][y] == mintotalentable[y][0]:
##                if x < width:
##                    x = x + 1
##            (red, green, blue) = pic.getpixel((x,y))
##            newimage.putpixel((x,y), (red, green, blue))
##    print newimage.size
##  
    
    
    if n > 0 :
        seampractice(newimage, n - 1)
    
    if n %5 == 0:
        newimage.show()
        newimage2.show()
    a = newimage
    return a
        
    
        
--------------------------------------------------------------------------------------------
from PIL import Image, ImageDraw
import webbrowser

land = Image.open('Animulandscape.jpg')
land3 = Image.open('Animulandscape.jpg')
listenergy = []


global li
global orig
global end
global width1
global height1
orig = Image.open('Animulandscape.jpg')
width1, height1 = orig.size
li = [[0 for sub in range(height1)] for subx in range(width1)]
end = Image.new('RGB', ((width1), (height1)), (255,0,0))



##land.show()
##def copy(pic):
##    for x in range(width):
##        for y in range (height):
##            (r,g,b) = pic.getpixel((x,y))
##            


##def seampractice():
##    
## 
##    table = [[0 for suby in range(height)] for subx in range(width)] #Creates table to store basic greyscale value
##    for x in range(width):
##        for y in range(height):
##            (Red, Green, Blue) = land.getpixel((x,y))
##            newred = Red * .21
##            newgreen = Green * .72
##            newblue = Blue * .07
##            totalcolor =  int((newred + newgreen + newblue))
##            land2.putpixel((x,y), (totalcolor, totalcolor, totalcolor)) #Calculates Greyscale
##            table[x][y] = totalcolor
##    entable = [[0 for suby in range(height)] for subx in range(width)] #Creates table to calculates each pixel's energy values
##    for x in range(width):
##        for y in range(height):
##            a,b = 1,1
##            if y == (height -1):
##                a = 0
##            if x == (width - 1): #if cases are for when points on edges where outside values cannot be obtained (out of range)
##                b = 0
##            entable[x][y] = ((abs(table[x][y] - table[x+b][y])) + abs(table[x][y] - table[x][y+a]))
##    totalentable = [[0 for sub in range(height)] for subx in range(width)] #creates table for storing total least energy values
##    totalentable[0][0] = 0
##    for y in range(height): #For y and For x need to be in this order where we calculate energy row by row not column by column where above energy values will not be present
##        for x in range(width):
##            c,d = -1,1         #Cases for when the x is at the edge where a table value above a point would not be available.
##            if x == 0:             
##                c =0
##            if x == width -1:
##                d = 0
##            totalentable[x][y] = entable[x][y] + testtopmin(y,totalentable[x][y-1],totalentable[x+c][y-1],totalentable[x+d][y-1])
##                #adds the energy values and stores in table
##    a = 9999999
##    mintotalentable = [0 for i in range(height)]
##    for y in range(height - 1, 0, -1):
##        for x in range(width - 1):
##            b = min(totalentable[x][y], 1000000)
##            if a > b:
##                a = b
##                mintotalentable[y] = b
##    newimage = Image.new('RGB', (height, (width -1)), (255,255,255))
##    height2, width2 = newimage2.size           
##    for y in range(height2, 0, -1):
##        for x in range(width2):
##            if totalentable[x][y] == mintotalentable[y]:
##                x = x + 1
##            (red, green, blue) = newimage2.getpixel((x,y))
##            newimage.putpixel((x,y), (red, green, blue))

def testtopmin(y,q,w,e):
    """Compares the energy values above the point indicated (The three values being evaluated are above and above diagonally) Returns the lowest value of energy""" 
    if y == 0:
        return 0
    elif w >= q:
        if q < e:
            return q
        else:
            return e   
    elif w <= e:
        return w
    else:
        return e
    return 0


    





def seampractice(pic, n):
    
    width, height = pic.size
    width1, height1 = orig.size
    table = [[0 for suby in range(height)] for subx in range(width)] #Creates table to store basic greyscale value
    for x in range(width):
        for y in range(height):
            (Red, Green, Blue) = pic.getpixel((x,y))
            newred = Red * .21
            newgreen = Green * .72
            newblue = Blue * .07
            totalcolor =  int((newred + newgreen + newblue))
##            land2.putpixel((x,y), (totalcolor, totalcolor, totalcolor)) #Calculates Greyscale
            table[x][y] = totalcolor

    entable = [[0 for suby in range(height)] for subx in range(width)] #Creates table to calculates each pixel's energy values

    for x in range(width):
        for y in range(height):
            a,b = 1,1
            if y >= (height -1):
                a = 0
            if x >= (width - 1): #if cases are for when points on edges where outside values cannot be obtained (out of range)
                b = 0
            entable[x][y] = ((abs(table[x][y] - table[x+b][y])) + abs(table[x][y] - table[x][y+a]))
    totalentable = [[0 for sub in range(height)] for subx in range(width)] #creates table for storing total least energy values
    totalentable[0][0] = 0


    newimage2 = Image.new('L', ((width - 1), (height)), (255))
    for x in range(width - 1):
        for y in range(height - 1):
            a = int(entable[x][y] * 2)
            newimage2.putpixel((x,y),(a))

    

    for y in range(height): #For y and For x need to be in this order where we calculate energy row by row not column by column where above energy values will not be present
        for x in range(width):
            c,d = -1,1         #Cases for when the x is at the edge where a table value above a point would not be available.
            if x <= 0:             
                c =0
            if x >= width -1:
                d = 0
            totalentable[x][y] = entable[x][y] + testtopmin(y,totalentable[x][y-1],totalentable[x+c][y-1],totalentable[x+d][y-1])
                #adds the energy values and stores in table

    a = 9999999 #beginning upper value to test for lower value
    mintotalentable = [[0 for i in range(height)] for h in range(2)] #create table of height length to store the mininum total energy for each row. (might not need all the table spaces)
    y = height - 1

    for x in range(width): #only tests for the lowest total energy value on the bottom
        b = totalentable[x][y]
        if a > b: #case to test for the lowest total energy value
            a = b
            mintotalentable[0][y] = b #stores the mininum total energy value
            mintotalentable[1][y] = x #stores x value (might be redunant because of variable 'c'
            c =x                      #stores the x value of the lowest total energy value on the bottom
##    newimage = Image.new('RGB', ((width - 1), (height)), (255,0,0)) #creates a new image of 1 less width to put picture
##    finx = c        #stores the value of c as finx
##
##
##
##
##    for y in range(height - 1, -1, -1): #starts from bottom then goes to top
##        for subx in range(-1, 2):
##            c,d = -1,1         #Cases for when the x is at the edge where a table value above a point would not be available.
##            if finx <= 0 +.5:
##                c =0
##            if finx >= width - 1.5:
##                d = 0
##            if finx >= (width -1) - .5:
##                if subx == 1:
##                    subx = 0
##            if finx <= 0 & subx == -1:
##                subx = 0
##            f = min(totalentable[finx][y],totalentable[finx + d][y],totalentable[finx + c][y])
##            a = totalentable[finx + subx][y]
##            if a <= f + .5:
##                finx = finx + subx
##                finy = y
##        for secx in range(width - 1):
##            subz = 1
##            thix = secx
##            forx = secx
##            if secx >= finx - .5:
##                if secx <= finx +.5:
##                    if thix >= (width -1) - .5:
##                        if subz >= 1 - .5:
##                            subz = 0
##                    if thix <= (1 -.5):
##                        subz = 0
##                    thix = thix -subz
##                    pass
##            (r,g,b) = pic.getpixel((forx, finy))
##            newimage.putpixel((thix,finy),(r,g,b))

    newimage = Image.new('RGB', ((width - 1), (height)), (255,0,0)) #creates a new image of 1 less width to put picture
    finx = c        #stores the value of c as finx


    

    for y in range(height - 1, -1, -1): #starts from bottom then goes to top
        for subx in range(-1, 2):
            c,d = -1,1         #Cases for when the x is at the edge where a table value above a point would not be available.
            if finx <= 0 +.5:
                c =0
            if finx >= width - 1.5:
                d = 0
            if finx >= (width -1) - .5:
                if subx == 1:
                    subx = 0
            if finx <= 0 & subx == -1:
                subx = 0
            f = min(totalentable[finx][y],totalentable[finx + d][y],totalentable[finx + c][y])
            a = totalentable[finx + subx][y]
            if a <= f + .5:
                finx = finx + subx
                finy = y
        for secx in range(width - 1):
            subz = 1
            thix = secx
            forx = secx
            if secx >= finx - .5:
                if secx <= finx +.5:
                    if thix >= (width -1) - .5:
                        if subz >= 1 - .5:
                            subz = 0
                    if thix <= (1 -.5):
                        subz = 0
                    thix = thix  - subz
                    li[forx][finy] = [forx,finy]
            (r,g,b) = pic.getpixel((forx, finy))
            newimage.putpixel((thix,finy),(r,g,b))
    filename = "test.jpg"
    newimage.save(filename)
    webbrowser.open(filename)
##    width1 = width1 -1
##    height1 = height1 -1
    prseams(li,(height1),(width1), newimage)

    
    if n > 1 :
        seampractice(newimage, n - 1)
    if n == 1:
##        countwhite(end)
        getridcolor(end)          
    a = newimage
    return a
        
def getridcolor(pic):
    width,height = pic.size
    newimage = Image.new('RGB', (width, height), (255,0,0))
    for y in range(height):
        for x in range(width):
            (r,g,b) = pic.getpixel((x, y))
            if (r,g,b) != (255,0,0):
                pass
            else:
                add = 1
                if x == width -1:
                    add = 0
                (r,g,b) = pic.getpixel((x + add,y))
            newimage.putpixel((x,y),(r,g,b))

        

def countwhite(pic):
    width,height = pic.size
    count = 0
    for y in range(height):
        for x in range(width):
            (r,g,b) = pic.getpixel((x,y))
            if (r,g,b) == (255,255,255):
                count = count + 1
            else:
                pass
        print count
    print count

def prseams(li,height1, width1, orig):
    for y in range(height1):
            for x in range (width1):
                suby = 0
                if li[x][y] == [x,y]:
                    suby = 1
                    pass
                else:
                    (r,g,b) = orig.getpixel((x,y))
                    end.putpixel((x,y),(r,g,b))
    orig = end
    height1, width1 = orig.size
    li = [[0 for sub in range(height1)] for subx in range(width1)]
    getridcolor(orig)
    filename1 = "test1.jpg"
    end.save(filename1)
    import webbrowser
    webbrowser.open(filename1)
                

