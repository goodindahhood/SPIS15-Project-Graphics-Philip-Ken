from PIL import Image, ImageDraw

land = Image.open('Animulandscape.jpg')
width,height = land.size
listenergy = []


def seampractice():
    table = [[0 for suby in range(height)] for subx in range(width)] #Creates table to store basic greyscale value
    for x in range(width):
        for y in range(height):
            (Red, Green, Blue) = land.getpixel((x,y))
            newred = Red * .21
            newgreen = Green * .72
            newblue = Blue * .07
            totalcolor =  int((newred + newgreen + newblue))
            land.putpixel((x,y), (totalcolor, totalcolor, totalcolor)) #Calculates Greyscale
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
    for y in range(height, 0, -1):
        for x in range(width):
            pass


        
              
##    for x in range(5):
##        for y in range(5):
##            print entable[x][y]
##            print totalentable[x][y]
##


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

##    if y == 0:
##        return 0
##    ef testtopmin(x,y,q,w,e):
##    c,d = -1,1
##    if y == 0:
##        return 0
##    if x == 0:
##        c =0
##    if x == width -1:
##        d = 0
##    if entable[x+c][y-1] >= entable[x][y-1]:
##        if entable[x+c][y-1] > entable[x+d][y-1]:
##            return entable[x+c][y-1]
##        else:
##            return entable[x+d][y-1]
##    elif entable[x][y-1] > entable[x+d][y-1]:
##        return entable[x][y-1]
##    else:
##        return entable[x+d][y-1]
    
##            a,b,c,d = 1,1,1,1
##            if y == (height -1):
##                a = 0
##            if x == (width - 1):
##                b = 0
##            if y == 0:
##                c = 0
##            if x == 0:
##                d = 0
##            (red1,green1,blue1) = land.getpixel(((x+b),y))
##            (red2, green2, blue2) = land.getpixel(((x-d),y))
##            (red3,green3,blue3) = land.getpixel((x,(y+a)))
##            (red4, green4, blue4) = land.getpixel((x,(y-c)))
##            exred = abs(red1 - red2)
##            exgreen = abs(green1 - green2)
##            exblue = abs(blue1 - blue2)
##            eyred = abs(red3 -red4)
##            eygreen = abs(green3 - green4)
##            eyblue = abs(blue3 -blue4)
##            totxs = (exgreen ** 2) + (exred ** 2) + (exblue ** 2)
##            totys = (eygreen ** 2) + (eyred ** 2) + (eyblue ** 2)
##            totalenergy = (totxs + totys)
##            listenergy.append(totalenergy)
##            listenergy[:1]
##            
land.show()
##    print listenergy
