# Paint_Project
# Janurary 18, 2018
# Paint Project

# Inspirational Saying
# Why break the code into different functions when long formulas make you look cool?
# shiyang made a better program
# Features
# Pencil, Eraser, Ellipse, Rectangle, Spray, Eyedropper, Bucket, Grid, Line, Text, Clear, Save, Load, Fill Ellipse, Fill Rectangle, 6 Stamps
# Shows: Pixel Location, Tool Selected, Colour on the top, Size
# Able to change size for most tools
# Gets file name from module "getname"
# Text tool uses "getname"
# When using the save or load tool, clicking on an existing file name will automatically be typed in the text box
# Be able to use any colour, using the 3 sliders that represents R, G and B
# The power to (un)pause music
# Able to change the size of pixels when using the grid
# Able to erase pixels using mb[2] when using the grid
# Selecting a tool will highlights its border

# Attention to Detail
    # Colour
# If the colour changes, the preview box will change along with it
# Using the eyedropper will adjust the preview box, sliders and value accordingly
# There are 10 colours near the bottom, selecting one of the colours will adjust the preview box, sliders and the values of the colour
# If the colour changes, then the sliders as well as the colour values will change with it

    # Miscellaneous
# Font and Music is from the game (theme)
# If mouse is clicked, then the cursor disappears
# The cursor will not disappear however if it's outside the canvas
# The pixel location is relative to the canvas, in other words, if you go up the top left corner of the canvas, the coords will be (0,0)
# The pixel location will not work unless it's on the canvas
# When using the clear tool, the program will ask the user if they are sure to clear the canvas
# When using the clear tool, you will not be able to interact with anything until you click yes or no
# The window bar is renamed as "Cave Pixel Paint"

    # Load/Save
# Modified getname
# If the user does not add ".picturefile" during saving, it will automatically be saved with ".png"
# Typing nothing will exit load/save
# Changed the font, colour, size and location of the textbox in "getname"
# If the user presses escape, even if there's text in the textbox in "getname", it will delete the text in the textbox and exit
# Typing an invalid file name will not crash

    # Text
# Modified getname (check getname file for comments)
# When using the text tool, you can type very long words and it will not go outside the text box, instead the letters will shift to the left
# If you type a very long word and it starts shifting to the left, you can press the backkey and it will recover the letters that were shifted to the left

from pygame import*
from random import*
from math import*
from getname import *

# Paint Design
screen = display.set_mode((1240,780)) # it's 1240 px by 780 px, fascinating
canvasRect = Rect(0,100,875,680) # canvas size
display.set_caption("Cave Pixel Paint") # the theme is from the 2004 indie game "Cave Story"
screen.fill((255, 255, 255))
running = True

# Icons
cavestoryMainPic = image.load("images/cavestoryMainPic1.png")
pencilPic = image.load("images/pencilPic.png")
eraserPic = image.load("images/eraser1Pic.png")
ellipsePic = image.load("images/ellipsePic.png")
rectPic = image.load("images/rectPic.png")
sprayPic = image.load("images/sprayPic.png")
eyedropperPic = image.load("images/eyedropperPic.png")
bucketPic = image.load("images/bucketPic.png")
gridPic = image.load("images/gridPic.png")
linePic = image.load("images/linePic.png")
textPic = image.load("images/textPic.png")
clearPic = image.load("images/clearPic.png")
savePic = image.load("images/savePic.png")
loadPic = image.load("images/loadPic.png")
fillellipsePic = image.load("images/fillellipsePic.png")
fillrectPic = image.load("images/fillrectPic.png")
playstopPic = image.load("images/playstopPic.png")
slidePic = image.load("images/slidePic.png")
sliderPic = image.load("images/sliderPic.png")
    # Icon Stamps
quoteiconPic = image.load("images/quote1Pic.png")
curlyiconPic = image.load("images/curly1Pic.png")
sueiconPic = image.load("images/sue1Pic.png")
doctoriconPic = image.load("images/doctor1Pic.png")
torokoiconPic = image.load("images/toroko1Pic.png")
miseryiconPic = image.load("images/misery1Pic.png")
    # Stamps to Place On Screen
quotePic = image.load("images/quotePic.png")
curlyPic = image.load("images/curlyPic.png")
suePic = image.load("images/suePic.png")
doctorPic = image.load("images/doctorPic.png")
torokoPic = image.load("images/torokoPic.png")
miseryPic = image.load("images/miseryPic.png")

