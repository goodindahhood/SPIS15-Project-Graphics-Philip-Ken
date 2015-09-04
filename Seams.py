



from PIL import Image, ImageDraw

land = Image.open('test.jpg')
land3 = Image.open('Animulandscape.jpg')
land4 = Image.open('TowerDefense.jpg')
land5 = Image.open('Cornercut.jpg')


global li
global orig
global end

orig = Image.open('test.jpg')
width1, height1 = orig.size
li = [[0 for subi in range(2000)] for subu in range(1500)]
end = Image.new('RGB', ((width1), (height1)), (255,255,255))

##@profile
def seampractice(pic, n):
    width, height = pic.size
    width1, height1 = orig.size
    piccolor = pic.load()
    table = [[0 for suby in range(height)] for subx in range(width)] #Creates table to store basic greyscale value
    for x in range(width):
        for y in range(height):
            newred,newgreen,newblue = piccolor[x,y][0] * .21,piccolor[x,y][1] * .72,piccolor[x,y][2] * .07
            table[x][y]  =  int((newred + newgreen + newblue))
##            land2.putpixel((x,y), (totalcolor, totalcolor, totalcolor)) #Calculates Greyscale
             

    entable = [[0 for suby in range(height)] for subx in range(width)] #Creates table to calculates each pixel's energy values

    for x in range(width):
        a,b = 1,1
        for y in range(height):
            if y >= height-1 or x>= width-1:
                if y >= (height -1):
                    a = 0
                if x >= (width - 1): #if cases are for when points on edges where outside values cannot be obtained (out of range)
                    b = 0
            entable[x][y] = ((abs(table[x][y] - table[x+b][y])) + abs(table[x][y] - table[x][y+a]))
    totalentable = [[0 for sub in range(height)] for subx in range(width)] #creates table for storing total least energy values
    totalentable[0][0] = 0


##    newimage2 = Image.new('L', ((width - 1), (height)), (255))
##    for x in range(width - 1):
##        for y in range(height - 1):
##            a = int(entable[x][y])                                #prints Greyscale image
##            newimage2.putpixel((x,y),(a))
##    if n%10 == 0:
##        newimage2.show()

    for y in range(height): #For y and For x need to be in this order where we calculate energy row by row not column by column where above energy values will not be present
        c,d = -1,1         #Cases for when the x is at the edge where a table value above a point would not be available.
        for x in range(width):
            if x <= 0 or x>= width -1:
                if x <= 0:             
                    c =0
                if x >= width -1:
                    d = 0
            totalentable[x][y] = entable[x][y] + min(totalentable[x][y-1],totalentable[x+c][y-1],totalentable[x+d][y-1])             #adds the energy values and stores in table

    a,y = 9999999,height - 1 #beginning upper value to test for lower value     
    for x in range(width): #only tests for the lowest total energy value on the bottom
        b = totalentable[x][y]
        if a > b: #case to test for the lowest total energy value
            a = b
            finx =x                      #stores the x value of the lowest total energy value on the bottom


    newimage = Image.new('RGB', ((width), (height)), (255,0,0)) #creates a new image of 1 less width to put picture



    
    newcolor = newimage.load()
    for y in range(height - 1, -1, -1): #starts from bottom then goes to top
        subz = 1
        c,d = -1,1 #Cases for when the x is at the edge where a table value above a point would not be available.
        for subx in range(-1, 2):
            if finx <= 0:
                c =0
            if finx >= width - 1.5:
                d = 0
            if finx >= (width ) - 1.5:
                if subx == 1:
                    subx = 0
            if finx <= 0 & subx == -1:
                subx = 0
            f = min(totalentable[finx][y],totalentable[finx + d][y],totalentable[finx + c][y])     
            a = totalentable[finx + subx][y]
            if a <= f + .5:
                finx = finx + subx
                finy = y
        for secx in range(width):
            thix = secx
            if secx == finx:
                if thix >= (width -1) - .5:
                    if subz >= 1 - .5:
                        subz = 0
                if thix <= (1 -.5):
                    subz = 0
                thix = thix  - subz
                li[finx][finy] = [finx,finy]                  
##            (r,g,b) = pic.getpixel((forx, finy))
##            newimage.putpixel((thix,finy),(r,g,b))
            newcolor[thix,finy] = piccolor[secx,finy]
    if n%10 == 0:
        newimage.show()
##    newimage.show()


    if n > 1 :
        seampractice((getridcolor(newimage)), n - 1)
    if n == 1:
        getridcolor(newimage).show()
        prseam(li)
##        a = getridcolor(newimage)
##        a.save("Cornercut.jpg")
        

def getridcolor(pic):
    width,height = pic.size
    newimage = Image.new('RGB', (width - 1, height), (255,0,0))
    piccolor2 = pic.load()
    newcolor2 = newimage.load()
    for y in range(height):
        add = 0
        for x in range(width - 1):
            if piccolor2[x,y] == (255,0,0):
                add = 1
                if x + add >= width:
                    add = 0
            else:
                pass 
            newcolor2[x,y] = piccolor2[x+add,y]
    return newimage


def prseam(li):
    origcolor = orig.load()
    endcolor = end.load()
    for y in range(height1):
        for x in range(width1):
            if li[x][y] == [x,y]:
                pass
            else:
                endcolor[x,y] = origcolor[x,y]
    end.show()

