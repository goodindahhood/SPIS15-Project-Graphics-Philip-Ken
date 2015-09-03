# SPIS15-Project-Graphics-Philip-Ken

First:
  We will create a program that can seam carve any image and resize it without getting rid of very important details.







                
from PIL import Image, ImageDraw

land = Image.open('Animulandscape.jpg')
land3 = Image.open('Animulandscape.jpg')

listenergy = []


global li
global orig
global end
global done
global k
orig = Image.open('Animulandscape.jpg')
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


    





def seampractice(pic, n, li = li):
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
        for y in range(height -1, -1, -1):
            a,b = 1,1
            if y <= (0):
                a = 0
            if x >= (width - 1): #if cases are for when points on edges where outside values cannot be obtained (out of range)
                b = 0
            entable[x][y] = ((abs(table[x][y] - table[x+b][y])) + abs(table[x][y] - table[x][y-a]))
    totalentable = [[0 for sub in range(height)] for subx in range(width)] #creates table for storing total least energy values
    totalentable[0][0] = 0

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
            totalentable[x][y] = entable[x][y] + testleftmin(x,totalentable[x-1][y-1],totalentable[x-1][y+c],totalentable[x-1][y+d])
                #adds the energy values and stores in table

    a = 9999999 #beginning upper value to test for lower value
    mintotalentable = [[0 for i in range(height)] for h in range(2)] #create table of height length to store the mininum total energy for each row. (might not need all the table spaces)
    x = width - 1

    for y in range(height): #only tests for the lowest total energy value on the bottom
        b = totalentable[x][y]
        if a > b: #case to test for the lowest total energy value
            a = b
            mintotalentable[0][y] = b #stores the mininum total energy value
            mintotalentable[1][y] = y #stores x value (might be redunant because of variable 'c'
            c = y                      #stores the x value of the lowest total energy value on the bottom


    newimage = Image.new('RGB', ((width), (height)), (255,0,0)) #creates a new image of 1 less width to put picture
    finy = c        #stores the value of c as finx


    

    for x in range(width - 1, -1, -1): #starts from right then go to left
        for suby in range(-1, 2):
            c,d = -1,1         #Cases for when the x is at the edge where a table value above a point would not be available.
            if finy <= 0 +.5:
                c =0
            if finy >= height - 1.5:
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
            (r,g,b) = pic.getpixel((finx, fory))
            newimage.putpixel((finx, thiy),(r,g,b))
##    if n%5 == 0:
##        newimage.show()
##    newimage.show()


    if n > 1 :
        seampractice((getridcolor(newimage)), n - 1, li)
    if n == 1:
        getridcolor(newimage).show()
##        prseam(li)
##        a = getridcolor(newimage)
##        a.save("Cornercut.jpg")
        
def getridcolor(pic):
    width,height = pic.size
    newimage = Image.new('RGB', (width, height - 1), (255,0,0))
    
    for x in range(width):
        add = 0
        for y in range(height - 1):
            (r,g,b) = pic.getpixel((x, y+add))
            if (r,g,b) == (255,0,0):
                add = 1
                if y + add >= height:
                    add = 0
                (r,g,b) = pic.getpixel((x,y+add))
            else:
                pass 
            newimage.putpixel((x,y),(r,g,b))
    return newimage

def prseam(li):
    height1, width1 = orig.size
    end = Image.new('RGB', ((width1), (height1)), (255,255,255)) 
    for y in range(height1):
        for x in range(width1):
            if li[x][y] == [x,y]:
                pass
            else:
                (r,g,b) = orig.getpixel((x,y))
                end.putpixel((x,y),(r,g,b))
    end.show()