# Blitting Default Images
screen.blit(cavestoryMainPic,(0,0)) # Main Background
    # Icons
screen.blit(pencilPic, (880, 130))
screen.blit(eraserPic, (880, 190))
screen.blit(ellipsePic, (880, 250))
screen.blit(rectPic, (880,310))
screen.blit(sprayPic,(880,370))
screen.blit(eyedropperPic, (881,431))
screen.blit(bucketPic,(881,490))
screen.blit(gridPic,(880,550))
screen.blit(linePic,(880,610))
screen.blit(textPic,(880,670))
screen.blit(clearPic,(880,730))
screen.blit(savePic, (940,130))
screen.blit(loadPic,(941,190))
screen.blit(fillellipsePic,(940,250))
screen.blit(fillrectPic,(940,310))
screen.blit(playstopPic,(940,370))
screen.blit(quoteiconPic, (940,430))
screen.blit(curlyiconPic, (940,490))
screen.blit(torokoiconPic, (940,550))
screen.blit(sueiconPic, (940,610))
screen.blit(doctoriconPic, (940,670))
screen.blit(miseryiconPic, (940,730))

# Tools
# names of all tools available in the paint program
tools = ["pencil","eraser","ellipse","rectangle","spray","eyedropper","bucket","grid","line","text","clear","save","load","fillcircle","fillrect","play/stop music","quotestamp","curlystamp","torokostamp", "suestamp", "doctorstamp","miserystamp"]
tool = "pencil" # default tool
rects = [] # list that contains all the dimensions of the icon boxes
size = 10 # default size
    # Grid
grid = Surface((875,680)).convert() # surface to draw the grid on
gridon = 0 # flag that detects whether the grid is currently used or not
pixellist= [] # list that will contain all the dot locations when using the grid
originalgrid = Surface((875,780)).convert() # another surface for the same grid, there's 2 grids because the above grid will be drawn on, and the originalgrid will not be changed

# Font
font.init() # initates font
cavestoryfnt = font.Font("Cave_Story.ttf",40) # custom font

# Default tool name
txtPic = cavestoryfnt.render(tool, True, (255,0,0)) # default tool name ("pencil")
draw.rect(screen,(255,255,255),(960,10,230,30)) # white rectangle behind the tool name
screen.blit(txtPic,(960,10))

# Default Pixel Location Preview
pixLoc = cavestoryfnt.render(str((0,0)),True,(255,0,0)) # default pixel coords
draw.rect(screen,(255,255,255),(960,50,230,30)) # white rectangle behind the pixel coords
screen.blit(pixLoc,(960,50))

draw.rect(screen,(255,255,255),canvasRect) # the white canvas

# Colours
# slides are the gray rectangles, sliders are the movable black rectangles
draw.rect(screen,(0,0,0),(95,5,775,95)) # black background for the slides and sliders
colourslide = [(0,0,0),(0,0,0),(0,0,0)] # list that contain the colours for the colourvalue text next to the slides
slideRect = [] # dimensions of the slide rectangles
slideycoord= [10,40,70] # list to hold y coordinates of the slides
colourvalue = [0,0,0] # defaulr colour values, (r,g,b)
colour = (0,0,0) # default colour
colourtxt= cavestoryfnt.render(str(0), True, (0,0,0)) # default colour text next to the slides which is 0
for ycoordslides in slideycoord: # y coords (10,40,70)
    screen.blit(slidePic,(100,ycoordslides)) # places the 3 sliders for the colours
    slideRect.append(Rect(100,ycoordslides,766,25))
    draw.rect(screen,(255,255,255),(880,ycoordslides,70,25)) # draws the white rectangles for the colour text (0-255)
    screen.blit(colourtxt,(880,ycoordslides))
    screen.blit(sliderPic,(95,ycoordslides))
draw.rect(screen,(0,0,0),(0,0,75,75)) # default preview colour box

# Music
mixer.pre_init(44100,-16,2,1024) # doesn't sound great in pygame
mixer.init()
mixer.music.load("songs/cavestoryost.mp3") # original game music from cavestory, the theme of this paint project
mixer.music.play(-1)
mixer.music.pause()
checkpause = 1 # flag that checks if the music is currently paused or not

