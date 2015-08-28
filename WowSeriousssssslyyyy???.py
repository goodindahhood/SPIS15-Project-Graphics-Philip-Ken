from PIL import Image, ImageDraw
land = Image.open('Animulandscape.jpg')
land2 = Image.open('Animulandscape.jpg')
width,height = land.size
listenergy = []


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
            land2.putpixel((x,y), (totalcolor, totalcolor, totalcolor)) #Calculates Greyscale
            table[x][y] = totalcolor
    entable = [[0 for suby in range(height)] for subx in range(width)] #Creates table to calculates each pixel's energy values
    for x in range(width):
        for y in range(height):
            a,b = 1,1
            if y == (height -1):
                a = 0
            if x == (width - 1): #if cases are for when points on edges where outside values cannot be obtained (out of range)
                b = 0
            entable[x][y] = ((abs(table[x][y] - table[x+b][y])) + abs(table[x][y] - table[x][y+a]))
    totalentable = [[0 for sub in range(height)] for subx in range(width)] #creates table for storing total least energy values
    totalentable[0][0] = 0
    for y in range(height): #For y and For x need to be in this order where we calculate energy row by row not column by column where above energy values will not be present
        for x in range(width):
            c,d = -1,1         #Cases for when the x is at the edge where a table value above a point would not be available.
            if x == 0:             
                c =0
            if x == width -1:
                d = 0
            totalentable[x][y] = entable[x][y] + testtopmin(y,totalentable[x][y-1],totalentable[x+c][y-1],totalentable[x+d][y-1])
                #adds the energy values and stores in table
    a = 9999999
    mintotalentable = [[0 for i in range(height)] for h in range(2)]
    y = height - 1
    for x in range(width):
        b = totalentable[x][y]
        if a > b:
            a = b
            mintotalentable[0][y] = b
            mintotalentable[1][y] = x
            c =x
    newimage = Image.new('RGB', ((width - 1), (height)), (255,255,255))
    b = 999999999
    finx = c
    for y in range(height - 1, 0, -1):
        for subx in range(-1,2,1):
            if finx == width - 1 & subx == 1:
                subx = 0
            if finx == 0 & subx == -1:
                subx = 0
            a = totalentable[finx+subx][y]
            if a < b:
                b = a
                finx = finx + subx
                finy = y
        for secx in range(width - 1):
            thix = secx
            if secx == finx:
                thix = secx - 1
                pass
            (r,g,b) = pic.getpixel((secx, y))
            newimage.putpixel((thix,y),(r,g,b))
        
        
            

##    for y in range(height - 1, 0, -1):
##        for x in range(width - 3):
##            if totalentable[x][y] == mintotalentable[y][0]:
##                if x < width:
##                    x = x + 1
##            (red, green, blue) = pic.getpixel((x,y))
##            newimage.putpixel((x,y), (red, green, blue))
##    print newimage.size
##    
    newimage.show()
    
    
    if n > 0 :
        seampractice(newimage, n - 1)

    a = newimage
    return a
        
    
        

            

