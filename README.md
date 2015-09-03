# SPIS15-Project-Graphics-Philip-Ken

First:
  We will create a program that can seam carve any image and resize it without getting rid of very important details.





                
from PIL import Image, ImageDraw

land = Image.open('test.jpg')
land3 = Image.open('Animulandscape.jpg')

listenergy = []


global li
global orig
global end
global done
global k
orig = Image.open('test.jpg')
width1, height1 = orig.size
li = [[0 for subi in range(height1)] for subu in range(width1)]
end = Image.new('RGB', ((width1), (height1)), (255,255,255))
done =  Image.new('RGB', ((width1), (height1)), (255,0,0))


def testleftmin(x,q,w,e):
    """Compares the energy values above the point indicated (The three values being evaluated are above and above diagonally) Returns the lowest value of energy""" 
    if x == 0:
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
    piccolor = pic.load()
    table = [[0 for suby in range(height)] for subx in range(width)] #Creates table to store basic greyscale value
    for x in range(width):
        for y in range(height):
            
            newred = piccolor[x,y][0] * .21
            newgreen = piccolor[x,y][1] * .72
            newblue = piccolor[x,y][2] * .07
            totalcolor =  int((newred + newgreen + newblue))
##            land2.putpixel((x,y), (totalcolor, totalcolor, totalcolor)) #Calculates Greyscale
            table[x][y] = totalcolor

    entable = [[0 for suby in range(height)] for subx in range(width)] #Creates table to calculates each pixel's energy values

    for x in range(width):
        for y in range(height -1, -1, -1):
            a,b = 1,1
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
        for y in range(height-1, -1, -1):
            c,d = -1,1         #Cases for when the x is at the edge where a table value of a point outside the pic would not be available.
            if y <= 0:             
                c =0
            if y >= height -1:
                d = 0
            totalentable[x][y] = entable[x][y] + testleftmin(x,totalentable[x-1][y],totalentable[x-1][y+c],totalentable[x-1][y+d])
                #adds the energy values and stores in table

    a = 9999999 #beginning upper value to test for lower value
    
    x = width - 1

    for y in range(height): #only tests for the lowest total energy value on the bottom
        b = totalentable[x][y]
        if a > b: #case to test for the lowest total energy value
            a = b
            mintotalentable = b #stores the mininum total energy value
            finy = y                      #stores the x value of the lowest total energy value on the bottom


    newimage = Image.new('RGB', ((width), (height)), (255,0,0)) #creates a new image of 1 less width to put picture



    
    newcolor = newimage.load()
    for x in range(width - 1, -1, -1): #starts from right then go to left
        for suby in range(-1, 2):
            c,d = -1,1         #Cases for when the x is at the edge where a table value above a point would not be available.
            if finy <= 0 +.5:
                c =0
            if finy >= height - .5:
                d = 0
            if finy >= (height -1) - .5:
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
            subz = 1
            thiy = secy
            fory = secy
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
            newcolor[finx,thiy] = piccolor[finx,fory]
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
    newimage = Image.new('RGB', (width, height - 1), (255,0,0))
    piccolor2 = pic.load()
    newcolor2 = newimage.load()
    for x in range(width):
        add = 0
        for y in range(height - 1):
            if piccolor2[x,y] == (255,0,0):
                add = 1
                if y + add >= height - 1.5:
                    add = 0
            else:
                pass
            newcolor2[x,y] = piccolor2[x,y+add]
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