# Clear Are You Sure
confirm= Surface((1240,780)).convert() # the surface that will overlay everything
confirm.fill((255,0,255)) # refills the grid and sets everything transparent
draw.rect(confirm,(0,0,0),(0,0,1240,780)) # covers the confirm surface with black
confirm.set_alpha(200) # alpha will make it partially black only
confirm.set_colorkey((255,0,255))
confirmtop = cavestoryfnt.render("Confirm Clear?", True, (255,255,255)) # first line
confirmbottom = cavestoryfnt.render("Yes   No", True,(255,255,255)) # second line
confirm.blit(confirmtop,(520,380))
confirm.blit(confirmbottom,(568,420))
yesRect = Rect(568,422,48,20)
noRect = Rect(640,422,38,20)
confirmflag = 0 # flag that checks if the user pressed the clear tool or not

# The border boxes for the tools
for xtoolbox in range(880,941,60):
    for ytoolbox in range(130,780,60):
        draw.rect(screen,(0,0,0),(xtoolbox,ytoolbox,40,40),2) # draws the tool border boxes
        rectdimensions = Rect(xtoolbox,ytoolbox,40,40) # the dimensions of the boxes of the tools
        rects.append(rectdimensions)
draw.rect(screen,(255,0,0),(880,130,40,40),2) # draws the default selected box, which is the pencil box

# The 10 colours at the bottom right of the screen
c = 0 # counter that will count up to 10
boxcolours = 0 # flag, it becomes 1 when it detects that it's using one of the default colours and becomes 0 when the user is using the sliders
colourlist = [(255,0,0),(0,0,255),(255,128,0),(102,0,204),(255,255,0),(255,0,127),(0,255,0),(166,166,166),(0,255,255),(0,0,0)] # list of colours used
colourrect = [] # list that will contain the dimensions of the boxes of the default colours
for xcolourboxes in range(1000,1161,39):
    for ycolourboxes in range(690,731,40):
        draw.rect(screen,colourlist[c],(xcolourboxes,ycolourboxes,40,40)) # draws the default colours
        draw.rect(screen,(0,0,0),(xcolourboxes,ycolourboxes,40,40),2) # draws the borders of the default colours
        colourdimensions = Rect(xcolourboxes,ycolourboxes,40,40)
        colourrect.append(colourdimensions)
        c+= 1

draw.line(screen,(0,0,0),(0,100),(875,100)) # the canvas borders
draw.line(screen,(0,0,0),(0,100),(0,780))
draw.line(screen,(0,0,0),(875,100),(875,780))
draw.line(screen,(0,0,0),(0,780),(875,780))