##
##import cProfile, pstats, StringIO
##pr = cProfile.Profile()
##pr.enable()
##seampractice(land,2)
##pr.disable()
##s = StringIO.StringIO()
##sortby = 'cumulative'
##ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
##ps.print_stats()
##print s.getvalue()




#################################################################################################



def seampractice1(pic, n):
    width, height = pic.size
    width1, height1 = orig.size
    piccolor = pic.load()
    table = [[0 for suby in range(height)] for subx in range(width)] #Creates table to store basic greyscale value
    for x in range(width):
        for y in range(height):
            
            newred,newgreen,newblue = piccolor[x,y][0] * .21,piccolor[x,y][1] * .72,piccolor[x,y][2] * .07
##            newgreen = piccolor[x,y][1] * .72
##            newblue = piccolor[x,y][2] * .07
            table[x][y] = int((newred + newgreen + newblue))
##            land2.putpixel((x,y), (totalcolor, totalcolor, totalcolor)) #Calculates Greyscale
            

    entable = [[0 for suby in range(height)] for subx in range(width)] #Creates table to calculates each pixel's energy values

    for x in range(width):
        a,b = 1,1
        for y in range(height -1, -1, -1):
            if y <= (0) or x>= (width -1):
                if y <= (0):
                    a = 0
                if x >= (width - 1): #if cases are for when points on edges where outside values cannot be obtained (out of range)
                    b = 0
            entable[x][y] = ((abs(table[x][y] - table[x+b][y])) + abs(table[x][y] - table[x][y-a]))
    totalentable = [[0 for sub in range(height)] for subx in range(width)] #creates table for storing total least energy values
    totalentable[0][height - 1] = 0

##
##    newimage2 = Image.new('L', ((width - 1), (height)), (255))
##    for x in range(width - 1):
##        for y in range(height - 1):
##            a = int(entable[x][y])                                #prints Greyscale image
##            newimage2.putpixel((x,y),(a))
##    if n%10 == 0:
##        newimage2.show()

    for x in range(width): #For y and For x need to be in this order where we calculate energy row by row not column by column where above energy values will not be present
        c,d = -1,1        #Cases for when the x is at the edge where a table value of a point outside the pic would not be available.
        for y in range(height-1, -1, -1):
            if y <= 0 or y >= height -1:
                if y <= 0:             
                    c =0
                if y >= height -1:
                    d = 0
            totalentable[x][y] = entable[x][y] + min(totalentable[x-1][y],totalentable[x-1][y+c],totalentable[x-1][y+d])
                #adds the energy values and stores in table

    a,x = 9999999,width - 1 #beginning upper value to test for lower value  
    for y in range(height): #only tests for the lowest total energy value on the bottom
        b = totalentable[x][y]
        if a > b: #case to test for the lowest total energy value
            a = b
            finy = y                      #stores the x value of the lowest total energy value on the bottom


    newimage = Image.new('RGB', ((width), (height)), (255,0,0)) #creates a new image of 1 less width to put picture



    
    newcolor = newimage.load()
    for x in range(width - 1, -1, -1): #starts from right then go to left
        subz = 1
        c,d = -1,1         #Cases for when the x is at the edge where a table value above a point would not be available.
        for suby in range(-1, 2):
      
            if finy <= 0:
                c =0
            if finy >= height - 1.5:
                d = 0
            if finy >= (height ) - 1.5:
                if suby == 1:
                    suby = 0
            if finy <= 0 & suby == -1:
                suby = 0
            f = min(totalentable[x][finy],totalentable[x][finy + d],totalentable[x][finy + c])
            a = totalentable[x][finy + suby]
            if a <= f + .5:
                finx = x
                finy = finy + suby
        for secy in range(height):
            thiy = secy
            if secy >= finy - .5:
                if secy <= finy +.5:
                    if thiy >= (height -1) - .5:
                        if subz >= 1 - .5:
                            subz = 0
                    if thiy <= (1 -.5):
                        subz = 0
                    thiy = thiy  - subz
                    li[finx][finy] = [finx,finy]                  
##            (r,g,b) = pic.getpixel((finx, fory))
##            newimage.putpixel((finx, thiy),(r,g,b))
            newcolor[finx,thiy] = piccolor[finx,secy]
    if n%10 == 0:
        newimage.show()
##    newimage.show()


    if n > 1 :
        seampractice1((getridcolor1(newimage)), n - 1)
    if n == 1:
        getridcolor1(newimage).show()
        prseam1(li)
##        a = getridcolor(newimage)
##        a.save("Cornercut.jpg")
        
def getridcolor1(pic):
    width,height = pic.size
    newimage = Image.new('RGB', (width, height - 1), (255,0,0))
    piccolor2 = pic.load()
    newcolor2 = newimage.load()
    for x in range(width):
        add = 0
        for y in range(height - 1):
            if piccolor2[x,y] == (255,0,0):
                add = 1
                if y + add >= height:
                    add = 0
            else:
                pass
            newcolor2[x,y] = piccolor2[x,y+add]
    return newimage

def prseam1(li):
    origcolor = orig.load()
    endcolor = end.load()
    for y in range(height1):
        for x in range(width1):
            if li[x][y] == [x,y]:
                pass
            else:
                endcolor[x,y] = origcolor[x,y]
    end.show()