while running:
    # Colour Preview Box
    screen.set_clip(None)
    draw.rect(screen,colour,(0,0,75,75)) # colour preview box
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            xd,yd = mouse.get_pos() # gets the pos after one click
            copy = screen.copy() # gets a copy of the screen to a surface
            if canvasRect.collidepoint(mx,my):
                mouse.set_visible(False) # mouse becomes invisible when it's pressed unless it's outside of the canvas
        # Scrolling/Scale
            if e.button == 1:
               start = e.pos
            if e.button == 4:
               size += 1
            if e.button == 5:
               size -= 1
            if size<=2: # if the size is too small it resets it back to 2
               size = 2
            if size > 1000: # just for fun
                size = 1000
        if e.type == MOUSEBUTTONUP:
             mouse.set_visible(True) # mouse appears
             # Play/stop music
             if tool == "play/stop music":
                checkpause ^= 1 # everytime the mouse button goes up it will switch from 1 to 0 then then the next time from 0 to 1
                if checkpause == 1:
                    mixer.music.pause() # pause the music
                if checkpause == 0:
                    mixer.music.unpause() # unpause the music
    # Size
    if confirmflag == 0:
        sizetxt = cavestoryfnt.render("size = "+str(size),True,(255,0,0))
        screen.set_clip(None)
        draw.rect(screen,(255,255,255),(960,90,230,30))
        screen.blit(sizetxt,(960,90))

    # Pixel Location
    if canvasRect.collidepoint(mx,my) and confirmflag == 0:
        pixLoc = cavestoryfnt.render(str((mx,my-100)),True,(255,0,0)) # gets the coords of the mouse on the canvas
        screen.set_clip(None)
        draw.rect(screen,(255,255,255),(960,50,230,30)) # draws the white rectangle for the pixel location
        screen.blit(pixLoc,(960,50))
        screen.set_clip(canvasRect)

    # On Click
    if mb[0] == 1 and confirmflag == 0: # confirm flag, if confirm clear is being used, then the user would not be able to interact with anything except for the yes or no option
        for r in rects: # rects is the list that contains the dimensions of the tool icons
            if r.collidepoint(mx,my): # if mouse presses one of the box icon rects
                tn = rects.index(r) # gets the tool number in the list of tools (default is 0)
                tool = tools[tn] # gets the name of the tool (default is "pencil")
                # Tool box selected colour
                for xta in range(880,941,60):
                    for yta in range(130,780,60):
                        screen.set_clip(None)
                        draw.rect(screen,(0,0,0),(xta,yta,40,40),2) # redraws the boxes in black
                        draw.rect(screen,(255,0,0),rects[tn],2) # draws the red highlighted colour on the selected box
                        # Name of the Tool
                        txtPic = cavestoryfnt.render(tool, True, (255,0,0)) # gets the name of the tool from the list
                        draw.rect(screen,(255,255,255),(960,10,230,30)) # draws the white rectangle for the tool name
                        screen.blit(txtPic,(960,10)) # blits the tool name
        # Slide Colour
        for slide in slideRect: # from the slider's dimensions
            if slide.collidepoint(mx,my):
                slidepos = slideRect.index(slide) # gets the slider number, (top is 0, middle is 1, bottom is 2)
                boxcolours = 0 # if it presses one of the sliders
                screen.blit(slidePic,(slideRect[slidepos])) # blits the slide again, to cover up the slider
                colourvaluefrommx = (mx-100)//3 # gets the colour value from the mx value, the width of the slider is exactly 3 times larger than the maximum rgb value (255)
                colourvalue.insert(slidepos,colourvaluefrommx) # it places the new colour value in place of the old colour value
                del colourvalue[slidepos+1] # since when it placed the new colour value, the old value will shift to the right, so this deletes the old colourvalue
                colourtxt= cavestoryfnt.render(str(colourvaluefrommx), True, colourslide[slidepos]) # gets the rgb value and converts it to text form
                draw.rect(screen,(255,255,255),(880,slideycoord[slidepos],70,25)) # draws the white rectangle for the colour text
                screen.blit(colourtxt,(880,slideycoord[slidepos]))
                screen.blit(sliderPic,(mx-5,slideycoord[slidepos]))

        # Default Colour
            for colourdimen in colourrect: # if it clicks on one of the default colours
                if colourdimen.collidepoint(mx,my):
                    boxcolours = 1 # flag changes
                    del colourvalue[:] # will reste everything in the colourvalue list
                    defaultcolour = colourrect.index(colourdimen) # will get the position of the selected colour from the colourrect list
                    for ycoordslides in slideycoord:
                        screen.set_clip(None)
                        screen.blit(slidePic,(100,ycoordslides)) # reblits the slides to cover up the slider
                        draw.rect(screen,(255,255,255),(880,ycoordslides,70,25)) # redraws the white rectangles next to the sliders
                        for posslide in range(0,3): # top slide is 0, middle 1, bottom 2
                            colourvalue.append(colourlist[defaultcolour][posslide]) # will get the new value from the the list of default colours
                            # so colourlist is the list that has the value for all the default colours, defaultcolour will determine which tuple to get and posslide will determine which number from the tuple it will get
                            # colourlist[0][0] will be 255, colourlist[0][1] will be 0
                            colourtxt = cavestoryfnt.render(str(colourlist[defaultcolour][posslide]),True,colourslide[posslide]) # will get the new value and convert it to text form
                            screen.blit(colourtxt,(880,slideycoord[posslide])) # blits the new colourvalues, slideycoord is the list  = [10,40,70]
                            screen.blit(sliderPic,((colourvalue[posslide]*3)+95,slideycoord[posslide])) # will blit the correct position of the sliders according to the default colours

                    for xcolourboxes in range(1000,1161,39): # default colour borders
                        for ycolourboxes in range(690,731,40):
                            screen.set_clip(None)
                            draw.rect(screen,(0,0,0),(xcolourboxes,ycolourboxes,40,40),2) # redraws the borders
                            draw.rect(screen,colour,colourrect[defaultcolour],2) # draws the selected border

                colourslide = [(colourvalue[0],0,0),(0,colourvalue[1],0),(0,0,colourvalue[2])] # the colours for the values next to the slides
                colour = (colourvalue[0],colourvalue[1],colourvalue[2]) # brand new colour

        # Pencil
        if tool == "pencil" and canvasRect.collidepoint(mx,my):
            draw.line(screen,colour,(mx,my),oldmxmy,size+2) # draws lines, oldmxmy is the last pos the mouse was in
            draw.circle(screen,colour,(mx,my),int(size/2)) # draws a circle to make it coherant

        # Eraser
        if tool == "eraser" and canvasRect.collidepoint(mx,my):
            draw.circle(screen,(255,255,255),(mx,my),size) # nothing special about it

        # Ellipse and Filled Ellipse
        if tool == "ellipse" and canvasRect.collidepoint(mx,my) or tool == "fillcircle" and canvasRect.collidepoint(mx,my): # circle and fill circle is used in the same block
            screen.blit(copy,(0,0)) # copys the screen so the circle can be dragged around
            elRect = Rect(xd,yd,(mx-xd),(my-yd)) # create an "invisible" rectangle around the circle
            elRect.normalize() # corrects negative sides
            if elRect[3] <=size*2 or elRect[2] <= size*2 or tool == "fillcircle": # elRect are the coords
                draw.ellipse(screen,colour,elRect,0) # fills the circle
            else:
                draw.ellipse(screen,colour,elRect,size) # doesn't fill the circle

         # Rectangle and Filled Rectangle
        if tool == "rectangle" and canvasRect.collidepoint(mx,my) or tool == "fillrect" and canvasRect.collidepoint(mx,my): # rectangle and fill rectangle is used in the same block
            screen.blit(copy,(0,0))
            if tool == "fillrect":
                draw.rect(screen,colour,(xd,yd,(mx-xd),(my-yd)),0) # draws rectangles, simple enough
            else:
                draw.rect(screen,colour,(xd,yd,(mx-xd),(my-yd)),size)

        # Spray Can
        if tool == "spray" and canvasRect.collidepoint(mx,my):
            randomx = randint(size*-1,size) # x and y range according to the size
            randomy = randint(size*-1,size)
            d = (randomx**2+randomy**2)**0.5 # the diameter of the circle shape that will contain all the dots
            if d<=size:
                draw.circle(screen,colour,(mx+randomx,my+randomy),0) # as long as the diameter is smaller than size

        # Eyedropper
        if tool == "eyedropper" and canvasRect.collidepoint(mx,my):
           boxcolours = 0 # change from default colours to slide colours
           colour = screen.get_at((mx,my))
           del colourvalue[:] # resets colourvalue
           for ycoordslides in slideycoord:
                screen.set_clip(None)
                screen.blit(slidePic,(100,ycoordslides)) # reblits the slides to cover up the slider
                draw.rect(screen,(255,255,255),(880,ycoordslides,70,25)) # redraws the white rectangles next to the sliders

           for posslide in range(0,3):
                colourvalue.append(colour[posslide]) # add on the new colourvalues to the colourvalue
                colourtxt = cavestoryfnt.render(str(colour[posslide]),True,colourslide[posslide])
                screen.blit(colourtxt,(880,slideycoord[posslide])) # will blit the correct colour values
                screen.blit(sliderPic,((colourvalue[posslide]*3)+95,slideycoord[posslide])) # will blit the slider to the correct position

           for xcolourboxes in range(1000,1161,39): # redraws the default colour border boxes because in case the user was using default colours before
                for ycolourboxes in range(690,731,40):
                    screen.set_clip(None)
                    draw.rect(screen,(0,0,0),(xcolourboxes,ycolourboxes,40,40),2)

        # Buckets
        if tool == "bucket" and canvasRect.collidepoint(mx,my):
            clickedcolour = screen.get_at((mx,my)) # the colour the bucket clicks on
            if clickedcolour != colour: # if clicked colour does not equal to current colour
                points =[(mx,my)] # will contain all the points
                while len(points)>0:
                    posx,posy = points.pop() # takes the last value of the list, get it then deletes it from the list
                    if screen.get_at((posx,posy)) == clickedcolour and 0<posx<875 and 100<posy<779:
                        screen.set_at((posx,posy),colour)# takes a point from the list (from posx,posy) and checks if it's the same as the clicked colour
                        # if it's not the same as clicked colour, it sets the colour
                        points.append((posx+1,posy)) # gets the coords of the 4 points around the point the program took from the list
                        points.append((posx-1,posy))
                        points.append((posx,posy+1))
                        points.append((posx,posy-1))

        # Grid
        if tool == "grid":
            grid.fill((255,0,255)) # refills the grid and sets everything transparent
            grid.set_alpha(255)
            grid.set_colorkey((255,0,255))
            originalgrid.fill((255,0,255)) # refills the grid and sets everything transparent
            originalgrid.set_alpha(255)
            originalgrid.set_colorkey((255,0,255))
            if gridon == 0: # detects if the grid has been drawn yet, if it didn't it will copy the screen and create the list
                before = screen.copy()
                pixellist= []
            gridon = 1

            for x in range(0,875,size): # draws the grid
                for y in range(0,780,size):
                    if y<100: # if the grid goes smaller 100 it resets it to 100
                        y = 100
                    draw.line(grid,(0,0,0),(x,y),(x+size,y))
                    draw.line(grid,(0,0,0),(x,y),(x,y+size))
                    draw.line(originalgrid,(0,0,0),(x,y),(x+size,y))
                    draw.line(originalgrid,(0,0,0),(x,y),(x,y+size))

            for i in range (len(pixellist)): # draws the dots on the grid surface
                draw.rect(grid,pixellist[i][0],(pixellist[i][1],pixellist[i][2],size,size))
            screen.blit(before,(0,0)) # i blit the surface without the grid
            screen.blit(grid,(0,0)) # then i blit the surface with the grid because in case the user changes the size of the grid
            draw.rect(screen,colour,(0,0,75,75)) # because the colour might change when i'm using the grid, so I have to update the new colour

            # Because I'm blitting the "before" surface, the colour preview box, the colour sliders, size preview box and pixel location will not change, which is why i have to reblit them
            # Colour Sliders
            for ycoordslides in slideycoord: # redraws the slide
                screen.blit(slidePic,(100,ycoordslides))
                draw.rect(screen,(255,255,255),(880,ycoordslides,70,25))

            for posslide in range(0,3):
                colourvalue.append(colour[posslide])
                colourtxt = cavestoryfnt.render(str(colour[posslide]),True,colourslide[posslide])
                screen.blit(colourtxt,(880,slideycoord[posslide])) # redraws the colour values next to the slides
                screen.blit(sliderPic,((colourvalue[posslide]*3)+95,slideycoord[posslide])) # redraws the sliders

            for colourdimen in colourrect: # when the user uses a default colour when the grid is on
                if colourdimen.collidepoint(mx,my):
                    for xcolourboxes in range(1000,1161,39):
                        for ycolourboxes in range(690,731,40):
                            screen.set_clip(None)
                            draw.rect(screen,(0,0,0),(xcolourboxes,ycolourboxes,40,40),2)
                            draw.rect(screen,colour,colourrect[defaultcolour],2) # redraws selected colour border
            # when the pixel location changes
            draw.rect(screen,(255,255,255),(960,50,200,30)) # white rectangle to cover up the old coord location
            screen.blit(pixLoc,(960,50))
            # when the size changes
            draw.rect(screen,(255,255,255),(960,90,230,30))
            screen.blit(sizetxt,(960,90))

            # Drawing the dots on the grid
            if canvasRect.collidepoint(mx,my):
                screen.set_clip(canvasRect)
                rmx = (mx//size)*size # calculates where dots should be drawn
                rmy = (my//size)*size
                draw.rect(screen,colour,(rmx,rmy,size,size))
                pixellist.append((colour,rmx,rmy)) # adds the colour and the position to a list
            screen.blit(originalgrid,(0,0)) # the original grid does not have the dots, it reblits because otherwise the grid lines will disappear

        if tool != "grid" and gridon == 1: # if the user clicks out of the grid tool
            screen.set_clip(canvasRect)
            screen.blit(before,(0,0)) # blit the surface without the grid
            for i in range (len(pixellist)): # then it draws the pixels from the list
                draw.rect(screen,pixellist[i][0],(pixellist[i][1],pixellist[i][2],size,size))
            gridon = 0 # reset flag

        # Line
        if tool == "line" and canvasRect.collidepoint(mx,my):
            screen.blit(copy,(0,0))
            draw.line(screen,colour,start,(mx,my),size) # start is where you first clicked

        # Text
        if tool == "text" and canvasRect.collidepoint(mx,my):
            screen.set_clip(None) # this is required because otherwise the user will not be able to see the input box
            text = getName(screen, False) # requests text from the user
            textPic = cavestoryfnt.render(text, True, colour)
            screen.set_clip(canvasRect)
            screen.blit(textPic,(mx-textPic.get_width()/2, my-textPic.get_height()/2)) # places text in the middle

        # Save
        if tool == "save":
            screen.set_clip(None)
            txt = getName(screen,True) # requests file name from user
            if "." not in txt: # if the user does not specify which file type, it will be automatically be .png
                txt = txt+".png"
            if txt > ".png": # no file name is bad
                try: # if the user enters an invalid name, it will do nothing
                    image.save(screen.subsurface(canvasRect),txt) # saves canvas
                    screen.set_clip(canvasRect)
                    tool = ""  # after the user saves, the tool must be changed to avoid being stuck in a "save" loop, because the while loop detects that the tool is still "save" and will ask the user to save again
                except:
                    pass
                    tool = ""

        # Load
        if tool == "load":
            txt = getName(screen,True) # requests file name from user
            if txt > "": # no file name, no load
                try: # if the user enters and invalud name, it will do nothing
                    imageload = image.load(txt) # loads the image from system
                    screen.blit(imageload, (0,100))
                    tool = ""
                except:
                    pass
                    tool = ""

        # Stamps
        if tool == "quotestamp" and canvasRect.collidepoint(mx,my):
            screen.blit(copy,(0,0)) # blits copy so it does not blit a trail of images
            screen.blit(quotePic,(mx-150,my-200))

        if tool == "curlystamp" and canvasRect.collidepoint(mx,my):
            screen.blit(copy,(0,0))
            screen.blit(curlyPic,(mx-170,my-200))

        if tool == "torokostamp" and canvasRect.collidepoint(mx,my):
            screen.blit(copy,(0,0))
            screen.blit(torokoPic,(mx-170,my-200))

        if tool == "suestamp" and canvasRect.collidepoint(mx,my):
            screen.blit(copy,(0,0))
            screen.blit(suePic,(mx-170,my-200))

        if tool == "doctorstamp" and canvasRect.collidepoint(mx,my):
            screen.blit(copy,(0,0))
            screen.blit(doctorPic,(mx-100,my-150))

        if tool == "miserystamp"and canvasRect.collidepoint(mx,my):
            screen.blit(copy,(0,0))
            screen.blit(miseryPic,(mx-130,my-200))

    # Clear
    if tool == "clear" and mb[0] == 1:
        if confirmflag == 0:
            screen.set_clip(None)
            beforecopy = screen.copy() # copies the screen before the confirm surface gets blitted on
            screen.blit(confirm,(0,0))
            confirmflag = 1 # user will not be able to interact with anything in the background
        if yesRect.collidepoint(mx,my):
            screen.set_clip(None)
            screen.blit(beforecopy,(0,0))
            draw.rect(screen,(255,255,255),(0,100,875,680)) # will "clear" the canvas by drawing a white rectangle over the canvas
            tool = ""
            confirmflag = 0
        if noRect.collidepoint(mx,my):
            screen.set_clip(None)
            screen.blit(beforecopy,(0,0))
            tool = ""
            confirmflag = 0

    if mb[2] == 1:
        if tool == "grid":
            if canvasRect.collidepoint(mx,my):
                rmx = (mx//size)*size # calculates where the dots should be drawn
                rmy= (my//size)*size
                draw.rect(screen,(255,255,255),(rmx,rmy,size,size)) # draws dots but it's white, so it acts like an eraser
                pixellist.append(((255,255,255),rmx,rmy)) # adds the colour and the position to a list
                screen.blit(originalgrid,(0,0)) # blits back the grid

    draw.line(screen,(0,0,0),(0,100),(875,100)) # redraw the canvas borders
    draw.line(screen,(0,0,0),(0,100),(0,780))
    draw.line(screen,(0,0,0),(875,100),(875,780))
    draw.line(screen,(0,0,0),(0,780),(875,780))

    oldmxmy = (mx,my)
    display.flip()
font.quit()
del cavestoryfnt
quit() # the end